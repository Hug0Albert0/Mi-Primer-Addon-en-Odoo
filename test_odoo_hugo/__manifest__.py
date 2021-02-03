# -*- coding: utf-8 -*-
{
    'name': "test_odoo_hugo",

    'summary': """ Simple CRUD addon for my Systeg Odoo training""",

    'description': """
        — Creación de un addons (test_odoo)
        — Modelo básico(‘test.odoo’), 5 tipos de campos
        — Crear xml de la vista y menú
        — Menú ítem para llamar el modelo en “Ventas — Facturación”
        — Vista de Lista y Vista de Formulario
        — Vista de formulario crear un botón en la cabecera
    """,

    'author': "Hugo Alberto Rivera Diaz",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Systeg',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', "sale"],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/test_tech.xml',
        "views/secuencias.xml",
        "views/res_partner.xml",
        'views/cabecera_cliente.xml',
        "report/action_report.xml",
        "report/action_template.xml"
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}