#!/usr/bin/env python3
"""
Daily stats update: reads templates/*/meta.yaml, fetches live GitHub stats,
recomputes status and weight, writes updated meta.yaml.

Runs as a GitHub Action (see .github/workflows/update_meta.yml).
Requires: GITHUB_TOKEN, REPO env vars.
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path

import requests
import yaml

REPO = os.environ["REPO"]
TOKEN = os.environ.get("GITHUB_TOKEN", "")
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"}
API = "https://api.github.com"

SUPPORTED_VERSIONS_PATH = Path("docs/_data/supported_versions.json")
TEMPLATES_DIR = Path("templates")


def load_supported_versions():
    with open(SUPPORTED_VERSIONS_PATH) as f:
        return json.load(f)


def gh_search(query):
    """Run a GitHub search query and return total_count."""
    r = requests.get(f"{API}/search/issues",
                     headers=HEADERS,
                     params={"q": f"repo:{REPO} {query}", "per_page": 1},
                     timeout=15)
    r.raise_for_status()
    return r.json().get("total_count", 0)


def fetch_issue_counts(template_name):
    """Return (open_issues, closed_issues) for issues mentioning the template name."""
    try:
        total = gh_search(f"is:issue {template_name}")
        open_count = gh_search(f"is:issue is:open {template_name}")
        return open_count, max(0, total - open_count)
    except Exception:
        return 0, 0


def fetch_discussion_count(template_name):
    """Return number of discussions mentioning the template name."""
    try:
        return gh_search(f"is:discussion {template_name}")
    except Exception:
        return 0


def compute_status(meta, supported_versions):
    """
    Derive status from version compatibility.
    broken/update_needed labels (applied by label_automation) take priority
    over the version-based check, so preserve them if already set.
    """
    versions = [str(v) for v in meta.get("versions", [])]
    version_compatible = any(v in supported_versions for v in versions)

    current = meta.get("status", "active")
    if current == "broken":
        return "broken"  # only cleared by Zabbix team
    if not version_compatible:
        return "update_needed"
    if current == "update_needed":
        return "update_needed"  # label still present; label_automation clears it
    return "active"


def compute_weight(meta, open_issues, closed_issues, discussion_count):
    """
    Community weight formula (see TEMPLATE_SPEC.md — Weight / Ranking).
    Caps at 380 for community templates; official templates start at 1000+.
    """
    status = meta.get("status", "active")
    has_maintainer = bool(str(meta.get("maintainer", "")).strip())
    has_screenshot = meta.get("screenshot", False)

    discussion_score  = min(discussion_count * 5, 150)           # capped at 150
    ratio             = min(closed_issues / (open_issues + 1), 4)
    issue_score       = int(ratio * 20)                           # capped at 80
    maintainer_score  = 100 if has_maintainer else 0
    screenshot_score  = 50  if has_screenshot  else 0
    penalty           = (-100 if status == "update_needed" else
                         -999 if status == "broken"       else 0)

    return (discussion_score + issue_score + maintainer_score
            + screenshot_score + penalty)


def update_template(template_dir: Path, supported_versions: list):
    meta_path = template_dir / "meta.yaml"
    if not meta_path.exists():
        return

    with open(meta_path) as f:
        meta = yaml.safe_load(f)
    if not isinstance(meta, dict):
        return

    name = template_dir.name
    print(f"Updating {name}...")

    open_issues, closed_issues = fetch_issue_counts(name)
    discussion_count           = fetch_discussion_count(name)

    meta["status"]       = compute_status(meta, supported_versions)
    meta["open_issues"]  = open_issues
    meta["discussion_count"] = discussion_count
    meta["last_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    meta["weight"]       = compute_weight(meta, open_issues, closed_issues,
                                          discussion_count)
    meta["screenshot"]   = (template_dir / "dashboard.png").exists()

    # Preserve the authoritative field order from the spec
    with open(meta_path, "w") as f:
        yaml.dump(meta, f, default_flow_style=False, allow_unicode=True,
                  sort_keys=False)

    print(f"  status={meta['status']}  weight={meta['weight']}  "
          f"open_issues={open_issues}  discussions={discussion_count}")


def main():
    supported_versions = load_supported_versions()

    for template_dir in sorted(TEMPLATES_DIR.iterdir()):
        if template_dir.is_dir() and (template_dir / "meta.yaml").exists():
            update_template(template_dir, supported_versions)

    print("\nDone.")


if __name__ == "__main__":
    main()
