"""
MkDocs hook — injects a "1 Table of Contents" section at the top of every
standards and template page. The sidebar TOC is the actual table of contents;
this section preserves the numbered-section convention from the source documents.
"""

# Pages that should receive the injected TOC section
INCLUDE_PATHS = ("standards/", "template-docs/")

TOC_BLOCK = """## 1 Table of Contents

!!! note "Table of Contents"
    This document follows the numbered section convention of the ATL BIM Standards.
    The full table of contents for this page is available in the sidebar navigation.

---

"""


def on_page_markdown(markdown, *, page, config, files):
    if any(page.file.src_path.startswith(p) for p in INCLUDE_PATHS):
        # Don't inject on index pages (template-docs/index.md etc.)
        if page.file.name != "index":
            return TOC_BLOCK + markdown
    return markdown
