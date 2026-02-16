'''
MkDocs Macros - Reusable content definitions
'''

def define_env(env):
    # Standards definitions
    env.variables['standards'] = {
        'GN-001': {
            'title': 'File Naming and Organization',
            'code': 'ATL-STD-XX-DC-GN-001',
            'version': '1.0',
            'date': 'February 2026',
            'description': 'Comprehensive file naming conventions and project organization standards.',
            'pdf': 'ATL-STD-XX-DC-GN-001.pdf',
            'url': 'standards/dc-gn-001/'
        },
        'GN-002': {
            'title': 'BIM Modeling Best Practices',
            'code': 'ATL-STD-XX-DC-GN-002',
            'version': '1.0',
            'date': 'February 2026',
            'description': 'Best practices for creating accurate, coordinated, and efficient BIM models.',
            'pdf': 'ATL-STD-XX-DC-GN-002.pdf',
            'url': 'standards/dc-gn-002/'
        },
        'GN-003': {
            'title': 'Revit Project Setup with Custom Coordinates',
            'code': 'ATL-STD-XX-DC-GN-003',
            'version': '1.0',
            'date': 'February 2026',
            'description': 'Workflows and procedures for Revit project setup with custom coordinates.',
            'pdf': 'ATL-STD-XX-DC-GN-003.pdf',
            'url': 'standards/dc-gn-003/'
        }
    }
    
    # Templates
    env.variables['templates'] = {
        'TP-GN-001': {
            'title': 'BIM Execution Plan Template',
            'code': 'ATL-STD-XX-TP-GN-001',
            'version': '2.0',
            'file': 'ATL-STD-XX-TP-GN-001.docx',
            'description': 'BIM Execution Plan template.',
            'url': 'template-docs/tp-gn-001/'
        },
        'TP-GN-002': {
            'title': 'Coordination Tracker',
            'code': 'ATL-STD-XX-TP-GN-002',
            'version': '2.0',
            'file': 'ATL-STD-XX-TP-GN-002.xlsx',
            'description': 'Excel template for coordination tracking.',
            'url': 'template-docs/tp-gn-002/'
        }
    }
    
    # Contact
    env.variables['contact'] = {
        'email': 'bim-standards@atl.com',
        'phone': '+1 (555) 123-4567'
    }
    
    # Release info
    env.variables['release'] = {
        'current_version': '1.0',
        'release_date': 'February 2026'
    }
        
    @env.macro
    def download_button(file, text='Download'):
        return f'[{text}](/downloads/{file}){{ .md-button .md-button--primary }}'
    
    @env.macro
    def release_widget(version=None):
        """Generate latest release widget"""
        release = env.variables['release']
        
        display_version = version or release['current_version']
        download_file = f"ATL-BIM-Standards-v{display_version}.zip"
        
        return f"""
<div class="release-widget">
  <h3>📦 Latest Release</h3>
  <p><strong>Version {display_version}</strong> - {release['release_date']}</p>
  <p>
    <a href="/downloads/{download_file}" class="md-button md-button--primary" download>Download Complete Package</a>
  </p>
  <p><small>Download standards PDFs, templates, and libraries from the release package.</small></p>
</div>
"""
