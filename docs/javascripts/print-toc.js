// Print-only Table of Contents generator for MkDocs Material
(function() {
  'use strict';
  
  function generatePrintTOC() {
    // Skip if TOC already exists
    if (document.getElementById('print-toc')) {
      return;
    }
    
    var content = document.querySelector('.md-content__inner');
    if (!content) return;
    
    // Select all headers with IDs, but be more permissive
    var headers = content.querySelectorAll('h2, h3, h4');
    var validHeaders = [];
    
    // Filter headers manually
    for (var i = 0; i < headers.length; i++) {
      var header = headers[i];
      // Skip if no ID or inside admonition
      if (header.id && !header.closest('.admonition')) {
        validHeaders.push(header);
      }
    }
    
    if (validHeaders.length === 0) return;
    
    // Create TOC container
    var printTocContainer = document.createElement('div');
    printTocContainer.className = 'print-only-toc';
    printTocContainer.id = 'print-toc';
    
    // Add heading
    var tocHeading = document.createElement('h2');
    tocHeading.textContent = 'Table of Contents';
    printTocContainer.appendChild(tocHeading);
    
    // Create list
    var tocList = document.createElement('ul');
    
    for (var i = 0; i < validHeaders.length; i++) {
      var header = validHeaders[i];
      var listItem = document.createElement('li');
      var text = header.textContent.replace(/¶|#/g, '').trim();
      listItem.textContent = text;
      
      // Add indentation
      if (header.tagName === 'H3') {
        listItem.style.paddingLeft = '1.5em';
      } else if (header.tagName === 'H4') {
        listItem.style.paddingLeft = '3em';
      }
      
      tocList.appendChild(listItem);
    }
    
    printTocContainer.appendChild(tocList);
    
    // Insert at the very beginning
    content.insertBefore(printTocContainer, content.firstChild);
  }
  
  // Run on page load with delay to ensure content is ready
  function init() {
    setTimeout(generatePrintTOC, 500);
  }
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
  
  // Handle MkDocs Material instant navigation
  if (typeof app !== 'undefined' && app.document$) {
    app.document$.subscribe(function() {
      setTimeout(generatePrintTOC, 500);
    });
  }
  
  // Optimize print button click handlers
  document.addEventListener('click', function(e) {
    if (e.target.classList.contains('print-button')) {
      e.preventDefault();
      // Small delay to prevent forced reflow
      setTimeout(function() {
        window.print();
      }, 50);
    }
  });
  
})();
