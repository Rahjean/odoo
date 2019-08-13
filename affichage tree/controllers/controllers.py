# -*- coding: utf-8 -*-
from odoo import http

# class X(http.Controller):
#     @http.route('/x/x/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/x/x/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('x.listing', {
#             'root': '/x/x',
#             'objects': http.request.env['x.x'].search([]),
#         })

#     @http.route('/x/x/objects/<model("x.x"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('x.object', {
#             'object': obj
#         })