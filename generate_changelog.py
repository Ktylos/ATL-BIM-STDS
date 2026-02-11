"""
Generate changelog from git history for MkDocs site
Supports tracking from a specific date/commit and grouping by releases
"""
import subprocess
import datetime
from pathlib import Path
import re

# Configuration
CHANGELOG_START_DATE = "2026-01-01"  # Start tracking from this date (YYYY-MM-DD)
# Or use a specific commit: CHANGELOG_START_COMMIT = "abc123def"
MAX_COMMITS = 500  # Maximum commits to process

def get_git_tags():
    """Get all git tags (releases) with dates"""
    cmd = ['git', 'tag', '-l', '--sort=-creatordate', '--format=%(refname:short)|%(creatordate:short)']
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    tags = {}
    for line in result.stdout.strip().split('\n'):
        if line and '|' in line:
            tag, date = line.split('|', 1)
            tags[tag] = date
    return tags

def get_git_log_since_date(since_date):
    """Get git log since a specific date"""
    cmd = [
        'git', 'log',
        f'--since={since_date}',
        '--pretty=format:%ad|%s|%an|%H',
        '--date=short',
        '--no-merges',
        f'-{MAX_COMMITS}'
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip().split('\n')

def get_commits_between_tags(tag1, tag2=None):
    """Get commits between two tags (or tag and HEAD)"""
    if tag2:
        range_spec = f'{tag2}..{tag1}'
    else:
        range_spec = f'{tag1}..HEAD'
    
    cmd = [
        'git', 'log',
        range_spec,
        '--pretty=format:%ad|%s|%an',
        '--date=short',
        '--no-merges'
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip().split('\n')

def categorize_commit(message):
    """Categorize commit based on message"""
    message_lower = message.lower()
    
    if any(word in message_lower for word in ['feat:', 'feature:', 'add']):
        return ('✨ New Features', message)
    elif any(word in message_lower for word in ['fix:', 'bug:', 'resolve']):
        return ('🐛 Bug Fixes', message)
    elif any(word in message_lower for word in ['doc:', 'docs:', 'documentation']):
        return ('📚 Documentation', message)
    elif any(word in message_lower for word in ['style:', 'format:', 'css']):
        return ('💎 Style & Formatting', message)
    elif any(word in message_lower for word in ['refactor:', 'restructure']):
        return ('♻️ Code Refactoring', message)
    elif any(word in message_lower for word in ['update', 'improve']):
        return ('🔨 Improvements', message)
    else:
        return ('📝 Other Changes', message)

def generate_changelog():
    """Generate markdown changelog with releases and chronological view"""
    tags = get_git_tags()
    commits = get_git_log_since_date(CHANGELOG_START_DATE)
    
    # Build changelog
    changelog = []
    changelog.append("# Recent Updates & Release History\n")
    changelog.append("This page tracks all changes to the ATL BIM Standards documentation.\n")
    changelog.append("!!! info \"Tracking Information\"")
    changelog.append(f"    **Tracking Since**: {CHANGELOG_START_DATE}")
    changelog.append(f"    **Last Generated**: {datetime.datetime.now().strftime('%B %d, %Y at %I:%M %p')}\n")
    
    # Section 1: Releases
    if tags:
        changelog.append("## 📦 Releases\n")
        
        sorted_tags = sorted(tags.items(), key=lambda x: x[1], reverse=True)
        
        for i, (tag, tag_date) in enumerate(sorted_tags):
            changelog.append(f"### {tag} - {tag_date}\n")
            
            # Get commits for this release
            if i < len(sorted_tags) - 1:
                prev_tag = sorted_tags[i + 1][0]
                release_commits = get_commits_between_tags(tag, prev_tag)
            else:
                # First release - all commits up to tag
                release_commits = get_commits_between_tags(tag)
            
            # Categorize commits
            categorized = {}
            for commit in release_commits:
                if not commit:
                    continue
                parts = commit.split('|')
                if len(parts) >= 2:
                    message = parts[1].strip()
                    category, clean_msg = categorize_commit(message)
                    if category not in categorized:
                        categorized[category] = []
                    categorized[category].append(clean_msg)
            
            # Output by category
            for category in ['✨ New Features', '🔨 Improvements', '🐛 Bug Fixes', 
                           '📚 Documentation', '💎 Style & Formatting', '♻️ Code Refactoring', 
                           '📝 Other Changes']:
                if category in categorized:
                    changelog.append(f"\n**{category}**\n")
                    for msg in categorized[category]:
                        changelog.append(f"- {msg}")
            
            changelog.append("\n")
    
    # Section 2: Unreleased Changes
    changelog.append("## 🚧 Unreleased Changes\n")
    changelog.append("*Changes since the last release:*\n")
    
    if tags:
        latest_tag = sorted(tags.items(), key=lambda x: x[1], reverse=True)[0][0]
        unreleased = get_commits_between_tags(latest_tag)
    else:
        unreleased = commits
    
    # Group unreleased by category
    categorized_unreleased = {}
    for commit in unreleased:
        if not commit:
            continue
        parts = commit.split('|')
        if len(parts) >= 2:
            message = parts[1].strip()
            category, clean_msg = categorize_commit(message)
            if category not in categorized_unreleased:
                categorized_unreleased[category] = []
            categorized_unreleased[category].append(clean_msg)
    
    if categorized_unreleased:
        for category in ['✨ New Features', '🔨 Improvements', '🐛 Bug Fixes', 
                       '📚 Documentation', '💎 Style & Formatting', '♻️ Code Refactoring', 
                       '📝 Other Changes']:
            if category in categorized_unreleased:
                changelog.append(f"\n**{category}**\n")
                for msg in categorized_unreleased[category]:
                    changelog.append(f"- {msg}")
    else:
        changelog.append("*No unreleased changes*\n")
    
    # Section 3: Chronological History
    changelog.append("\n---\n")
    changelog.append("## 📅 Chronological History\n")
    changelog.append("*All changes grouped by date:*\n")
    
    # Group commits by date
    by_date = {}
    for commit in commits:
        if not commit:
            continue
        parts = commit.split('|')
        if len(parts) >= 2:
            date = parts[0]
            message = parts[1].strip()
            if date not in by_date:
                by_date[date] = []
            by_date[date].append(message)
    
    for date in sorted(by_date.keys(), reverse=True)[:30]:  # Last 30 days
        changelog.append(f"\n### {date}\n")
        for message in by_date[date]:
            changelog.append(f"- {message}")
    
    return '\n'.join(changelog)

if __name__ == '__main__':
    changelog = generate_changelog()
    
    # Write to docs folder
    output_path = Path('docs/resources/changelog.md')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(changelog)
    
    print(f"✓ Changelog generated: {output_path}")
    releases = changelog.count('### v') + changelog.count('### 1.') + changelog.count('### 2.')
    print(f"  Releases documented: {releases}")
    print(f"  Unreleased changes: {changelog.count('Unreleased Changes')}")
