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
            'date': 'January 2026',
            'description': 'Comprehensive file naming conventions and project organization standards.',
            'pdf': 'ATL-STD-XX-DC-GN-001.pdf',
            'url': 'standards/dc-gn-001/'
        },
        'GN-002': {
            'title': 'BIM Modeling Best Practices',
            'code': 'ATL-STD-XX-DC-GN-002',
            'version': '1.0',
            'date': 'January 2026',
            'description': 'Best practices for creating accurate, coordinated, and efficient BIM models.',
            'pdf': 'ATL-STD-XX-DC-GN-002.pdf',
            'url': 'standards/dc-gn-002/'
        },
        'GN-003': {
            'title': 'Coordination and Collaboration Workflows',
            'code': 'ATL-STD-XX-DC-GN-003',
            'version': '1.0',
            'date': 'January 2026',
            'description': 'Workflows and procedures for multi-discipline coordination.',
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
            'url': 'templates/tp-gn-001/'
        },
        'TP-GN-002': {
            'title': 'Coordination Tracker',
            'code': 'ATL-STD-XX-TP-GN-002',
            'version': '2.0',
            'file': 'ATL-STD-XX-TP-GN-002.xlsx',
            'description': 'Excel template for coordination tracking.',
            'url': 'templates/tp-gn-002/'
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
