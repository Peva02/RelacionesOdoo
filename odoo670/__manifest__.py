# -*- coding: utf-8 -*-
{
    'name': "odoo670",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/odoo670_security.xml',
        'security/ir.model.access.csv', 
        'views/views.xml',
        'views/views_clientes.xml',
        'views/views_empleados.xml',
        'views/templates.xml',
        'report/odoo670_coches670_report.xml',
        'report/odoo670_clientes670_report.xml',
        'report/odoo670_empleados670_report.xml'
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
