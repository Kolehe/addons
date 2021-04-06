# -*- coding: utf-8 -*-
from odoo import http

# class Deober(http.Controller):
#     @http.route('/deober/deober/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/deober/deober/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('deober.listing', {
#             'root': '/deober/deober',
#             'objects': http.request.env['deober.deober'].search([]),
#         })

#     @http.route('/deober/deober/objects/<model("deober.deober"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('deober.object', {
#             'object': obj
#         })