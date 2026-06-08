---
layout: default
title: Submit a Template
permalink: /submit.html
---

<div class="container">
  <div style="max-width: 740px; margin: 0 auto; padding: 2rem 0;">

    <h1>Submit a Template</h1>
    <p style="font-size: 1.1rem; color: #7F8C8D; margin-bottom: 2rem;">
      No Git experience needed. Fill out a simple form and a pull request is created for you automatically.
    </p>

    <!-- How it works -->
    <div style="background: #EAF4FB; border-left: 4px solid #0275B8; padding: 1.25rem 1.5rem; border-radius: 4px; margin-bottom: 2.5rem;">
      <strong style="display: block; margin-bottom: 0.75rem; color: #0A466A;">How it works</strong>
      <ol style="margin: 0; padding-left: 1.25rem; line-height: 1.8;">
        <li>Click <strong>Submit via Form</strong> below — it opens a structured form on GitHub</li>
        <li>Fill in the details (title, description, category, template content)</li>
        <li>Submit — a pull request is created automatically in the background</li>
        <li>A maintainer reviews and merges your template into the directory</li>
      </ol>
    </div>

    <!-- CTA -->
    <div style="text-align: center; margin: 2.5rem 0;">
      <a href="https://github.com/{{ site.repository }}/issues/new?template=submit_template.yml"
         target="_blank"
         class="btn btn-primary"
         style="font-size: 1.05rem; padding: 0.875rem 2.25rem; display: inline-block;">
        Submit via Form
      </a>
      <p style="margin-top: 1rem; color: #95A5A6; font-size: 0.9rem;">
        Opens GitHub — a free account is required
      </p>
    </div>

    <hr style="margin: 2.5rem 0; border: none; border-top: 1px solid #E1E8ED;">

    <!-- What to include -->
    <h2>What to include</h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; margin-bottom: 2rem;">
      <div style="background: white; border: 1px solid #E1E8ED; border-radius: 8px; padding: 1.25rem;">
        <h3 style="margin-top: 0; color: #0275B8; font-size: 1rem;">Required</h3>
        <ul style="margin: 0; padding-left: 1.25rem; line-height: 1.8;">
          <li>Template title</li>
          <li>Short description</li>
          <li>Category</li>
          <li>Your GitHub username</li>
          <li>Tested Zabbix versions</li>
        </ul>
      </div>
      <div style="background: white; border: 1px solid #E1E8ED; border-radius: 8px; padding: 1.25rem;">
        <h3 style="margin-top: 0; color: #7F8C8D; font-size: 1rem;">Optional but helpful</h3>
        <ul style="margin: 0; padding-left: 1.25rem; line-height: 1.8;">
          <li>Template XML/YAML content</li>
          <li>README / installation guide</li>
          <li>Dashboard screenshot</li>
        </ul>
      </div>
    </div>

    <!-- Tip for large files -->
    <div style="background: #FFF8E6; border-left: 4px solid #F5A623; padding: 1.25rem 1.5rem; border-radius: 4px; margin-bottom: 2.5rem;">
      <strong>Have a large template file?</strong>
      You can paste just a few lines in the form and attach the full file as a comment on the GitHub issue after submitting.
    </div>

    <hr style="margin: 2.5rem 0; border: none; border-top: 1px solid #E1E8ED;">

    <!-- What happens after -->
    <h2>What happens after you submit</h2>
    <ol style="line-height: 2;">
      <li>A GitHub issue is created with your submission details</li>
      <li>A GitHub Action reads the form and opens a pull request with your template files</li>
      <li>The bot posts a link to the PR on your issue so you can track progress</li>
      <li>A maintainer reviews the PR and may ask follow-up questions</li>
      <li>Once approved and merged, your template appears on this site within minutes</li>
    </ol>

    <hr style="margin: 2.5rem 0; border: none; border-top: 1px solid #E1E8ED;">

    <!-- Git users -->
    <h2>Prefer to use Git?</h2>
    <p>
      If you're comfortable with Git, check out the
      <a href="{{ '/contribute.html' | relative_url }}">contribution guide</a>
      to submit a pull request directly — you'll have more control over the folder structure and versioning.
    </p>

  </div>
</div>
