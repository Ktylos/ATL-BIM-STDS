"""
Generate changelog from git history for MkDocs site.

Only commits prefixed with [CONTENT] appear in the changelog.
Example commit message: "[CONTENT] Updated DC-GN-001 Section 3.2 MEP naming convention"

All other commits (dev, CI, formatting, etc.) are silently excluded.
"""
import subprocess
import datetime
from pathlib import Path

# How many past releases to show on the changelog page
MAX_RELEASES_SHOWN = 5

# Your GitHub repo URL (no trailing slash)
GITHUB_REPO = "https://github.com/Ktylos/ATL-BIM-STDS"


def get_git_tags():
    """Return list of (tag, date) sorted newest first."""
    cmd = ['git', 'tag', '-l', '--sort=-creatordate',
           '--format=%(refname:short)|%(creatordate:short)']
    result = subprocess.run(cmd, capture_output=True, text=True)
    tags = []
    for line in result.stdout.strip().split('\n'):
        if line and '|' in line:
            tag, date = line.split('|', 1)
            tags.append((tag, date))
    return tags


def get_content_commits(from_ref=None, to_ref=None):
    """
    Return only commits prefixed [CONTENT] in the given range.
    from_ref..to_ref, or from_ref..HEAD if to_ref is None.
    """
    if from_ref and to_ref:
        range_spec = f'{from_ref}..{to_ref}'
    elif from_ref:
        range_spec = f'{from_ref}..HEAD'
    else:
        range_spec = 'HEAD'

    cmd = [
        'git', 'log', range_spec,
        '--pretty=format:%s',
        '--no-merges',
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    lines = [l.strip() for l in result.stdout.strip().split('\n') if l.strip()]
    # Only keep [CONTENT] prefixed commits, strip the prefix for display
    content = []
    for line in lines:
        if line.upper().startswith('[CONTENT]'):
            clean = line[len('[CONTENT]'):].strip()
            content.append(clean)
    return content


def generate_changelog():
    tags = get_git_tags()
    now = datetime.datetime.now().strftime('%B %d, %Y')

    lines = []
    lines.append("# Release Notes\n")
    lines.append(
        "This page summarises standards-level changes in each release. "
        "Only updates that affect the content of the standards are listed here.\n"
    )
    lines.append(
        f"[View full commit history on GitHub]({GITHUB_REPO}/commits/main)"
        "{ .md-button }\n"
    )
    lines.append(f"*Last generated: {now}*\n")
    lines.append("---\n")

    # ── Unreleased changes ────────────────────────────────────────────────
    latest_tag = tags[0][0] if tags else None
    unreleased = get_content_commits(from_ref=latest_tag)

    lines.append("## Unreleased\n")
    if unreleased:
        for item in unreleased:
            lines.append(f"- {item}")
    else:
        lines.append("*No content changes pending release.*")
    lines.append("")

    # ── Tagged releases ───────────────────────────────────────────────────
    if not tags:
        lines.append("*No releases yet.*\n")
    else:
        shown = tags[:MAX_RELEASES_SHOWN]
        for i, (tag, tag_date) in enumerate(shown):
            prev_tag = shown[i + 1][0] if i + 1 < len(shown) else None
            commits = get_content_commits(from_ref=prev_tag, to_ref=tag)

            lines.append(f"## {tag} — {tag_date}\n")
            lines.append(
                f"[Release notes on GitHub]({GITHUB_REPO}/releases/tag/{tag})\n"
            )
            if commits:
                for item in commits:
                    lines.append(f"- {item}")
            else:
                lines.append("*See GitHub for technical changes in this release.*")
            lines.append("")

        if len(tags) > MAX_RELEASES_SHOWN:
            lines.append(
                f"[View all {len(tags)} releases on GitHub]"
                f"({GITHUB_REPO}/releases){{ .md-button }}\n"
            )

    return '\n'.join(lines)


if __name__ == '__main__':
    changelog = generate_changelog()

    output_path = Path('docs/resources/changelog.md')
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(changelog)

    print(f"Changelog written to {output_path}")
