/**
 * ATL BIM Standards — Navigation Enhancements
 *
 * 1. Hover dropdowns on the top navigation tabs
 * 2. External links (non-atlstandards.com) open in a new tab
 */

document$.subscribe(function () {
  buildTabDropdowns();
  openExternalLinksInNewTab();
});

// ---------------------------------------------------------------------------
// 1. Tab Dropdowns
// ---------------------------------------------------------------------------
// Reads child links from the full primary-nav DOM (which Material always
// renders even when only the active section is visible in the sidebar)
// and attaches a hover dropdown to each top-tab that has more than one child.

function buildTabDropdowns() {
  var tabsList = document.querySelector('.md-tabs__list');
  if (!tabsList) return;

  // Clean up any dropdowns injected on a previous call
  tabsList.querySelectorAll('.md-tabs__dropdown').forEach(function (d) { d.remove(); });
  tabsList.querySelectorAll('.md-tabs__item--has-dropdown').forEach(function (i) {
    i.classList.remove('md-tabs__item--has-dropdown');
  });

  // The primary nav (data-md-level="0") contains ALL sections in the DOM
  // even when navigation.tabs hides non-active sections from the sidebar.
  var primaryNavList = document.querySelector('.md-nav[data-md-level="0"] > .md-nav__list');
  if (!primaryNavList) return;

  // Build map: section aria-label → [{text, href}]
  var sectionMap = {};
  primaryNavList.querySelectorAll(':scope > .md-nav__item').forEach(function (item) {
    var childNav = item.querySelector(':scope > .md-nav[aria-label]');
    if (!childNav) return;
    var label = childNav.getAttribute('aria-label');
    var links = [];
    childNav.querySelectorAll(':scope > .md-nav__list > .md-nav__item > a.md-nav__link').forEach(function (a) {
      var ellipsis = a.querySelector('.md-ellipsis');
      var text = (ellipsis ? ellipsis : a).textContent.trim();
      var href = a.getAttribute('href');
      if (text && href) links.push({ text: text, href: href });
    });
    if (label && links.length > 1) sectionMap[label] = links;
  });

  // Attach a dropdown <ul> to each matching tab item
  tabsList.querySelectorAll('.md-tabs__item').forEach(function (tabItem) {
    var tabLink = tabItem.querySelector('.md-tabs__link');
    if (!tabLink) return;
    var tabName = tabLink.textContent.trim();
    var children = sectionMap[tabName];
    if (!children) return;

    var dropdown = document.createElement('ul');
    dropdown.className = 'md-tabs__dropdown';
    children.forEach(function (child) {
      var li = document.createElement('li');
      var a = document.createElement('a');
      a.href = child.href;
      a.textContent = child.text;
      li.appendChild(a);
      dropdown.appendChild(li);
    });

    tabItem.appendChild(dropdown);
    tabItem.classList.add('md-tabs__item--has-dropdown');
  });
}

// ---------------------------------------------------------------------------
// 2. External links → new tab
// ---------------------------------------------------------------------------
// Targets only links inside the main content area (.md-typeset), so in-site
// navigation (sidebar, tabs, footer) is never affected.

function openExternalLinksInNewTab() {
  document.querySelectorAll('.md-typeset a[href]').forEach(function (link) {
    var href = link.href; // fully resolved absolute URL
    if (!href || !href.includes('://')) return;
    if (href.includes('atlstandards.com')) return;
    link.setAttribute('target', '_blank');
    link.setAttribute('rel', 'noopener noreferrer');
  });
}
