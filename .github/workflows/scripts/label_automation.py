#!/usr/bin/env python3
"""
Label automation for template issues.

Runs on issue events and on a daily schedule (see label_automation.yml).

Rules from TEMPLATE_SPEC.md:
  - broken/outdated open + no maintainer response in 14 days → apply update_needed to template
  - broken open + no maintainer response in 60 days          → apply broken to template
  - No version in supported_versions.json                    → apply update_needed to template

  - claim-maintainer issue opened → notify team (comment), leave for team to act
  - clear-maintainer  issue opened → notify team (comment), leave for team to act

Maintainer changes (claim/clear) always require Zabbix team approval and are never automated.
"""

import json
import os
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

import requests
import yaml

REPO        = os.environ["REPO"]
TOKEN       = os.environ.get("GITHUB_TOKEN", "")
EVENT_NAME  = os.environ.get("EVENT_NAME", "schedule")
ISSUE_NUM   = os.environ.get("ISSUE_NUMBER", "")

HEADERS = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"}
API     = "https://api.github.com"

SUPPORTED_VERSIONS_PATH = Path("docs/_data/supported_versions.json")
TEMPLATES_DIR           = Path("templates")

# Days of silence before automated label escalation
DAYS_UPDATE_NEEDED = 14
DAYS_BROKEN        = 60


# ---------------------------------------------------------------------------
# GitHub API helpers
# ---------------------------------------------------------------------------

def gh(method, path, **kwargs):
    r = requests.request(method, f"{API}{path}", headers=HEADERS, timeout=15, **kwargs)
    r.raise_for_status()
    return r.json() if r.content else {}


def list_open_issues(label=None):
    params = {"state": "open", "per_page": 100}
    if label:
        params["labels"] = label
    return gh("GET", f"/repos/{REPO}/issues", params=params)


def list_issue_comments(issue_number):
    return gh("GET", f"/repos/{REPO}/issues/{issue_number}/comments",
              params={"per_page": 100})


def add_label(issue_number, label):
    gh("POST", f"/repos/{REPO}/issues/{issue_number}/labels", json={"labels": [label]})


def post_comment(issue_number, body):
    gh("POST", f"/repos/{REPO}/issues/{issue_number}/comments", json={"body": body})


# ---------------------------------------------------------------------------
# Template helpers
# ---------------------------------------------------------------------------

def load_supported_versions():
    with open(SUPPORTED_VERSIONS_PATH) as f:
        return json.load(f)


def find_template_for_issue(issue_title, issue_body):
    """
    Best-effort: match issue text against known template names.
    Returns the template directory Path or None.
    """
    text = f"{issue_title} {issue_body or ''}".lower()
    for d in sorted(TEMPLATES_DIR.iterdir()):
        if d.is_dir() and (d / "meta.yaml").exists():
            if d.name.lower() in text:
                return d
    return None


def set_template_status(template_dir: Path, status: str):
    """Update the status field in meta.yaml."""
    meta_path = template_dir / "meta.yaml"
    with open(meta_path) as f:
        meta = yaml.safe_load(f)
    if meta.get("status") == status:
        return False  # already set, no change
    meta["status"] = status
    with open(meta_path, "w") as f:
        yaml.dump(meta, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    print(f"  Set {template_dir.name} status → {status}")
    return True


def get_maintainer(template_dir: Path):
    meta_path = template_dir / "meta.yaml"
    with open(meta_path) as f:
        meta = yaml.safe_load(f)
    return meta.get("maintainer", "").strip()


# ---------------------------------------------------------------------------
# Staleness check
# ---------------------------------------------------------------------------

def maintainer_replied(issue_number, maintainer_login):
    """Return True if the maintainer has commented on this issue."""
    if not maintainer_login:
        return False
    for comment in list_issue_comments(issue_number):
        if comment["user"]["login"].lower() == maintainer_login.lower():
            return True
    return False


def issue_age_days(issue):
    created = datetime.fromisoformat(issue["created_at"].rstrip("Z")).replace(tzinfo=timezone.utc)
    return (datetime.now(timezone.utc) - created).days


def process_stale_issues():
    """
    Daily sweep: check broken and outdated issues for staleness rules.
    """
    supported_versions = load_supported_versions()

    for label in ("broken", "outdated"):
        for issue in list_open_issues(label=label):
            age = issue_age_days(issue)
            template_dir = find_template_for_issue(
                issue["title"], issue.get("body", ""))

            if template_dir is None:
                continue

            maintainer = get_maintainer(template_dir)
            replied = maintainer_replied(issue["number"], maintainer)

            if label == "broken" and age >= DAYS_BROKEN and not replied:
                # Escalate to broken status on the template
                if set_template_status(template_dir, "broken"):
                    post_comment(
                        issue["number"],
                        f"⚠️ This issue has been open for {age} days with no maintainer "
                        f"response. The template has been marked **broken**. "
                        f"@Zabbix team: please review."
                    )

            elif age >= DAYS_UPDATE_NEEDED and not replied:
                # Mark template as update_needed
                if set_template_status(template_dir, "update_needed"):
                    post_comment(
                        issue["number"],
                        f"This issue has been open for {age} days with no maintainer "
                        f"response. The template has been flagged as **update_needed**."
                    )

    # Also flag any template whose versions don't match supported_versions
    for template_dir in sorted(TEMPLATES_DIR.iterdir()):
        meta_path = template_dir / "meta.yaml"
        if not meta_path.exists():
            continue
        with open(meta_path) as f:
            meta = yaml.safe_load(f)
        versions = [str(v) for v in meta.get("versions", [])]
        if not any(v in supported_versions for v in versions):
            set_template_status(template_dir, "update_needed")


# ---------------------------------------------------------------------------
# Issue event handlers
# ---------------------------------------------------------------------------

def handle_issue_event():
    """
    Triggered when an issue is opened or labeled.
    Handles: claim-maintainer, clear-maintainer — notifies the team.
    """
    if not ISSUE_NUM:
        return

    issue = gh("GET", f"/repos/{REPO}/issues/{ISSUE_NUM}")
    labels = [l["name"] for l in issue.get("labels", [])]
    title  = issue.get("title", "")
    body   = issue.get("body", "")

    if "claim-maintainer" in labels:
        # Notify team; they act manually
        post_comment(
            ISSUE_NUM,
            "👋 **Maintainer claim received.**\n\n"
            "The Zabbix team will review this request and update `meta.yaml` if approved. "
            "No automated action will be taken — maintainer changes always require team approval."
        )
        print(f"  Notified team about claim-maintainer on issue #{ISSUE_NUM}")

    if "clear-maintainer" in labels:
        post_comment(
            ISSUE_NUM,
            "👋 **Maintainer removal requested.**\n\n"
            "The Zabbix team has been notified. Clearing the maintainer field requires "
            "explicit team approval and will never happen automatically."
        )
        print(f"  Notified team about clear-maintainer on issue #{ISSUE_NUM}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    if EVENT_NAME == "issues":
        handle_issue_event()
    else:
        # Daily schedule: sweep for stale issues
        process_stale_issues()

    print("Done.")


if __name__ == "__main__":
    main()
