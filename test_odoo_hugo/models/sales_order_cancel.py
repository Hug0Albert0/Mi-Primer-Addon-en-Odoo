# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SalesOrderCancel(models.Model):
    _inherit = "sale.order"

    @api.multi
    def action_cancel(self):
        print "CAPACITACION ODOO"
        super(SalesOrderCancel,self).action_cancel()