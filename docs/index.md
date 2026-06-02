---
layout: default
title: Home
description: A comprehensive directory of community-maintained Zabbix monitoring templates
permalink: /
---

<div class="container">
    <!-- Hero Section -->
    <div class="hero-section" style="text-align: center; margin-bottom: 3rem;">
        <h1 style="color: #D40000; margin-bottom: 1rem;">Zabbix Community Templates</h1>
        <p style="font-size: 1.2rem; color: #7F8C8D; max-width: 600px; margin: 0 auto;">
            Discover, explore, and contribute to a growing collection of community-maintained Zabbix monitoring templates. 
            Find templates for your infrastructure, apply to become a maintainer, or report any issues.
        </p>
        
        <!-- Search Bar -->
        <div style="margin-top: 2rem;">
            <input type="text" class="search-input" placeholder="Search templates..." 
                   style="width: 100%; max-width: 500px; padding: 12px 16px; border: 2px solid #0275B8; border-radius: 6px; font-size: 1rem;">
        </div>
    </div>

    <!-- Filter Section -->
    <div style="margin-bottom: 2rem; display: flex; gap: 1rem; flex-wrap: wrap; justify-content: center;">
        <a href="{{ '/' | relative_url }}" class="btn btn-secondary" style="cursor: pointer;">All Templates</a>
        <a href="{{ '/' | relative_url }}?tag=Cloud" class="btn btn-secondary" style="cursor: pointer;">Cloud</a>
        <a href="{{ '/' | relative_url }}?tag=Network" class="btn btn-secondary" style="cursor: pointer;">Network</a>
        <a href="{{ '/' | relative_url }}?tag=Monitoring" class="btn btn-secondary" style="cursor: pointer;">Monitoring</a>
    </div>

    <!-- Templates Grid -->
    {% assign template_pages = site.pages | where_exp: "p", "p.dir == '/templates/'" | sort: "community_score" | reverse %}
    <div class="cards-grid">
        {% for tmpl in template_pages %}
            <div class="card">
                <div class="card-header">
                    <h2 class="card-title">{{ tmpl.title }}</h2>
                </div>
                
                <p class="card-description">{{ tmpl.description | truncatewords: 20 }}</p>
                
                <!-- Status Badge -->
                <div style="margin-bottom: 1rem;">
                    <span class="badge badge-{{ tmpl.status }}">
                        {{ tmpl.status | capitalize }}
                    </span>
                </div>
                
                <!-- Tags -->
                {% if tmpl.tags %}
                <div class="tags">
                    {% for tag in tmpl.tags %}
                        <a href="{{ '/' | relative_url }}?tag={{ tag }}" class="tag">{{ tag }}</a>
                    {% endfor %}
                </div>
                {% endif %}
                
                <!-- Actions -->
                <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 1rem;">
                    <a href="{{ tmpl.url | relative_url }}" class="btn btn-primary">View Details</a>
                    <a href="https://github.com/{{ site.repository }}/tree/main/{{ tmpl.folder_path }}" 
                       target="_blank" class="btn btn-secondary">Repository</a>
                    <a href="https://github.com/{{ site.repository }}/issues/new?title=Issue:%20{{ tmpl.title }}" 
                       target="_blank" class="btn btn-danger">Report</a>
                </div>
            </div>
        {% endfor %}
    </div>

    <!-- Empty State -->
    {% if template_pages.size == 0 %}
    <div style="text-align: center; padding: 3rem; background: white; border-radius: 8px; border: 1px solid #E1E8ED;">
        <h3 style="color: #7F8C8D;">No templates found</h3>
        <p>Add templates to the <code>templates/</code> directory with a <code>meta.yaml</code> file.</p>
    </div>
    {% endif %}

    <!-- Call to Action -->
    <div style="margin-top: 4rem; padding: 2rem; background: linear-gradient(135deg, #0A466A 0%, #0275B8 100%); 
                border-radius: 12px; color: white; text-align: center;">
        <h2 style="color: white; margin-bottom: 1rem;">Want to contribute?</h2>
        <p style="margin-bottom: 1.5rem; color: rgba(255, 255, 255, 0.9);">
            Help the community by maintaining a template, creating a new one, or improving documentation.
        </p>
        <a href="https://github.com/{{ site.repository }}/blob/main/CONTRIBUTING.md" target="_blank" class="btn btn-primary">
            Learn How to Contribute
        </a>
    </div>
</div>
