from odoo import models, fields


class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'

    branch_name = fields.Char(string='Şube Adı')
    branch_code = fields.Char(string='Şube Kodu')
    swift = fields.Char(string='SWIFT / BIC')
    iban = fields.Char(string='IBAN')
