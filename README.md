# ATL BIM Standards

> **Live site:** [bim.atlstandards.com](https://bim.atlstandards.com)

This repository contains the source for the Hartsfield-Jackson Atlanta International Airport BIM Standards documentation site. Standards are published as a versioned web reference for all consultants engaged on ATL Planning & Development projects.

This is a **public repository**. Consultants may file feedback and amendment proposals using GitHub Issues.

---

## Versioned Documentation

Standards are versioned using [Mike](https://github.com/jimporter/mike). Each release is tagged and deployed independently, so consultants can always access the exact version of the standards referenced in their contract.

**How to access a specific version:**

1. Visit [bim.atlstandards.com](https://bim.atlstandards.com)
2. Use the version selector in the top navigation bar to choose your version (e.g., `1.0`, `1.1`)
3. The `latest` alias always points to the most recently released version

If your contract references a specific version (e.g., "ATL BIM Standards v1.0, March 2026"), select that version from the dropdown to view the standards exactly as they were when your contract was issued.

---

## Filing Feedback

Consultants and project teams may file structured feedback via GitHub Issues:

**[Open a new issue](https://github.com/Ktylos/ATL-BIM-STDS/issues/new/choose)**

Three issue types are available:

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
mkdocs serve
# Opens at http://localhost:8000

# Test versioning locally
mike deploy 1.0 --config-file mkdocs.yml
mike serve
# Opens versioned preview at http://localhost:8000

# Build static site (sanity check before tagging)
mkdocs build
```

Always run `mkdocs build` before opening a PR to catch configuration errors.

---

## For BIM Team: Releasing a New Version

1. **Edit on `develop`** — make all content changes on the `develop` branch
2. **Test locally** — run `mkdocs serve` and review all affected pages
3. **Open a PR** — `develop` → `main`, review changes, merge when approved
4. **Tag the release** on `main`:

   ```bash
   git checkout main
   git pull
   git tag v1.1
   git push origin v1.1
   ```

5. **CI deploys automatically** — GitHub Actions runs Mike to version the build and FTP-deploys to `bim.atlstandards.com`

**Do not push directly to `main`.** All changes go through PRs from `develop`.

---

## Tech Stack

| Component | Technology |
| --- | --- |
| Site generator | [MkDocs](https://www.mkdocs.org/) with [Material theme](https://squidfunk.github.io/mkdocs-material/) |
| Versioning | [Mike](https://github.com/jimporter/mike) |
| Reusable content | [mkdocs-macros-plugin](https://mkdocs-macros-plugin.readthedocs.io/) |
| Deployment | FTP via GitHub Actions ([SamKirkland/FTP-Deploy-Action](https://github.com/SamKirkland/FTP-Deploy-Action)) |
| Hosting | `bim.atlstandards.com` |
