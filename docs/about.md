---
layout: default
title: About
permalink: /about.html
---

# About Zabbix Community Templates

## Mission

The Zabbix Community Templates portal is a collaborative platform dedicated to providing high-quality, community-maintained monitoring templates for the Zabbix platform. Our mission is to democratize infrastructure monitoring and make it accessible to organizations of all sizes.

## What We Do

We maintain a curated collection of templates that extend Zabbix's capabilities across various technologies, cloud platforms, databases, and infrastructure components. Each template is maintained by dedicated community members who ensure quality, documentation, and ongoing support.

## Core Values

### Quality
- Templates are tested and validated
- Clear documentation for setup and configuration
- Regular updates for new Zabbix versions

### Community-Driven
- Built by and for the Zabbix community
- Open contribution model
- Transparent maintenance and issue tracking

### Accessibility
- Free and open-source
- Easy to discover and implement
- Comprehensive documentation

### Support
- Active community support through GitHub Issues
- Discussion forums for best practices
- Responsive maintainers

## Template Status Definitions

### Active ✅
Regularly maintained, tested with current Zabbix versions, and actively supported. Issues are addressed promptly.

### Stale ⚠️
Previously active but not recently updated. May work with current Zabbix versions but needs community contributions or maintainer attention.

### Unmaintained 🔴
No longer actively maintained. Use at your own risk. Community contributions welcome to revive these templates.

### Experimental 🧪
New or experimental templates. May have limited testing and documentation. Feedback welcome.

## Get Started

### For Users
1. **Browse** our collection of templates
2. **Review** template status and documentation
3. **Import** the template into your Zabbix instance
4. **Configure** according to your environment
5. **Report** any issues or improvements

### For Contributors
1. **Create** new templates for uncovered technologies
2. **Maintain** existing templates by responding to issues
3. **Improve** documentation and examples
4. **Share** best practices with the community

## Technology Stack

- **Platform**: GitHub Pages with Jekyll
- **Comments**: Giscus (GitHub Discussions)
- **Status Badges**: Shields.io
- **Design**: Responsive CSS Grid with Zabbix brand colors
- **Fonts**: Gotham Pro, Roboto

## Project Statistics

- **Templates**: {{ site.integrations | size }} and growing
- **Contributors**: Active community members
- **Last Updated**: {{ site.time | date: "%Y-%m-%d" }}

## Support & Contact

- **Issues**: [Report on GitHub](https://github.com/{{ site.repository }}/issues)
- **Discussions**: [Join our discussions](https://github.com/{{ site.repository }}/discussions)
- **Repository**: [Source code](https://github.com/{{ site.repository }})

## License

All templates are provided under the MIT License unless otherwise specified. See [LICENSE](../LICENSE) for details.

## Acknowledgments

We thank the entire Zabbix community for their contributions, feedback, and support. Together, we're making monitoring accessible and powerful for everyone.

---

**Last Updated:** {{ site.time | date: "%B %d, %Y" }}
