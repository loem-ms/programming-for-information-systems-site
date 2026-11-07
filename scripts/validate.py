"""Check the reviewed public book without executing notebooks or requiring MyST."""
from __future__ import annotations
import argparse
import hashlib
from html.parser import HTMLParser
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
            and bool(weeks) and weeks == list(range(1, len(weeks)+1)) and len(weeks) <= 10,
            'Only a consecutive selection of Weeks 1–10 may be published')
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
    require(Path(name).name not in ('Midterm_Assignment.pdf', 'Final_Assignment.pdf', 'Assignment_Guide.pdf') or list(weeks) == list(range(1, 11)),
            'Later assessment PDF outside all-week release: '+name)


def markdown_parts(path):
    if path.suffix == '.md':
        return [path.read_text()]
    if path.suffix == '.ipynb':
        data = json.loads(path.read_text())
        for cell in data['cells']:
            if cell['cell_type'] == 'code':
                saved_checkpoint = (path.parent.name == 'previews' and
                                    path.name == 'Food_Rescue_System.ipynb' and
                                    'system-checkpoint' in cell.get('metadata', {}).get('tags', []))
                if saved_checkpoint:
                    outputs = cell.get('outputs', [])
                    require(len(outputs) == 1 and outputs[0].get('output_type') == 'stream' and
                            outputs[0].get('name') == 'stdout' and
                            type(cell.get('execution_count')) is int,
                            'Checkpoint must have one saved standard-text example: '+str(path))
                    text = ''.join(outputs[0].get('text', []))
                    require(' / 10' not in text and 'មិនទាន់អនុវត្ត' not in text and 'PLACEHOLDER' not in text,
                            'Learning progress must stay outside the operator display: '+str(path))
                    require(text.count('ប្រព័ន្ធសង្គ្រោះអាហារ') == 1 and
                            all(len(line) <= 60 for line in text.splitlines()),
                            'Checkpoint example missing or wider than 60 characters: '+str(path))
                else:
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


def validate_preview(content, publication, book):
    previews = publication.get('preview_notebooks', [])
    names = [entry.get('name') for entry in previews]
    require(names in ([], ['Food_Rescue_System.ipynb']), 'Unreviewed preview notebook')
    actual = {p.name for p in (content/'previews').glob('*.ipynb')}
    require(actual == set(names), 'Preview reading files differ from explicit allowlist')
    expected_downloads = {'Python_Basics.ipynb', *(f'Week_{w:02}.ipynb' for w in publication['weeks']), *names}
    require({p.name for p in (content/'downloads').glob('*.ipynb')} == expected_downloads,
            'Unexpected standalone notebook download')
    for entry in previews:
        name = entry['name']
        require(entry.get('title') == 'Food Rescue System (preview)', 'Preview menu label missing')
        require(re.fullmatch(r'[0-9a-f]{64}', entry.get('sha256', '')), 'Preview source hash missing')
        section = next(node for node in book['project']['toc'] if node.get('title') == 'Tasks and downloads')
        require({'file':'content/previews/'+name, 'title':entry['title']} in section['children'],
                'Preview must be under Tasks and downloads')
        raw = json.loads((content/'downloads'/name).read_text())
        reading = json.loads((content/'previews'/name).read_text())
        require('skip-execution' in reading['metadata'].get('tags', []), 'Preview execution guard missing')
        require(reading['metadata']['course_draft'].get('saved_checkpoint_outputs') == 10,
                'The ten saved checkpoint examples must be refreshed')
        require([c['source'] for c in raw['cells'] if c['cell_type']=='code'] ==
                [c['source'] for c in reading['cells'] if c['cell_type']=='code'], 'Preview runnable code differs')
        require(raw['metadata']['course_draft']['status'] == 'learning_resource',
                'Preview status missing')
        for notebook in (raw, reading):
            checkpoints = [c for c in notebook['cells']
                           if 'system-checkpoint' in c.get('metadata', {}).get('tags', [])]
            require([c['metadata'].get('checkpoint') for c in checkpoints] == list(range(1, 11)),
                    'The ten ordered progressive system checkpoints are required')
            require(notebook['metadata']['course_draft'].get('system_checkpoints') == 10,
                    'Progressive checkpoint metadata missing')
        launch = ('https://colab.research.google.com/github/' + publication['public_repository']
                  + '/blob/main/content/downloads/' + name)
        for notebook in (raw, reading):
            markdown = '\n'.join(''.join(c['source']) for c in notebook['cells'] if c['cell_type']=='markdown')
            require(']('+launch+')' in markdown, 'Preview Colab target missing')
            require('File → Save a copy in Drive' in markdown, 'Preview personal-copy guidance missing')
            require('announced final rubric' in markdown and 'automatically translated' in markdown,
                    'Student grading guidance or translation notice missing')
            require('LOCAL DRAFT' not in markdown, 'Outdated local-only preview wording')
            for cell in notebook['cells']:
                if cell['cell_type'] == 'markdown':
                    text = ''.join(cell['source'])
                    require(text.count('<details>') == 1 and text.count('</details>') == 1,
                            'Each Khmer explanation must have one closed-by-default toggle')
                    require(text.index('**English**') < text.index('<details>') < text.index('**ភាសាខ្មែរ**'),
                            'English must remain outside the Khmer toggle')
                    require('<summary>' in text and '</summary>' in text, 'Khmer toggle label missing')

            require(not any(value in json.dumps(notebook) for value in ('/Users/', '/workspace/', 'instructor/final_project_notebook_draft')),
                    'Private local path in preview')
            require(sum('student-response' in c.get('metadata', {}).get('tags', []) for c in notebook['cells']) == 9,
                    'Required student response blocks changed')


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
    assessment_pdfs = {'Assignment_Guide.pdf', 'Midterm_Assignment.pdf', 'Final_Assignment.pdf'} if weeks == list(range(1, 11)) else set()
    require({p.name for p in (content/'assignments').glob('*.pdf')} == {f'Week_{w:02}_Assignments.pdf' for w in weeks} | assessment_pdfs, 'Unexpected task PDFs')
    require({p.name for p in (content/'learning_materials').glob('*.ipynb')} ==
            {'Python_Basics.ipynb', *(f'Week_{w:02}.ipynb' for w in weeks)}, 'Unexpected notebook set')
    book = json.loads((folder/'myst.yml').read_text())
    require(book['site']['template'] == 'book-theme', 'Use the standard MyST book theme')
    def entries(nodes):
        for node in nodes:
            if 'file' in node:
                yield node['file']
            yield from entries(node.get('children', []))
    top_level = book['project']['toc']
    require(not any(node.get('title') == 'Before Week 1' for node in top_level),
            'Preparation pages must not be hidden behind a Before Week 1 toggle')
    preparation = ['content/COURSE_OVERVIEW.md', 'content/orientation.md',
                   'content/INSTRUCTOR.md', 'content/SETUP.md']
    require([node.get('file') for node in top_level[1:5]] == preparation and
            top_level[5].get('title') == 'Week 1',
            'The four preparation pages must appear directly before Week 1')
    toc = list(entries(book['project']['toc']))
    for name in toc:
        require((folder/name).is_file(), 'Missing TOC page: '+name)
    pages = {p.relative_to(folder).as_posix() for p in content.rglob('*') if p.suffix in ('.md', '.ipynb') and 'downloads' not in p.parts}
    require(set(toc) == pages, 'Every book page must be explicitly listed in the TOC: '+str(set(toc) ^ pages))
    for week in weeks:
        section = next((node for node in book['project']['toc'] if node.get('title') == f'Week {week}'), {})
        for folder, title in (('assignments', 'Assignment'), ('reflections', 'Reflection form')):
            name = f'{folder}/Week_{week:02}.md'
            require({'file': 'content/'+name, 'title': title} in section.get('children', []),
                    f'Week {week} must contain its {title} menu entry')
            text = (content/name).read_text()
            if folder == 'assignments':
                require(f'](/assignments/Week_{week:02}_Assignments.pdf)' in text and 'mailto:'+email in text,
                        f'Week {week} assignment links must match the existing PDF and submission email')
            elif approved_form_url:
                require(']('+approved_form_url+')' in text and f'**Week {week}**' in text and
                        'not anonymous' in text and 'does not automatically prove attendance' in text,
                        f'Week {week} reflection must use the approved form and explain week/privacy guidance')
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
            require('automatic translation' in markdown, 'Missing Khmer translation warning: '+name)
            require('fluent_review' not in json.dumps(notebook), 'Internal Khmer review metadata: '+name)
            for cell in notebook['cells']:
                if cell['cell_type'] == 'markdown' and cell.get('metadata', {}).get('course_khmer'):
                    translated = ''.join(cell['source'])
                    require(translated.count('<details>') == 1 and translated.count('</details>') == 1,
                            'Each translated cell needs its own Khmer toggle: '+name)
                    require('<details open' not in translated and 'automatic translation</summary>' in translated,
                            'Each Khmer cell toggle must start closed with a warning: '+name)
                    require(bool(translated.split('<details>', 1)[0].strip()),
                            'English must remain before each Khmer cell toggle: '+name)
                if week > 2:
                    continue
                require(not set(cell.get('metadata', {}).get('tags', [])) &
                        {'course-setup', 'course-setup-guide', 'course-figure'}, 'Runtime bootstrap in standalone week: ' + name)
                require('assets/diagrams/' not in ''.join(cell['source']), 'Diagram dependency in standalone week: ' + name)
    for name in ('README.md', 'resources.md', 'assignments/README.md'):
        require('Khmer text is automatically translated' in (content/name).read_text(), 'Missing visible translation warning: '+name)
    internal_note = re.compile(r'(?i)(PUBLIC PREVIEW FOR REVIEW|LOCAL DRAFT FOR INSTRUCTOR REVIEW|Instructor release check|draft translation|fluent_review|will be added after review|pending fluent review|review pending|work[- ]in[- ]progress)')
    for path in content.rglob('*'):
        if path.is_file() and path.suffix in ('.md', '.ipynb'):
            require(not internal_note.search(path.read_text()), 'Internal release note in '+str(path))
    validate_preview(content, publication, book)
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
        for week in weeks:
            for folder in ('assignments', 'reflections'):
                page = html/f'content/{folder}/week-{week:02}/index.html'
                require(page.is_file(), f'Missing rendered weekly {folder} page: '+str(page))
        class WeeklyKhmerToggleCheck(HTMLParser):
            def __init__(self):
                super().__init__()
                self.stack = []
                self.in_summary = False
                self.summary = ''
                self.khmer_toggles = []
            def handle_starttag(self, tag, attrs):
                if tag == 'details':self.stack.append(dict(attrs))
                if tag == 'summary':self.in_summary = True;self.summary = ''
            def handle_data(self, data):
                if self.in_summary:self.summary += data
            def handle_endtag(self, tag):
                if tag == 'summary':
                    if 'automatic translation' in self.summary:
                        require(bool(self.stack), 'Khmer summary is outside details')
                        self.khmer_toggles.append(self.stack[-1])
                    self.in_summary = False
                if tag == 'details':
                    require(bool(self.stack), 'Unbalanced details in weekly HTML')
                    self.stack.pop()
        for week in weeks:
            path = content/f'learning_materials/Week_{week:02}.ipynb'
            notebook = json.loads(path.read_text())
            expected_toggles = sum(c['cell_type'] == 'markdown' and '<!-- course-khmer:start -->' in ''.join(c['source']) for c in notebook['cells'])
            page = html/f'content/learning-materials/week-{week:02}/index.html'
            require(page.is_file(), 'Missing weekly reading page: '+str(page))
            parser = WeeklyKhmerToggleCheck()
            parser.feed(page.read_text())
            require(len(parser.khmer_toggles) == expected_toggles and expected_toggles > 1,
                    f'Week {week} must render a separate Khmer toggle for every translated cell')
            require(all('open' not in attrs for attrs in parser.khmer_toggles) and not parser.stack,
                    f'Week {week} Khmer toggles must be closed and balanced')
        for entry in publication.get('preview_notebooks', []):
            require((html/'downloads'/entry['name']).is_file(), 'Preview static download missing')
            class ToggleCheck(HTMLParser):
                def __init__(self):
                    super().__init__()
                    self.details = []
                    self.summaries = 0
                    self.summary_text = []
                    self.in_summary = False
                    self.depth = 0
                    self.english_inside = False
                    self.in_pre = 0
                    self.pre_text = []
                def handle_starttag(self, tag, attrs):
                    if tag == 'pre':
                        self.in_pre += 1
                        self.pre_text.append('')
                    if tag == 'details':
                        self.details.append(dict(attrs))
                        self.depth += 1
                    if tag == 'summary':
                        self.summaries += 1
                        self.in_summary = True
                        self.summary_text.append('')
                def handle_endtag(self, tag):
                    if tag == 'summary':
                        self.in_summary = False
                    if tag == 'pre':
                        self.in_pre -= 1
                    if tag == 'details':
                        self.depth -= 1
                def handle_data(self, data):
                    if self.in_summary:
                        self.summary_text[-1] += data
                    if self.in_pre:
                        self.pre_text[-1] += data
                    if self.depth and data.strip() == 'English':
                        self.english_inside = True
            parser = ToggleCheck()
            parser.feed((html/'content/previews/food-rescue-system/index.html').read_text())
            expected_toggles = sum(c['cell_type'] == 'markdown' for c in json.loads(
                (content/'previews'/entry['name']).read_text())['cells'])
            notebook = json.loads((content/'previews'/entry['name']).read_text())
            code_toggles = sum('hide-input' in c.get('metadata', {}).get('tags', []) for c in notebook['cells'])
            require(len(parser.details) == expected_toggles + code_toggles and parser.summaries == expected_toggles + code_toggles,
                    'Khmer and provided-code toggles must all render')
            require(sum('automatic translation' in t for t in parser.summary_text) == expected_toggles,
                    'Every Khmer toggle needs its automatic-translation warning')
            require(all('open' not in attrs for attrs in parser.details), 'Khmer toggles must start closed')
            require(not parser.english_inside and parser.depth == 0, 'English must stay outside balanced toggles')
            rendered = [t for t in parser.pre_text if 'ប្រព័ន្ធសង្គ្រោះអាហារ' in t
                        and 'def show_checkpoint' not in t]
            reading = json.loads((content/'previews'/entry['name']).read_text())
            expected_outputs = [''.join(c['outputs'][0]['text']) for c in reading['cells']
                        if c.get('outputs')]
            require(len(rendered) == 10 and [t.strip() for t in rendered] == [t.strip() for t in expected_outputs],
                    'The website must render all ten exact saved checkpoint examples')
        for assessment in assessment_pdfs:
            require((html/'assignments'/assessment).is_file(), 'Assessment static download missing: '+assessment)
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
