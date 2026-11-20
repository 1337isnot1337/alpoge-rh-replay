"""Keep the README tables compact while publishing every row on linked pages."""

import json

PREVIEW_ROWS = 20
PAGE_ROWS = 250
TABLES = {
    'active-volunteers': ('active', 'Active claims awaiting evidence', 'No active claims awaiting evidence.'),
    'pending-volunteers': ('pending', 'Submitted for review', 'No submissions awaiting review.'),
    'volunteers': ('reviewed', 'Reviewed volunteer evidence', 'No reviewed volunteer evidence yet.'),
}


def update_table(root, readme, marker, lines):
    name, title, empty = TABLES[marker]
    start, end = f'<!-- {marker}-start -->', f'<!-- {marker}-end -->'
    directory = root / 'tracker' / 'volunteer-tables' / name
    directory.mkdir(parents=True, exist_ok=True)
    header, rows = lines[:2], lines[2:]
    index = [f'# {title}', '', f'{len(rows):,} entries.', '']
    written = set()
    for offset in range(0, len(rows), PAGE_ROWS):
        chunk = rows[offset:offset + PAGE_ROWS]
        page = f'page-{offset // PAGE_ROWS + 1:03d}.md'
        written.add(page)
        index.append(f'- [Entries {offset + 1:,}–{offset + len(chunk):,}]({page})')
        content = [f'# {title}', '', '[All pages](README.md)', '', *header,
                   *(row.replace('](evidence/', '](../../../evidence/') for row in chunk)]
        (directory / page).write_text('\n'.join(content) + '\n', encoding='utf-8')
    for stale in directory.glob('page-*.md'):
        if stale.name not in written:
            stale.unlink()
    (directory / 'README.md').write_text('\n'.join(index) + '\n', encoding='utf-8')

    if rows:
        rendered = '\n'.join([f'[{len(rows):,} entries. View the full table]'
                              f'(tracker/volunteer-tables/{name}/README.md).', '',
                              *header, *rows[-PREVIEW_ROWS:]])
    else:
        rendered = empty
    before, suffix = readme.split(start, 1)
    _, after = suffix.split(end, 1)
    return f'{before}{start}\n\n{rendered}\n\n{end}{after}'


def update_reviewed(root, readme):
    header = ['| Contributor | Task | Modules | Review |', '|---|---|---:|---|']
    receipts = [(path, json.loads(path.read_text()))
                for path in (root / 'evidence' / 'volunteers').glob('*.json')]
    rows = []
    for path, receipt in sorted(receipts, key=lambda item: (item[1].get('reviewed_utc', ''), item[0].name)):
        contributor, task = receipt['contributor'], receipt['packet']
        rows.append(f"| [@{contributor}](https://github.com/{contributor}) | [{task}]({receipt['claim']}) "
                    f"| {len(receipt['tasks'])} | [Build evidence verified](evidence/volunteers/{path.name}) |")
    return update_table(root, readme, 'volunteers', header + rows)
