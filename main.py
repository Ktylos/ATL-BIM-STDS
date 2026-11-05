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
            'url': 'standards/dc-gn-001/'
        },
        'GN-002': {
            'title': 'BIM Modeling Best Practices',
            'code': 'ATL-STD-XX-DC-GN-002',
            'version': '1.0',
            'date': 'February 2026',
            'description': 'Best practices for creating accurate, coordinated, and efficient BIM models.',
            'url': 'standards/dc-gn-002/'
        },
        'GN-004': {
            'title': 'Revit SOP',
            'code': 'ATL-STD-XX-DC-GN-004',
            'version': '1.0',
            'date': 'March 2026',
            'description': 'Standard operating procedure for Revit project setup, modeling, coordination, and deliverables.',
            'url': 'standards/dc-gn-004/'
        },
        'GN-005': {
            'title': 'Civil 3D SOP',
            'code': 'ATL-STD-XX-DC-GN-005',
            'version': '0.1',
            'date': 'November 2026',
            'description': 'Standard operating procedure for Civil 3D and AutoCAD setup, modeling, plan production, and deliverables per the ATL CAD Standards.',
            'url': 'standards/dc-gn-005/'
        }
    }

    # Templates
    env.variables['templates'] = {
        'TP-GN-001': {
            'title': 'BIM Execution Plan Template',
            'code': 'ATL-STD-XX-TP-GN-001',
            'version': '2.0',
            'description': 'BIM Execution Plan template.',
            'url': 'template-docs/tp-gn-001/'
        },
        'TP-GN-002': {
            'title': 'Coordination Tracker',
            'code': 'ATL-STD-XX-TP-GN-002',
            'version': '2.0',
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
