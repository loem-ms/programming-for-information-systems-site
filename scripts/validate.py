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


def check_name(name, rendered=False):
    rel = PurePosixPath(name)
    require(not rel.is_absolute() and '..' not in rel.parts, 'Unsafe public path: '+name)
    require(not re.search(r'Week_(?!01)[0-9]{2}', name), 'Future weekly file: '+name)
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


def check_links(root):
    for path in root.rglob('*'):
        if not path.is_file():
            continue
        for text in markdown_parts(path):
            require('docs.google.com/forms/' not in text, 'Private class form in '+str(path))
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
    require(publication['weeks'] == [1], 'Unexpected pilot scope')
    require(publication['notebook_execution'] == 'disabled', 'Notebook execution must stay disabled')
    expected = {f['path']: f['sha256'] for f in publication['files']}
    actual = {p.relative_to(content).as_posix() for p in content.rglob('*') if p.is_file()}
    require(actual == set(expected), 'Content set changed outside the reviewed export: '+str(actual ^ set(expected)))
    for name, digest in expected.items():
        check_name(name)
        path = content/name
        require(not path.is_symlink(), 'Symlink in export: '+name)
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest, 'Changed export bytes: '+name)
    require({p.name for p in (content/'slides').glob('*.pdf')} ==
            {'Orientation.pdf', 'Course_Overview.pdf', 'Setup.pdf', 'Week_01_Slides.pdf'}, 'Unexpected lesson PDFs')
    require({p.name for p in (content/'assignments').glob('*.pdf')} == {'Week_01_Assignments.pdf'}, 'Unexpected task PDFs')
    require({p.name for p in (content/'learning_materials').glob('*.ipynb')} ==
            {'Week_01.ipynb', 'Python_Basics.ipynb'}, 'Unexpected notebook set')
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
    check_links(content)
    for archive_path in (content/'downloads').glob('*.zip'):
        with zipfile.ZipFile(archive_path) as archive:
            names = archive.namelist()
            require(len(names) == len(set(names)), 'Duplicate ZIP entries')
            for name in names:
                check_name(name)
            require('learning_materials/Python_Basics.ipynb' in names, 'Missing Basics notebook')
            require('learning_materials/programs/first_pickup.py' in names, 'Missing Week 1 support')
            if archive_path.stem == 'Week_01':
                require('learning_materials/Week_01.ipynb' in names, 'Missing weekly notebook')
            else:
                require(not any('Week_01' in n for n in names), 'Weekly material in Basics ZIP')
            with tempfile.TemporaryDirectory() as tmp:
                archive.extractall(tmp)
                check_links(Path(tmp))
    if html:
        require((html/'index.html').is_file(), 'MyST HTML entry point is missing')
        for path in html.rglob('*'):
            if path.is_file():
                check_name(path.relative_to(html).as_posix(), rendered=True)
        for name in ('slides/Setup.pdf', 'slides/Orientation.pdf', 'slides/Course_Overview.pdf',
                     'slides/Week_01_Slides.pdf', 'assignments/Week_01_Assignments.pdf',
                     'downloads/Week_01.zip', 'downloads/Week_01.ipynb'):
            require((html/name).is_file(), 'Static download missing from MyST output: '+name)
    if log:
        issues = [line for line in log.read_text().splitlines() if any(marker in line for marker in (
            '⛔', 'Duplicate identifier', 'No target for internal reference', 'Cross reference target was not found'))]
        require(not issues, 'MyST reported broken content:\n'+'\n'.join(issues))
    print(f'PASS {len(toc)} book pages, {len(expected)} content files, Week 1-only PDFs/notebooks, links and rebuilt ZIPs.')
    print('PASS static reading edition: no notebook execution, class form or private repository subresources.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('folder', type=Path)
    parser.add_argument('--html', type=Path)
    parser.add_argument('--log', type=Path)
    args = parser.parse_args()
    validate(args.folder, args.html, args.log)
