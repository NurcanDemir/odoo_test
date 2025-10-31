{
    'name': 'All Denims Bank Extension',
    'version': '18.0.1.0.0',
    'summary': 'Add branch details and IBAN/SWIFT to partner bank accounts',
    'category': 'Extra Tools',
    'author': 'Generated',
    'license': 'LGPL-3',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
}
