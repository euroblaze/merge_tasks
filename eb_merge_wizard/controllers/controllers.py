# -*- coding: utf-8 -*-
from odoo import http

# class /odoo/custom/addons/mergeTasksWizard(http.Controller):
#     @http.route('//odoo/custom/addons/merge_tasks_wizard//odoo/custom/addons/merge_tasks_wizard/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//odoo/custom/addons/merge_tasks_wizard//odoo/custom/addons/merge_tasks_wizard/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/odoo/custom/addons/merge_tasks_wizard.listing', {
#             'root': '//odoo/custom/addons/merge_tasks_wizard//odoo/custom/addons/merge_tasks_wizard',
#             'objects': http.request.env['/odoo/custom/addons/merge_tasks_wizard./odoo/custom/addons/merge_tasks_wizard'].search([]),
#         })

#     @http.route('//odoo/custom/addons/merge_tasks_wizard//odoo/custom/addons/merge_tasks_wizard/objects/<model("/odoo/custom/addons/merge_tasks_wizard./odoo/custom/addons/merge_tasks_wizard"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/odoo/custom/addons/merge_tasks_wizard.object', {
#             'object': obj
#         })