require "yaml"
require "pathname"

module Jekyll
  class TemplatePageGenerator < Generator
    safe true
    priority :normal

    def generate(site)
      # Walk up from docs/_plugins/ → docs/ → repo root → templates/
      templates_dir = Pathname.new(File.expand_path("../../templates", File.dirname(__FILE__)))

      Jekyll.logger.info "TemplateGenerator:", "__FILE__      = #{__FILE__}"
      Jekyll.logger.info "TemplateGenerator:", "templates_dir = #{templates_dir}"
      Jekyll.logger.info "TemplateGenerator:", "exists?       = #{templates_dir.exist?}"

      unless templates_dir.exist?
        Jekyll.logger.warn "TemplateGenerator:", "templates/ not found, skipping"
        return
      end

      meta_files = Dir.glob(templates_dir.join("*/meta.yaml")).sort
      Jekyll.logger.info "TemplateGenerator:", "meta.yaml files found: #{meta_files.size}"

      meta_files.each do |meta_path|
        template_name = File.basename(File.dirname(meta_path))
        meta = YAML.load_file(meta_path)
        next unless meta.is_a?(Hash)

        raw  = readme_body(templates_dir, template_name, meta["versions"] || [])
        body = site.find_converter_instance(Jekyll::Converters::Markdown).convert(raw)
        site.pages << TemplatePage.new(site, template_name, meta, body)
        Jekyll.logger.info "TemplateGenerator:", "added page: #{template_name}"
      end
    end

    private

    def readme_body(templates_dir, name, versions)
      versions.sort_by { |v| Gem::Version.new(v.to_s) rescue v.to_s }.reverse.each do |v|
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
      @name  = "#{template_name}.html"

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
        "screenshot"          => meta["screenshot"] || false,
        "description"         => meta["description"].to_s,
      }

      @content = body
    end
  end
end
