# -*- coding: utf-8 -*-
from odoo import http

# class TestOdooHugo(http.Controller):
#     @http.route('/test_odoo_hugo/test_odoo_hugo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_odoo_hugo/test_odoo_hugo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_odoo_hugo.listing', {
#             'root': '/test_odoo_hugo/test_odoo_hugo',
#             'objects': http.request.env['test_odoo_hugo.test_odoo_hugo'].search([]),
#         })

#     @http.route('/test_odoo_hugo/test_odoo_hugo/objects/<model("test_odoo_hugo.test_odoo_hugo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_odoo_hugo.object', {
#             'object': obj
#         })