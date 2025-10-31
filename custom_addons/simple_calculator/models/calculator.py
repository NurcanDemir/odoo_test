# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SimpleCalculator(models.Model):
    _name = 'simple.calculator'
    _description = 'Simple Calculator'

    # Input fields
    num1 = fields.Float(string='First Number', default=0.0)
    num2 = fields.Float(string='Second Number', default=0.0)
    
    # Output fields
    result = fields.Float(string='Result', readonly=True, default=0.0)
    operation_text = fields.Char(string='Operation', readonly=True)
    
    # Currency info
    usd_rate = fields.Float(string='USD/TRY', default=34.50, readonly=True)
    eur_rate = fields.Float(string='EUR/TRY', default=37.80, readonly=True)
    gbp_rate = fields.Float(string='GBP/TRY', default=44.20, readonly=True)

    def button_add(self):
        """Addition operation"""
        for record in self:
            record.result = record.num1 + record.num2
            record.operation_text = f"{record.num1} + {record.num2} = {record.result}"
        return True

    def button_subtract(self):
        """Subtraction operation"""
        for record in self:
            record.result = record.num1 - record.num2
            record.operation_text = f"{record.num1} - {record.num2} = {record.result}"
        return True

    def button_multiply(self):
        """Multiplication operation"""
        for record in self:
            record.result = record.num1 * record.num2
            record.operation_text = f"{record.num1} × {record.num2} = {record.result}"
        return True

    def button_divide(self):
        """Division operation"""
        for record in self:
            if record.num2 == 0:
                raise UserError(_('Cannot divide by zero!'))
            record.result = record.num1 / record.num2
            record.operation_text = f"{record.num1} ÷ {record.num2} = {record.result}"
        return True

    def button_clear(self):
        """Clear all fields"""
        for record in self:
            record.num1 = 0.0
            record.num2 = 0.0
            record.result = 0.0
            record.operation_text = ""
        return True