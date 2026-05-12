# Contributing to Zabbix Community Templates

Thank you for your interest in contributing to the Zabbix Community Templates project! This document provides guidelines and instructions for contributing.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Ways to Contribute](#ways-to-contribute)
3. [Getting Started](#getting-started)
4. [Submitting Changes](#submitting-changes)
5. [Template Standards](#template-standards)
6. [Questions?](#questions)

## Code of Conduct

This project adheres to the Contributor Covenant Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## Ways to Contribute

### Report Bugs
- Use the [Bug Report](https://github.com/mgeneralova/community-templates-playground/issues/new?template=bug_report.md) template
- Provide clear reproduction steps
- Include Zabbix version and environment details
- Attach relevant logs

### Suggest Features
- Use the [Feature Request](https://github.com/mgeneralova/community-templates-playground/issues/new?template=feature_request.md) template
- Explain the use case and benefits
- Suggest implementation approaches

### Create Templates
- Create new monitoring templates for uncovered technologies
- Follow the [Template Standards](#template-standards)
- Include comprehensive documentation
- Provide examples and troubleshooting tips

### Maintain Templates
- Apply via [Maintainer Application](https://github.com/mgeneralova/community-templates-playground/issues/new?template=maintainer_application.md)
- Keep templates updated with latest Zabbix versions
- Respond to issues and user questions
- Improve documentation

### Improve Documentation
- Enhance existing documentation
- Add more examples and use cases
- Fix typos and clarity issues
- Create tutorials

## Getting Started

### Prerequisites

- Git
- Ruby 3.0+
- Jekyll 4.0+
- Basic understanding of Zabbix and YAML

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/mgeneralova/community-templates-playground.git
cd community-templates-playground

# Install dependencies
bundle install

# Serve locally
bundle exec jekyll serve

# Visit http://localhost:4000
```

## Submitting Changes

### Branch Naming

Use descriptive branch names:
- `feature/template-name` - New template
- `fix/template-name-issue` - Bug fix
- `docs/update-documentation` - Documentation updates

### Commit Messages

Write clear, descriptive commit messages:

```
feat: Add Prometheus monitoring template

- Include metrics collection setup
- Add custom dashboards
- Update documentation with examples
```

### Pull Request Process

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes
4. **Test** locally with `bundle exec jekyll serve`
5. **Commit** with clear messages
6. **Push** to your fork
7. **Open** a pull request

### PR Template

```markdown
## Description
Brief description of changes.

## Type of Change
- [ ] New template
- [ ] Bug fix
- [ ] Documentation update
- [ ] Template improvement

## Testing
How have you tested these changes?

## Checklist
- [ ] I have tested this locally
- [ ] I have updated documentation
- [ ] I have followed the template standards
- [ ] My code follows the style guidelines
```

## Template Standards

### Front Matter

Every template must include complete front matter:

```yaml
---
layout: integration
title: "Integration Name"
folder_path: "Category/Subfolder"
tags: ["Tag1", "Tag2"]
categories: ["Category"]
status: "active"
author: "github_username"
maintainer: "github_username"
last_updated: "YYYY-MM-DD"
description: "One sentence description"
---
```

### Content Structure

Templates should include:

- **Overview**: What does it monitor?
- **Features**: Key capabilities
- **Installation**: Step-by-step setup
- **Configuration**: Configuration options
- **Metrics**: Metrics collected (table format)
- **Dashboards**: Available dashboards
- **Troubleshooting**: Common issues and solutions
- **Support**: Links and resources

### Quality Standards

- ✅ Clear and complete documentation
- ✅ Tested with current Zabbix versions
- ✅ Proper code formatting and examples
- ✅ Accurate links and references
- ✅ Professional writing quality

### Status Definitions

- **active**: Actively maintained, tested, and supported
- **stale**: Not recently updated, may need maintenance
- **unmaintained**: No longer actively maintained
- **experimental**: New or experimental

## Style Guidelines

### Writing

- Use clear, concise language
- Use active voice when possible
- Include examples for complex concepts
- Provide links to official documentation

### Code Examples

```markdown
\`\`\`bash
# Comment explaining what this does
command --option
\`\`\`

\`\`\`json
{
  "example": "configuration"
}
\`\`\`
```

### Links

```markdown
- Internal: [Link text](../contribute.md)
- External: [Text](https://example.com)
- GitHub: [Repository](https://github.com/mgeneralova/community-templates-playground)
```

## Maintenance Guidelines

If you're a template maintainer:

### Responsibilities

- **Respond** to issues within 7 days
- **Test** updates with current Zabbix LTS versions
- **Review** pull requests promptly
- **Update** documentation as needed
- **Communicate** status changes

### Update Frequency

- Check for Zabbix updates monthly
- Review issues weekly
- Test with new Zabbix versions after release
- Update `last_updated` field when changes made

### Stepping Down

If you can no longer maintain a template:

1. Announce in repository
2. Update template status to `stale`
3. Help transition to new maintainer
4. Update documentation accordingly

## Review Process

### Automated Checks

- YAML validation
- HTML proof reading (links)
- Jekyll build test

### Manual Review

- Content quality
- Documentation completeness
- Code examples accuracy
- Template standards compliance

### Approval

- At least one maintainer approval required
- All automated checks must pass
- Discussion resolved if needed

## Questions?

- **Issues**: [GitHub Issues](https://github.com/mgeneralova/community-templates-playground/issues)
- **Discussions**: [GitHub Discussions](https://github.com/mgeneralova/community-templates-playground/discussions)
- **Email**: Check repository for contact info

## Recognition

Contributors are recognized:
- In template metadata (author/maintainer fields)
- In GitHub contributors list
- In project announcements

Thank you for contributing! 🎉
