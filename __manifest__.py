{
    'name': 'Library',
    'version': '1.0',
    'summary': 'Manage books in a library',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
    ],
    'installable': True,
    'application': True,
}
