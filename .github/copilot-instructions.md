# ATL BIM Standards Documentation - Copilot Instructions

## Project Overview

This is a **MkDocs-based documentation site** for BIM (Building Information Modeling) standards at Hartsfield-Jackson Atlanta International Airport. The site is the sole authoritative source for ATL BIM standards — there are no Word document or PDF downloads. Versioning is managed with **Mike**, so consultants can access any historical version of the standards that was current at their project's contract date.

**Repo:** `https://github.com/Ktylos/ATL-BIM-STDS`
**Live site:** `https://bim.atlstandards.com`

**Key Architecture:**
- **Content**: Markdown files in `docs/`
- **Configuration**: `mkdocs.yml` for site structure and theme
- **Reusable Content**: Centralized in `main.py` using mkdocs-macros-plugin
- **Versioning**: Mike (`mike>=2.0.0`) manages versioned output on the `gh-pages` branch
- **Deployment**: FTP to `bim.atlstandards.com` via GitHub Actions, triggered on version tags only

## Branch Strategy

| Branch | Purpose |
|---|---|
| `develop` | Active development, edits, drafts — work here |
| `main` | Stable, release-ready content. Merge from `develop` via PR. Version tags created here. |
| `gh-pages` | Mike-managed versioned output — **never edit manually** |

## Release Workflow

1. Edit content on `develop`
2. Test locally: `mkdocs serve`
3. Open PR: `develop` → `main`, review, merge
4. Tag the release on `main`: `git tag v1.1 && git push origin v1.1`
5. GitHub Actions deploys automatically (Mike + FTP)

**Do not push directly to `main`.** Use PRs from `develop`.

## Local Development

```powershell
# Install dependencies (run once or after requirements changes)
pip install -r requirements.txt

# Preview site locally
mkdocs serve  # Opens at http://localhost:8000

# Test versioning locally
mike deploy 1.0 --config-file mkdocs.yml
mike serve    # Opens versioned preview at http://localhost:8000

# Build static site (sanity check before tagging)
mkdocs build
```

Always run `mkdocs build` before opening a PR to catch configuration errors. Workflows use `mkdocs build` (not `--strict`) to allow warnings.

## Project-Specific Conventions

### Reusable Content System

**All content definitions live in `main.py`** — single source of truth for:
- Standards metadata (GN-001, GN-002, GN-003, etc.)
- Template definitions (TP-GN-001, TP-GN-002)
- Contact information
- Release information

**When editing content:**
1. Update `main.py` — changes propagate to ALL pages that use macros
2. Do not edit content inline in Markdown files when a macro exists for it
3. Use macros in Markdown: `{{ standards_table() }}`, `{{ standard_card('GN-001') }}`, `{{ standards['GN-001'].title }}`

### Document Naming Convention

Standards follow **3-part prefix format**: `ATL-STD-XX-{DC|TP}-{CATEGORY}-{NUMBER}`
- **DC**: Document (standards)
- **TP**: Template
- **GN**: General category
- Examples: `DC-GN-001`, `TP-GN-001`

### Template Distribution

Templates (Revit `.rte`, Excel `.xlsx`, etc.) are **not distributed through this site**. They are provided directly to consultant teams at project scoping/kickoff by the ATL BIM Team. Do not add download links or file attachments to the site.

### No PDF Generation

Standards are web-only. Do not add PDF generation, export links, or references to PDF versions of any standard.

## GitHub Actions Workflow

**File:** `.github/workflows/deploy.yml`

- **Trigger:** Push of a version tag (`v1.0`, `v1.1`, `v2.0`, etc.) to `main`
- **Process:** Install deps → Generate changelog → Mike deploy version → FTP deploy `gh-pages` branch
- **Secrets required:** `FTP_USERNAME`, `FTP_PASSWORD` (configured in repo Settings → Secrets)
- **Git identity for Mike commits:** `ATL BIM Team <dev@ktylos.com>`

## MkDocs Configuration

**Version selector** (Mike) is configured in `mkdocs.yml`:
```yaml
extra:
  version:
    provider: mike
    default: latest
```

**Navigation structure** is defined in `mkdocs.yml` under `nav:` — update here when adding pages.

## Consultant Feedback

Consultants file feedback via **GitHub Issues** using structured templates:
- **Standard Clarification** — questions about intent or application
- **Standard Amendment Proposal** — suggested changes with justification
- **Technical Error Report** — factual errors in the published standards

Blank issues are disabled. Direct consultants to `github.com/Ktylos/ATL-BIM-STDS/issues/new/choose`.

## Integration Points

### External Dependencies (`requirements.txt`)
- `mkdocs>=1.5.0` + `mkdocs-material>=9.5.0`: Core site generation
- `mkdocs-macros-plugin`: Powers reusable content system
- `mkdocs-git-revision-date-localized-plugin`: Shows last-updated timestamps
- `pymdown-extensions`: Enables admonitions, tabs, diagrams (Mermaid)
- `mike>=2.0.0`: Versioned documentation deployment

### Custom Assets
- **CSS**: `docs/stylesheets/extra.css` for theme customization

## Documentation Structure

```
docs/
├── index.md                    # Home page (uses macros)
├── standards/                  # BIM standards (DC-GN-XXX)
│   ├── dc-gn-001.md
│   ├── dc-gn-002.md
│   └── dc-gn-003.md
├── template-docs/              # Template documentation (TP-GN-XXX)
│   ├── index.md
│   ├── tp-gn-001.md
│   └── tp-gn-002.md
├── resources/
│   ├── support.md
│   └── changelog.md            # Generated by generate_changelog.py
└── assets/images/              # Branding and content images
```

## Common Tasks

### Adding a New Standard
1. Update `main.py` → add to `standards` dictionary
2. Create `docs/standards/dc-gn-XXX.md`
3. Update `mkdocs.yml` navigation
4. Test locally: `mkdocs serve`
5. Commit to `develop`, open PR to `main`, tag when ready

### Updating Standard Metadata
Edit `main.py` only — changes cascade automatically to all pages using macros.

### Troubleshooting Build Errors
- Check `mkdocs.yml` syntax (YAML is whitespace-sensitive)
- Verify all referenced files in `nav:` exist
- Ensure image paths use relative paths: `../assets/images/filename.ext`
- Check macro syntax: `{{ variable }}` or `{{ function() }}`
