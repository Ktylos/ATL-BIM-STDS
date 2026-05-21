# ATL BIM Standards

> **Live site:** [bim.atlstandards.com](https://bim.atlstandards.com)

This repository contains the source for the Hartsfield-Jackson Atlanta International Airport BIM Standards documentation site. Standards are published as a versioned web reference for all consultants engaged on ATL Planning & Development projects.

This is a **public repository**. Consultants may file feedback and amendment proposals using GitHub Issues.

---

## Versioned Documentation

Standards are versioned using [Mike](https://github.com/jimporter/mike). The site maintains two types of published content:

| Version | What it is | URL |
| --- | --- | --- |
| **Latest** | Rolling build — updated on every merge to `main`. May include layout, resource, or training updates not yet in an official release. | `bim.atlstandards.com/latest/` |
| **1.0, 1.1, etc.** | Frozen snapshot — published on a quarterly release tag. Content is permanently fixed at the time of tagging. | `bim.atlstandards.com/1.0/` |

**How to access a specific version:**

1. Visit [bim.atlstandards.com](https://bim.atlstandards.com)
2. Use the **version selector dropdown** in the top navigation bar
3. Select `Latest` for current content, or a numbered version (e.g. `1.0`) for the snapshot referenced in your contract

Every page displays a banner identifying which version you are viewing and whether it is a rolling or frozen release.

---

## Filing Feedback

Consultants and project teams may file structured feedback via GitHub Issues:

**[Open a new issue](https://github.com/Ktylos/ATL-BIM-STDS/issues/new/choose)**

| Issue Type | Use For |
| --- | --- |
| Standard Clarification | Questions about the intent or application of a standard |
| Standard Amendment Proposal | Suggesting a change or addition to a standard |
| Technical Error Report | Reporting a factual error or inconsistency in the published standards |

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidance on filing effective feedback.

---

## For BIM Team: Local Development

**Prerequisites:** Python 3.11+, pip

```bash
# Install dependencies
pip install -r requirements.txt

# Preview site locally
python -m mkdocs serve
# Opens at http://localhost:8000

# Build static site (sanity check before committing)
python -m mkdocs build
```

> **Note:** The version selector dropdown and version banners only appear on the deployed site, not in local preview. This is expected — Mike versioning requires a deployed environment.

---

## For BIM Team: Two Deployment Workflows

This repo uses two GitHub Actions workflows with different triggers:

### 1. Publish to Latest (on every push to `main`)

Any commit merged or pushed to `main` automatically triggers a rebuild of the **Latest** version. Use this for:
- Layout and style updates
- Resource page updates (support, changelog)
- Training or news content
- Any non-standards content that doesn't require a version snapshot

```bash
# After merging a PR or pushing directly to main:
git push origin main
# → publish-latest.yml triggers automatically
```

### 2. Release a Numbered Version (on version tag)

Standards content updates are released on a quarterly cycle as frozen, numbered snapshots. This requires a version tag:

```bash
git checkout main
git pull
git tag v1.1
git push origin v1.1
# → deploy.yml triggers automatically
```

Full release steps:
1. **Edit on `develop`** — all standards content changes go here
2. **Test locally** — `python -m mkdocs serve`
3. **Open a PR** — `develop` → `main`, review and merge
4. **Tag on `main`** — `git tag v1.1 && git push origin v1.1`
5. **CI deploys automatically** — Mike creates the numbered snapshot, FTP deploys

---

## Commit Convention (BIM Team)

Only commits prefixed `[CONTENT]` appear in the public changelog. Use this prefix for any commit that changes the *substance* of a standard — wording, requirements, tables, diagrams. Omit it for dev, CI, or formatting changes.

| Commit message | Shows in changelog? |
| --- | --- |
| `[CONTENT] Updated DC-GN-001 Section 3.2 MEP naming convention` | Yes |
| `[CONTENT] Added LOD requirements table to DC-GN-002 Section 7` | Yes |
| `Fix TOC hook position` | No |
| `Update glightbox plugin` | No |
| `Merge develop into main` | No |

---

## Tech Stack

| Component | Technology |
| --- | --- |
| Site generator | [MkDocs](https://www.mkdocs.org/) with [Material theme](https://squidfunk.github.io/mkdocs-material/) |
| Versioning | [Mike](https://github.com/jimporter/mike) |
| Reusable content | [mkdocs-macros-plugin](https://mkdocs-macros-plugin.readthedocs.io/) |
| Image lightbox | [mkdocs-glightbox](https://github.com/blueswen/mkdocs-glightbox) |
| Deployment | FTP via GitHub Actions ([SamKirkland/FTP-Deploy-Action](https://github.com/SamKirkland/FTP-Deploy-Action)) |
| Hosting | `bim.atlstandards.com` |
