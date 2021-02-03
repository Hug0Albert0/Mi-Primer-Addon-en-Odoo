# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.addons import decimal_precision as dp

class TestTecnologies(models.Model):
    _name = "test_odoo_hugo.technologies"
    _description = "Tecnologias para Desarrolladores"
    _inherit = ['mail.thread', 'ir.needaction_mixin']

    name = fields.Char("Nombre de la Tecnologia", required = True)
    folio = fields.Char("Folio")
    description = fields.Text("Descripcion", required = True)
    is_active = fields.Boolean("¿Está activo?", default = True)
    users_number = fields.Integer("Número de Usuarios")
    version = fields.Float("Versión")
    estatus = fields.Selection([
        ("active", "Activo"),
        ("inactive","Inactivo")],
        default = "active",
        required = True
    )
    partner_id = fields.Many2one("res.partner")
    sale_ids = fields.Many2many("sale.order")
    total_sales = fields.Integer(compute = "count_sales")
    #ventas_ids = fields.One2many("sale.order", "partner_id")
    foto = fields.Binary("Foto")
    #archivo = fields.Binary("Archivo")
    date_field = fields.Date("Fecha")
    datetime_field = fields.Datetime("FechaHora")
    status = fields.Selection([('active', 'Activo'),('inactive','Inactivo')], default = "active", required = True)
    detail_id = fields.One2many("test_odoo_hugo.technologies.detail", "technology_id")
    value = fields.Integer()
    phone = fields.Char(related='partner_id.phone')
    total_money = fields.Integer()
    float_value=fields.Float(string="Valor 6 decimales", digits=dp.get_precision('Mi PD'))

    @api.model
    def create(self, vals):
        vals["folio"] = self.env["ir.sequence"].next_by_code("test_odoo_hugo.technologies")
        result =  super(TestTecnologies, self).create(vals)
        return result

    @api.depends("sale_ids")
    def count_sales(self):
        for req in self:
            if (len(req.sale_ids) > 0):
                req.total_sales = len(req.sale_ids)
            else:
                req.total_sales = 0
    @api.multi
    def tech_form_button(self):
        print type(self)
        print "HUGO ALBERTO RIVERA DIAZ"
        self.write({"version": 69.420})

    @api.multi
    def tech_form_button_2(self):
        for req in self:
            if req.partner_id:
                sales_ids = self.env['sale.order'].search([('partner_id', '=' ,req.partner_id.id)])
                req.value = len(sales_ids)
                for sale in sales_ids:
                    for value in sale.order_line:
                        print value.product_id.name
            else:
                raise UserError(_('Please, select a client before see the total sales.'))

    @api.multi
    def cancel_sales_from_client(self):
        for req in self:
            if req.partner_id:
                sales_ids = self.env['sale.order'].search([('partner_id', '=' ,req.partner_id.id)])
                for sale in sales_ids:
                    sale.action_cancel()
            else:
                raise UserError(_('Please, select a client before cancel the sales.'))


class TestTecnologiesDetail(models.Model):
    _name = 'test_odoo_hugo.technologies.detail'
    _description = "Technologies - Log details (fields updated)"

    name = fields.Char(required = True, string = "Nombre")
    description = fields.Text(required = True, string = "Descripcion")
    number = fields.Integer(string = "Numero")
    technology_id = fields.Many2one("test_odoo_hugo.technologies")