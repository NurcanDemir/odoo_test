# all_denims_bank_extension

Odoo 18 module to extend `res.partner.bank` with branch name, branch code, IBAN and SWIFT/BIC.

Installation:

1. Copy the `all_denims_bank_extension` folder to your Odoo `addons` path (e.g. `odoo/custom_addons`).
2. Update apps list in Odoo, then install the module.

This module:

- Adds fields: `branch_name`, `branch_code`, `swift`, `iban` to `res.partner.bank`.
- Adjusts the partner form to show a customized bank tree inside the "Faturalama" tab.
- Adjusts the bank account form to show the new fields after `acc_number` and hide `send_money`.
