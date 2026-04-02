/**
 * Version-aware banner and document info box for ATL BIM Standards.
 * Reads the current version from the URL path (set by Mike) and:
 *   1. Injects a contextual notice banner at the top of every content page
 *   2. Updates the "Version" field in the Document Information admonition box
 */

document$.subscribe(function () {
    // Remove any existing banner (handles MkDocs instant navigation re-renders)
    const existing = document.querySelector('.version-banner');
    if (existing) existing.remove();

    // Extract version from URL path — Mike deploys to /VERSION/...
    const match = window.location.pathname.match(/^\/([^\/]+)\//);
    if (!match) return;

    const version = match[1];

    // ── 1. VERSION BANNER ────────────────────────────────────────────────────

    const article = document.querySelector('article.md-content__inner');
    if (article) {
        const banner = document.createElement('div');
        banner.className = 'admonition version-banner';

        if (version === 'latest') {
            banner.classList.add('info');
            banner.innerHTML = `
                <p class="admonition-title">You are viewing the Latest version of these Standards</p>
                <p>This version reflects the most recent updates and may include changes not yet
                incorporated into an official numbered release. If your contract references a specific
                version, use the <strong>version selector</strong> at the top of the page to navigate
                to that version.
                <a href="/latest/resources/support/">Learn more about our GitDocs workflow.</a></p>`;
        } else {
            banner.classList.add('note');
            banner.innerHTML = `
                <p class="admonition-title">You are viewing Version ${version} of these Standards</p>
                <p>This is a frozen snapshot of the ATL BIM Standards as published for Version ${version}.
                Newer versions may be available. Use the <strong>version selector</strong> at the top
                of the page to view the latest release or other versions.
                <a href="/latest/resources/support/">Learn more about our GitDocs workflow.</a></p>`;
        }

        article.prepend(banner);
    }

    // ── 2. DOCUMENT INFORMATION BOX VERSION FIELD ────────────────────────────
    // Finds the "Version: x.x" line inside any admonition on the page and
    // updates it to reflect the URL version. Only updates if the element
    // contains a version number pattern (avoids touching other bold fields).

    const infoBoxes = document.querySelectorAll('.md-typeset .admonition');
    infoBoxes.forEach(function (box) {
        const strongs = box.querySelectorAll('strong');
        strongs.forEach(function (el) {
            if (el.textContent.trim() === 'Version') {
                const textNode = el.nextSibling;
                if (textNode && textNode.nodeType === Node.TEXT_NODE) {
                    if (version === 'latest') {
                        textNode.textContent = ': Latest';
                    } else {
                        textNode.textContent = ': ' + version;
                    }
                }
            }
        });
    });
});
