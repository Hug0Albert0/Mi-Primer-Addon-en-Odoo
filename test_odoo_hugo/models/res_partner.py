# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = "res.partner"
    descripcion = fields.Char(string = "Descripcion detallada")
    verificado = fields.Boolean(string = "Verificado?")
    notify_email = fields.Selection([
        ("none", "Nunca nunca"),
        ("always","Todos todos")],
        default = "none"
    )