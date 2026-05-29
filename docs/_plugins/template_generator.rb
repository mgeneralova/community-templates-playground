require "yaml"
require "pathname"

module Jekyll
  class TemplatePageGenerator < Generator
    safe true
    priority :normal

    def generate(site)
      # site.source is the docs/ dir; templates/ lives one level up
      templates_dir = Pathname.new(site.source).parent.join("templates")
      unless templates_dir.exist?
        Jekyll.logger.warn "TemplateGenerator:", "templates dir not found at #{templates_dir}"
        return
      end

      Dir.glob(templates_dir.join("*/meta.yaml")).sort.each do |meta_path|
        template_name = File.basename(File.dirname(meta_path))
        meta = YAML.load_file(meta_path)
        next unless meta.is_a?(Hash)

        body = readme_body(templates_dir, template_name, meta["versions"] || [])
        site.pages << TemplatePage.new(site, template_name, meta, body)
        Jekyll.logger.info "TemplateGenerator:", "added page for #{template_name}"
      end
    end

    private

    def readme_body(templates_dir, name, versions)
      # Sort versions numerically, pick highest
      sorted = versions.sort_by { |v| v.to_s.split(".").map { |n| n.to_i } }.reverse
      sorted.each do |v|
        readme = templates_dir.join(name, v.to_s, "README.md")
        next unless readme.exist?
        return readme.read.sub(/\A#[^\n]*\n+/, "").strip
      end
      ""
    end
  end

  class TemplatePage < Page
    def initialize(site, template_name, meta, body)
      @site  = site
      @base  = site.source
      @dir   = "templates"
      # Use .md so Jekyll converts README Markdown content through kramdown
      @name  = "#{template_name}.md"

      process(@name)

      @data = {
        "layout"              => "integration",
        "title"               => meta["title"] || template_name,
        "folder_path"         => "templates/#{template_name}",
        "tags"                => Array(meta["category"]),
        "categories"          => Array(meta["category"]),
        "status"              => meta["status"] || "active",
        "author"              => meta["author"].to_s,
        "maintainer"          => meta["maintainer"].to_s,
        "last_updated"        => meta["last_updated"].to_s,
        "versions"            => Array(meta["versions"]),
        "zabbix_tested_up_to" => meta["zabbix_tested_up_to"].to_s,
        "community_score"     => meta["weight"] || 0,
        "discussion_count"    => meta["discussion_count"] || 0,
        "open_issues"         => meta["open_issues"] || 0,
        "description"         => meta["description"].to_s,
        "is_template"         => true,
      }

      @content = body
    end
  end
end
