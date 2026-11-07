"""Check the reviewed public book without executing notebooks or requiring MyST."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import tempfile
from urllib.parse import unquote, urlsplit
import zipfile


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_weeks(weeks):
    require(isinstance(weeks, list) and all(type(w) is int for w in weeks)
            and weeks in ([1], [1, 2]), 'Only reviewed Weeks 1–2 may be published')
    return weeks


def validate_contact_email(value):
    require(value == 'submit.progmis@gmail.com', 'Use the approved course contact email')
    return value


def check_name(name, rendered=False, weeks=(1, 2)):
    rel = PurePosixPath(name)
    require(not rel.is_absolute() and '..' not in rel.parts, 'Unsafe public path: '+name)
    require(not any(int(w) not in weeks for w in re.findall(r'Week_([0-9]{2})', name)), 'Future weekly file: '+name)
    # The public INSTRUCTOR.md page legitimately renders to this route.
    allowed_profile = rendered and rel.parts == ('content', 'instructor', 'index.html')
    require(allowed_profile or not any(p in rel.parts for p in ('.git', 'instructor', 'examples', 'notes', '__pycache__')),
            'Private/runtime path: '+name)
    require('_Completed' not in name, 'Completed weekly solution: '+name)
    require(Path(name).name not in ('Midterm_Assignment.pdf', 'Final_Assignment.pdf', 'Assignment_Guide.pdf'),
            'Later assessment PDF: '+name)


def markdown_parts(path):
    if path.suffix == '.md':
        return [path.read_text()]
    if path.suffix == '.ipynb':
        data = json.loads(path.read_text())
        for cell in data['cells']:
            if cell['cell_type'] == 'code':
                require(cell.get('outputs') == [] and cell.get('execution_count') is None,
                        'Notebook output was published: '+str(path))
        return [''.join(c['source']) for c in data['cells'] if c['cell_type'] == 'markdown']
    return []


def validate_reflection_form_url(value):
    """Allow only an explicit Google Forms respondent URL, never edit or data links."""
    if value is None:
        return None
    require(isinstance(value, str), 'Reflection form URL must be a string or null')
    parsed = urlsplit(value)
    require(parsed.scheme == 'https' and not parsed.query and not parsed.fragment,
            'Reflection form URL must use HTTPS without query parameters or fragments')
    short = parsed.netloc == 'forms.gle' and re.fullmatch(r'/[A-Za-z0-9_-]+', parsed.path)
    respondent = parsed.netloc == 'docs.google.com' and re.fullmatch(
        r'/forms/d/(?:e/)?[A-Za-z0-9_-]+/viewform', parsed.path)
    require(short or respondent, 'Reflection form URL must be a Google Forms respondent link')
    return value


def check_form_links(text, approved_form_url, origin):
    form_urls = re.findall(r"https?://(?:docs\.google\.com/forms/|forms\.gle/)[^\s<>\"')\]]+", text)
    for url in form_urls:
        require(url == approved_form_url, 'Unapproved class form in '+str(origin)+': '+url)


def check_links(root, approved_form_url=None):
    for path in root.rglob('*'):
        if not path.is_file():
            continue
        for text in markdown_parts(path):
            check_form_links(text, approved_form_url, path)
            require('https://github.com/loem-ms/programming-for-information-systems/' not in text,
                    'Private repository subresource in public content: '+str(path))
            text = re.sub(r'```.*?```', '', text, flags=re.S)
            links = re.findall(r'\]\(([^\s)]+)\)', text)
            links += re.findall(r'(?:src|href)=[\"\']([^\"\']+)[\"\']', text)
            for target in links:
                parsed = urlsplit(target)
                if parsed.scheme or not parsed.path:
                    continue
                relative = unquote(parsed.path)
                # A raw download is opened beside the support files after extraction.
                origin = root/'learning_materials' if path.parent == root/'downloads' and path.suffix == '.ipynb' else path.parent
                resolved = ((root/relative.lstrip('/')) if relative.startswith('/') else origin/relative).resolve()
                require(root.resolve() in (resolved, *resolved.parents), f'Link leaves publication: {path}: {target}')
                require(resolved.exists(), f'Missing link: {path.relative_to(root)} -> {target}')


def validate(folder, html=None, log=None):
    folder = folder.resolve()
    content = folder/'content'
    publication = json.loads((folder/'publication.json').read_text())
    approved_form_url = validate_reflection_form_url(publication.get('reflection_form_url'))
    weeks = validate_weeks(publication['weeks'])
    email = validate_contact_email(publication.get('contact_email'))
    require(publication['notebook_execution'] == 'disabled', 'Notebook execution must stay disabled')
    expected = {f['path']: f['sha256'] for f in publication['files']}
    actual = {p.relative_to(content).as_posix() for p in content.rglob('*') if p.is_file()}
    require(actual == set(expected), 'Content set changed outside the reviewed export: '+str(actual ^ set(expected)))
    for name, digest in expected.items():
        check_name(name, weeks=weeks)
        path = content/name
        require(not path.is_symlink(), 'Symlink in export: '+name)
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest, 'Changed export bytes: '+name)
    require({p.name for p in (content/'slides').glob('*.pdf')} ==
            {'Orientation.pdf', 'Course_Overview.pdf', 'Setup.pdf', *(f'Week_{w:02}_Slides.pdf' for w in weeks)}, 'Unexpected lesson PDFs')
    require({p.name for p in (content/'assignments').glob('*.pdf')} == {f'Week_{w:02}_Assignments.pdf' for w in weeks}, 'Unexpected task PDFs')
    require({p.name for p in (content/'learning_materials').glob('*.ipynb')} ==
            {'Python_Basics.ipynb', *(f'Week_{w:02}.ipynb' for w in weeks)}, 'Unexpected notebook set')
    book = json.loads((folder/'myst.yml').read_text())
    require(book['site']['template'] == 'book-theme', 'Use the standard MyST book theme')
    def entries(nodes):
        for node in nodes:
            if 'file' in node:
                yield node['file']
            yield from entries(node.get('children', []))
    toc = list(entries(book['project']['toc']))
    for name in toc:
        require((folder/name).is_file(), 'Missing TOC page: '+name)
    pages = {p.relative_to(folder).as_posix() for p in content.rglob('*') if p.suffix in ('.md', '.ipynb') and 'downloads' not in p.parts}
    require(set(toc) == pages, 'Every book page must be explicitly listed in the TOC: '+str(set(toc) ^ pages))
    for path in (content/'learning_materials').glob('*.ipynb'):
        require('skip-execution' in json.loads(path.read_text())['metadata']['tags'], 'Missing execution guard')
    for name in ('README.md', 'INSTRUCTOR.md', 'COURSE_LINKS.md', 'assignments/README.md'):
        require('mailto:'+email in (content/name).read_text(), 'Missing course email: '+name)
    require(not re.search(r"\bI(?:['’]\w+)?\b", (content/'INSTRUCTOR.md').read_text()), 'First-person instructor introduction')
    require({p.name for p in (content/'downloads').glob('*.zip')} ==
            {'Python_Basics.zip', *(f'Week_{w:02}.zip' for w in weeks)}, 'Unexpected ZIP set')
    # Colab must launch the runnable raw weekly copy, never the generic home page.
    for week in weeks:
        name = f'Week_{week:02}.ipynb'
        launch = ('https://colab.research.google.com/github/' + publication['public_repository']
                  + '/blob/main/content/downloads/' + name)
        require('](' + launch + ')' in (content/'README.md').read_text(), 'Missing direct weekly Colab link')
        for folder in ('downloads', 'learning_materials'):
            notebook = json.loads((content/folder/name).read_text())
            markdown = '\n'.join(''.join(c['source']) for c in notebook['cells'] if c['cell_type'] == 'markdown')
            require('](' + launch + ')' in markdown, 'Wrong Colab notebook target: ' + name)
            require('](https://colab.research.google.com/)' not in markdown, 'Generic Colab target: ' + name)
            for cell in notebook['cells']:
                require(not set(cell.get('metadata', {}).get('tags', [])) &
                        {'course-setup', 'course-setup-guide', 'course-figure'}, 'Runtime bootstrap in standalone week: ' + name)
                require('assets/diagrams/' not in ''.join(cell['source']), 'Diagram dependency in standalone week: ' + name)
    check_links(content, approved_form_url)
    for archive_path in (content/'downloads').glob('*.zip'):
        with zipfile.ZipFile(archive_path) as archive:
            names = archive.namelist()
            require(len(names) == len(set(names)), 'Duplicate ZIP entries')
            for name in names:
                check_name(name, weeks=weeks)
            require('learning_materials/Python_Basics.ipynb' in names, 'Missing Basics notebook')
            require('learning_materials/programs/first_pickup.py' in names, 'Missing Week 1 support')
            selected = int(archive_path.stem[5:]) if archive_path.stem.startswith('Week_') else None
            if selected:
                require(f'learning_materials/Week_{selected:02}.ipynb' in names, 'Missing weekly notebook')
            require(not any(int(w) != selected for n in names for w in re.findall(r'Week_([0-9]{2})', n)),
                    'Wrong weekly material in '+archive_path.name)
            require(email in archive.read('README.md').decode(), 'Missing ZIP contact email')
            with tempfile.TemporaryDirectory() as tmp:
                archive.extractall(tmp)
                check_links(Path(tmp), approved_form_url)
    if html:
        require((html/'index.html').is_file(), 'MyST HTML entry point is missing')
        for path in html.rglob('*'):
            if path.is_file():
                check_name(path.relative_to(html).as_posix(), rendered=True, weeks=weeks)
        for name in ('slides/Setup.pdf', 'slides/Orientation.pdf', 'slides/Course_Overview.pdf',
                     *(f'{folder}/Week_{w:02}{suffix}' for w in weeks for folder, suffix in (
                         ('slides', '_Slides.pdf'), ('assignments', '_Assignments.pdf'),
                         ('downloads', '.zip'), ('downloads', '.ipynb')))):
            require((html/name).is_file(), 'Static download missing from MyST output: '+name)
    if log:
        issues = [line for line in log.read_text().splitlines() if any(marker in line for marker in (
            '⛔', 'Duplicate identifier', 'No target for internal reference', 'Cross reference target was not found'))]
        require(not issues, 'MyST reported broken content:\n'+'\n'.join(issues))
    print(f'PASS {len(toc)} book pages, {len(expected)} content files, Weeks {weeks} PDFs/notebooks, links and rebuilt ZIPs.')
    print('PASS static reading edition: no notebook execution or private repository subresources; only the explicitly approved reflection form is allowed.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('folder', type=Path)
    parser.add_argument('--html', type=Path)
    parser.add_argument('--log', type=Path)
    args = parser.parse_args()
    validate(args.folder, args.html, args.log)
