# -*- coding: utf-8 -*-
{
    'name': 'ALL DENIMS Bank Extension',
    'version': '18.0.1.0.0',
    'summary': 'Extend bank account with branch, IBAN and SWIFT fields',
    'description': 'Adds branch name/code, SWIFT/BIC and IBAN to res.partner.bank and updates partner views.',
    'category': 'Accounting',
    'author': 'ALL DENIMS',
    'license': 'LGPL-3',
    'depends': ['base', 'contacts'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
}
