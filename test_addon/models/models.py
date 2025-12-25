# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import UserError


class test_addon(models.Model):
    _name = 'test_addon.test_addon'
    _description = 'test_addon.test_addon'
    _inherit = ['portal.mixin', 'mail.thread.cc', 'mail.activity.mixin']


    name = fields.Char(string="Number Of Batch" , required=True)
    invoice_ids = fields.Many2many(
        'account.move',
        string='Bulk Draft invoices',
        domain="[('state','=','draft')]"
    )

    def action_post_invoices(self):
        if not self.invoice_ids:
            raise UserError("لا يوجد فواتير في حالة المسودة")

        for invoice in self.invoice_ids:
            invoice.action_post()



