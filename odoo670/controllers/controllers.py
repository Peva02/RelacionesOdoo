# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo670(http.Controller):
#     @http.route('/odoo670/odoo670/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo670/odoo670/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo670.listing', {
#             'root': '/odoo670/odoo670',
#             'objects': http.request.env['odoo670.odoo670'].search([]),
#         })

#     @http.route('/odoo670/odoo670/objects/<model("odoo670.odoo670"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo670.object', {
#             'object': obj
#         })
