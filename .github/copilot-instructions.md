# ATL BIM Standards Documentation - Copilot Instructions

## Project Overview

This is a **MkDocs-based documentation site** for BIM (Building Information Modeling) standards currently focused on **staging deployment** for internal review via GitHub Pages, with production deployment planned for future. The site is built with MkDocs Material theme and uses a custom macro system for reusable content.

**Key Architecture:**
- **Content**: Markdown files in `docs/` (originally converted from Word documents)
- **Configuration**: `mkdocs.yml` for site structure and theme
- **Reusable Content**: Centralized in `main.py` using mkdocs-macros-plugin
- **Native Assets**: `Source/` folder contains native files (.RTE, .docx, etc.) for release packaging - **DO NOT MODIFY**
- **Deployment**: Currently GitHub Pages staging; production workflow planned for future

## Critical Workflows

### Local Development
```powershell
# Activate virtual environment (if using)
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Preview site locally
mkdocs serve  # Opens at http://localhost:8000

# Build static site
mkdocs build  # Outputs to site/
```

### Deployment Flow (Current Focus: Staging)
1. **Feature Branch** → PR → **Main Branch** → Auto-deploys to **Staging** (GitHub Pages)
2. PRs trigger preview builds via `pr-preview.yml` workflow
3. **Production workflow** (planned): Main → Production Branch → External deployment (not yet implemented)

**Important**: 
- Never commit the `site/` directory - it's build output (excluded in .gitignore)
- Never modify files in `Source/` folder - these are native assets for release packaging

## Project-Specific Conventions

### Reusable Content System (Key Pattern!)

**All content definitions live in `main.py`** - this is the single source of truth for:
- Standards metadata (GN-001, GN-002, GN-003, etc.)
- Template definitions (TP-GN-001, TP-GN-002)
- Family library information
- GitHub URLs (auto-adapts between enterprise/public repos)
- Release information

**When editing content:**
1. ✅ Update `main.py` - changes propagate to ALL pages
2. ❌ Don't edit content inline in Markdown files
3. Use macros in Markdown: `{{ standards_table() }}`, `{{ standard_card('GN-001') }}`, `{{ standards['GN-001'].title }}`

**Example pattern:**
```python
# main.py
env.variables['standards'] = {
    'GN-001': {
        'title': 'File Naming and Organization',
        'version': '1.0',  # ← Update here, not in individual pages
        'date': 'January 2026',
        'pdf': 'ATL-STD-XX-DC-GN-001.pdf'
    }
}
```

See [REUSABLE-CONTENT-GUIDE.md](../REUSABLE-CONTENT-GUIDE.md) for complete macro reference.

### Document Naming Convention

Standards follow **3-part prefix format**: `ATL-STD-XX-{DC|TP}-{CATEGORY}-{NUMBER}`
- **DC**: Document (standards)
- **TP**: Template
- **GN**: General category
- Examples: `DC-GN-001`, `TP-GN-001`

Markdown files use shortened na (Rarely Used)

`convert_word_to_md.py` was used for initial document conversion and is **rarely needed** going forward:
```powershell
python convert_word_to_md.py
```

**What it does:**
- Extracts images to `docs/assets/images/` with descriptive names (`{doc}-image-{num}.{ext}`)
- Converts Word content to Markdown with proper image paths
- Removes HTML TOC anchor links (MkDocs auto-generates navigation)

**Note**: This script may be moved out of the workspace in the future. For new content, edit Markdown directly in `docs/`

**Add new documents** by updating `DOC_MAPPINGS` in the script before converting.

### GitHub Actions Workflows

Located in `.github/workflows/`:
- **`deploy-staging.yml`**: Auto-deploys to GitHub Pages on push to `main` - adds staging banner
- **`deploy-production.yml`***[ACTIVE]** Auto-deploys to GitHub Pages on push to `main` - adds staging banner
- **`pr-preview.yml`**: **[ACTIVE]** Builds preview for pull requests
- **`pr-check.yml`**: **[ACTIVE]** Validates build on PRs before merge
- **`deploy-production.yml`**: **[PLANNED]** Future production deployment (not yet implemented)
- **`deploy.yml`**: Legacy workflow (may be unused)

**Python version**: 3.11 (specified in all workflows
### MkDocs Configuration Patterns

**Environment-aware GitHub URLs** (`mkdocs.yml`):
```yaml
extra:
  github:
    enterprise_repo: https://github.com/EMU-WSP-Internal-Repos/...
    public_repo: https://github.com/YOUR-USERNAME/...
    environment: enterprise  # 'enterprise' for staging, 'public' for production
```

The `main.py` macros system reads this to serve correct GitHub links (issues, discussions, releases).

**Navigation structure** is defined in `mkdocs.yml` under `nav:` - update here when adding pages.

## Integration Points

### External Dependencies (requirements.txt)
- `mkdocs>=1.5.0` + `mkdocs-material>=9.5.0`: Core site generation
- `mkdocs-macros-plugin`: Powers reusable content system
- `mkdocs-git-revision-date-localized-plugin`: Shows last-updated timestamps
- `pymdown-extensions`: Enables admonitions, tabs, diagrams (Mermaid)

### Custom Assets
- **CSS**: `docs/stylesheets/extra.css` for theme customization
- **JavaScript**: `docs/javascripts/mathjax.js` for math equations (KaTeX/MathJax support)

## Documentation Structure

```
docs/
├── index.md                    # Home page (uses macros)
├── standards/                  # BIM standards (DC-GN-XXX)
│   ├── dc-gn-001.md           # File naming & organization
│   ├── dc-gn-002.md           # Modeling best practices
│   └── dc-gn-003.md           # Coordination workflows
├── templates/                  # Template documentation (TP-GN-XXX)
├── resources/                  # FAQs, support, downloads
├── contributing/               # How to contribute
└── assets/images/             # Extracted images from Word docs
```

## Common Tasks

Source/                         # Native format files - DO NOT MODIFY
├── *.docx                     # Original Word documents
├── *.RTE                      # Revit template files
└── *.xlsx                     # Excel templates
                               # Used for release packaging only

### Adding a New Standard
1. Update `main.py` → add to `standards` dictionary
2. Create `docs/standards/dc-gn-XXX.md` (or convert from Word)
3. Update `mkdocs.yml` navigation
4. Test locally: `mkdocs serve`
5. Commit and push to trigger staging deployment

### Updating Standard Metadata
Edit `main.py` only - changes cascade automatically to all pages using macros.

### Testing Before Deployment
Always run `mkdocs build` to catch configuration errors before pushing. Workflows use `mkdocs build` (not `mkdocs build --strict`) to allow warnings.

### Troubleshooting Build Errors
- Check `mkdocs.yml` syntax (YAML is whitespace-sensitive)
- Verify all referenced files in `nav:` exist
- Ensure image paths in Markdown use relative paths: `../assets/images/filename.ext`
- Check macro syntax: `{{ variable }}` or `{{ function() }}`

## W`Source/` folder**: Contains native format files for release packaging - never modify
- **Plugin configurations** in `mkdocs.yml`: Material theme features are tightly coupled
- **Workflow Python version**: 3.11 is tested and stable across all workflows
- **Base template structure**: MkDocs Material conventions (don't fight the framework)
- **`azure-pipelines.yml`**: Deprecated Azure Static Web Apps deployment (no longer used
- **Plugin configurations** in `mkdocs.yml`: Material theme features are tightly coupled
- **Workflow Python version**: 3.11 is tested and stable across all pipelines
- **Base template structure**: MkDocs Material conventions (don't fight the framework)

## Documentation References

- [DEPLOYMENT.md](../DEPLOYMENT.md): Complete deployment guide
- [REUSABLE-CONTENT-GUIDE.md](../REUSABLE-CONTENT-GUIDE.md): Macro system reference
- [GETTING-STARTED.md](../GETTING-STARTED.md): Quick start for new contributors
- [MACROS-EXAMPLES.md](../MACROS-EXAMPLES.md): Live examples of macro usage
