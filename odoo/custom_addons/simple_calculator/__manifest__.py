# -*- coding: utf-8 -*-
{
    'name': 'ALLDENIMS Hesap Makinesi',
    'version': '18.0.1.0.0',
    'category': 'Tools',
    'summary': 'ALLDENIMS Basic Calculator for Odoo 18',
    'description': """
        Simple Calculator Module
        ========================
        
        Basic calculator with:
        * Two number inputs
        * Four basic operations (+, -, ×, ÷)
        * Clear function
        * Result display
        * Currency rates display
        
        Clean and simple implementation for Odoo 18.
    """,
    'author': 'ALLDENIMS',
    'website': 'https://www.alldenims.com',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/calculator_views.xml',
        'views/calculator_menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}