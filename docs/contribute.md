---
layout: default
title: Contribute
permalink: /contribute.html
---

# How to Contribute

We welcome contributions from the Zabbix community! Whether you want to create new templates, improve existing ones, or help with documentation, there's a place for you.

## Ways to Contribute

### 1. Create a New Template

Is there a technology or service you'd like to monitor with Zabbix? Create a new template!

**Steps:**
1. Fork the repository
2. Create a new Markdown file in `_integrations/` folder
3. Follow the [template structure](#template-structure)
4. Add your template with documentation
5. Submit a pull request

### 2. Maintain an Existing Template

Help keep our templates up-to-date and working!

**To apply as a maintainer:**
- [Open a "Maintainer Application" issue](https://github.com/{{ site.repository }}/issues/new?template=maintainer_application.md)
- Tell us which template you want to maintain
- Describe your Zabbix experience and maintenance plan

**Maintainer responsibilities:**
- Respond to issues within 7 days
- Test with current Zabbix LTS versions
- Update documentation as needed
- Help users with implementation questions

### 3. Report Issues

Found a broken template or have ideas for improvements?

- [Report broken template](https://github.com/{{ site.repository }}/issues/new?template=broken_report.md)
- [Request a feature](https://github.com/{{ site.repository }}/issues/new?template=feature_request.md)
- [Report a bug](https://github.com/{{ site.repository }}/issues/new?template=bug_report.md)

### 4. Improve Documentation

Help us make documentation clearer and more comprehensive.

- Update existing template documentation
- Add more examples and use cases
- Improve this website

### 5. Share & Promote

Help others discover our templates!

- Share on social media
- Write blog posts about templates you use
- Mention this project in your Zabbix communities

## Template Structure

Each template file in `_integrations/` must follow this structure:

```markdown
---
layout: integration
title: "Template Name"
folder_path: "Category/Subfolder"
tags: ["Tag1", "Tag2", "Tag3"]
categories: ["Category1", "Category2"]
status: "active"  # active, stale, unmaintained, experimental
author: "your_github_username"
maintainer: "github_username"
last_updated: "2024-05-12"
description: "One-line description of what this template does"
---

## Overview

Explain what this template monitors and its key features.

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

Step-by-step installation instructions.

## Configuration

How to configure the template.

## Metrics

What metrics does it collect?

## Troubleshooting

Common issues and solutions.

## Support

Links to documentation and support resources.
```

## Front Matter Details

| Field | Required | Description |
|-------|----------|-------------|
| `layout` | Yes | Always use `integration` |
| `title` | Yes | Template name |
| `folder_path` | Yes | Folder path in repository |
| `tags` | Yes | Array of tags |
| `categories` | Yes | Array of categories |
| `status` | Yes | `active`, `stale`, `unmaintained`, or `experimental` |
| `author` | No | Original author |
| `maintainer` | No | Current maintainer |
| `last_updated` | Yes | Last update date (YYYY-MM-DD) |
| `description` | Yes | One-line description |

## Code of Conduct

We're committed to providing a welcoming and inclusive environment for all contributors.

- Be respectful and professional
- Give credit to others' work
- Help new contributors feel welcome
- Report inappropriate behavior to maintainers

## Development Setup

### Local Testing

```bash
# Clone the repository
git clone https://github.com/{{ site.repository }}.git
cd community-templates-playground

# Install dependencies
bundle install

# Build and serve locally
bundle exec jekyll serve

# Visit http://localhost:4000
```

### Testing Your Template

1. Add your template to `_integrations/`
2. Run `bundle exec jekyll serve`
3. Check that:
   - Template renders correctly
   - All links work
   - Status badges display properly
   - Code examples are properly formatted

## Pull Request Guidelines

When submitting a pull request:

1. **Clear title**: Describe what you're adding/fixing
2. **Description**: Explain the changes and why
3. **Testing**: Confirm you've tested locally
4. **One template per PR**: Keep PRs focused and reviewable

Example PR title:
- `feat: Add Prometheus template`
- `docs: Update AWS CloudWatch documentation`
- `fix: Correct Nginx Plus installation steps`

## Questions?

- Open a discussion: [GitHub Discussions](https://github.com/{{ site.repository }}/discussions)
- Check existing issues
- Review template documentation

## Recognition

Contributors will be recognized in:
- The template's "Author" and "Maintainer" fields
- Repository contributors list
- Project announcements

Thank you for helping make Zabbix monitoring better! 🚀
