#!/usr/bin/env python3
"""Process a new-integration issue and open a PR automatically."""

import os
import re
import subprocess
import sys
from pathlib import Path


def parse_issue_body(body: str) -> dict:
    """Parse GitHub issue form body into a {label: value} dict.

    Issue forms render as sections separated by '### Heading' lines.
    """
    body = body.replace('\r\n', '\n')
    fields = {}
    for section in re.split(r'\n### ', '\n' + body)[1:]:
        lines = section.split('\n')
        key = lines[0].strip()
        value = '\n'.join(lines[1:]).strip()
        if value == '_No response_':
            value = ''
        fields[key] = value
    return fields


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text.strip('-')


def run(cmd: list, **kwargs) -> subprocess.CompletedProcess:
    print('$', ' '.join(cmd))
    return subprocess.run(cmd, check=True, **kwargs)


def comment(issue_number: str, body: str):
    run(['gh', 'issue', 'comment', issue_number, '--body', body])


def main():
    issue_body = os.environ['ISSUE_BODY']
    issue_number = os.environ['ISSUE_NUMBER']
    issue_user = os.environ['ISSUE_USER']

    fields = parse_issue_body(issue_body)

    title = fields.get('Template Title', '').strip()
    description = fields.get('Description', '').strip()
    category = fields.get('Category', 'Other').strip()
    author = fields.get('Your GitHub Username', '').strip() or issue_user
    zabbix_versions = fields.get('Tested Zabbix Versions', '7.0').strip()
    status = fields.get('Template Status', 'experimental').strip()
    template_content = fields.get('Template File Content', '').strip()
    readme_content = fields.get('README / Documentation', '').strip()

    if not title:
        comment(issue_number,
                "Could not find a **Template Title** in your submission. "
                "Please edit the issue and make sure the title field is filled in.")
        sys.exit(1)

    slug = slugify(title)
    if not slug:
        comment(issue_number,
                f"Could not generate a valid folder name from title: `{title}`. "
                "Please use alphanumeric characters.")
        sys.exit(1)

    template_dir = Path(f"templates/{slug}")
    if template_dir.exists():
        comment(issue_number,
                f"A template folder `templates/{slug}/` already exists in the repository. "
                "Please check if your template is already there, or adjust the title to make it unique.")
        sys.exit(0)

    # Determine the version folder from the highest listed version
    versions = [v.strip() for v in re.split(r'[,\s]+', zabbix_versions) if v.strip()]
    if not versions:
        versions = ['7.0']

    def version_key(v):
        try:
            return [int(x) for x in v.split('.')]
        except ValueError:
            return [0]

    latest_version = sorted(versions, key=version_key)[-1]
    branch_name = f"new-integration/issue-{issue_number}-{slug}"

    run(['git', 'config', 'user.email', 'github-actions[bot]@users.noreply.github.com'])
    run(['git', 'config', 'user.name', 'github-actions[bot]'])
    run(['git', 'checkout', '-b', branch_name])

    version_dir = template_dir / latest_version
    version_dir.mkdir(parents=True)

    # Build README
    if not readme_content:
        readme_content = f"""## Overview

{description}

## Author

@{author}

## Requirements

- Zabbix {latest_version}+

## Installation

1. Import the template into your Zabbix instance via **Configuration → Templates → Import**.
2. Assign the template to a host.

## Configuration

<!-- Add macro/configuration details here -->
"""

    (version_dir / 'README.md').write_text(readme_content)

    # Write template file if provided
    if template_content:
        ext = 'xml' if template_content.lstrip().startswith('<') else 'yaml'
        (version_dir / f'template.{ext}').write_text(template_content)

    run(['git', 'add', str(template_dir)])
    run(['git', 'commit', '-m',
         f"feat: Add {title} template\n\nSubmitted via issue #{issue_number} by @{issue_user}."])
    run(['git', 'push', 'origin', branch_name])

    versions_str = ', '.join(versions)
    file_status = ('Template file included' if template_content
                   else 'Template file **not yet provided** — please attach it as a PR comment')

    pr_body = f"""## New Template Submission

Automatically created from issue #{issue_number} submitted by @{issue_user}.

| Field | Value |
|-------|-------|
| **Title** | {title} |
| **Folder** | `templates/{slug}/` |
| **Author** | @{author} |
| **Category** | {category} |
| **Tested Zabbix Versions** | {versions_str} |
| **Status** | `{status}` |
| **Template file** | {file_status} |

Closes #{issue_number}

---

### Reviewer Checklist
- [ ] Template imports without errors in Zabbix
- [ ] Description is accurate and helpful
- [ ] Category is appropriate
- [ ] README has clear installation instructions
- [ ] Template file is attached / included
"""

    result = subprocess.run(
        ['gh', 'pr', 'create',
         '--title', f"feat: Add {title} template",
         '--body', pr_body,
         '--head', branch_name,
         '--base', 'main',
         '--label', 'new-integration'],
        capture_output=True, text=True
    )

    if result.returncode != 0:
        # Label may not exist yet — retry without it
        result = subprocess.run(
            ['gh', 'pr', 'create',
             '--title', f"feat: Add {title} template",
             '--body', pr_body,
             '--head', branch_name,
             '--base', 'main'],
            capture_output=True, text=True
        )

    if result.returncode != 0:
        print(f"::error::Failed to create PR: {result.stderr}")
        sys.exit(1)

    pr_url = result.stdout.strip()
    print(f"PR created: {pr_url}")

    comment(issue_number,
            f"Thanks for your submission, @{issue_user}! \n\n"
            f"A pull request has been automatically created: {pr_url}\n\n"
            "A maintainer will review it shortly. "
            "If you didn't include the template file in the form, please attach it as a comment here or directly on the PR.")

    # Best-effort: mark the issue as in-review
    subprocess.run(['gh', 'issue', 'edit', issue_number, '--add-label', 'in-review'],
                   capture_output=True)


if __name__ == '__main__':
    main()
