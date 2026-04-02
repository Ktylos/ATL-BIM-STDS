/**
 * Version-aware banner for ATL BIM Standards
 * Reads the current version from the URL path and injects a contextual
 * notice at the top of every content page.
 */

document$.subscribe(function () {
    // Remove any existing banner (handles MkDocs instant navigation re-renders)
    const existing = document.querySelector('.version-banner');
    if (existing) existing.remove();

    // Only inject on content pages
    const article = document.querySelector('article.md-content__inner');
    if (!article) return;

    // Extract version from URL path — Mike deploys to /VERSION/...
    const match = window.location.pathname.match(/^\/([^\/]+)\//);
    if (!match) return;

    const version = match[1];
    const banner = document.createElement('div');
    banner.className = 'admonition version-banner';

    if (version === 'latest') {
        banner.classList.add('info');
        banner.innerHTML = `
            <p class="admonition-title">You are viewing the Latest version of these Standards</p>
            <p>This version reflects the most recent updates to the ATL BIM Standards and may include
            changes not yet incorporated into an official numbered release. If your contract references
            a specific version, use the <strong>version selector</strong> at the top of the page to
            navigate to that version.
            <a href="/latest/resources/support/">Learn more about our GitDocs workflow.</a></p>`;
    } else {
        banner.classList.add('note');
        banner.innerHTML = `
            <p class="admonition-title">You are viewing Version ${version} of these Standards</p>
            <p>This is a archived snapshot of the ATL BIM Standards as published for Version ${version}.
            Newer versions may be available. Use the <strong>version selector</strong> at the top of
            the page to view the latest release or other versions.
            <a href="/latest/resources/support/">Learn more about our GitDocs workflow.</a></p>`;
    }

    article.prepend(banner);
});
