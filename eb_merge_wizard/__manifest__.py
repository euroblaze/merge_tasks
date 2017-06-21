# -*- coding: utf-8 -*-
{
    'name': "Merge Tasks",

    'summary': """
        The merge_tasks_wizard module merges multiple tasks into one,
                """,
    'description': """
        Merging multiple tasks into one is now possible with this module.
        Go to Project --> Tasks (list view) and select multiple tasks, in the action button
        there will be Merge Tasks option. The wizard will open and place your settings there.

   """,

    'website': 'www.euroblaze.de',
     'author': 'odoo@simplify-erp.com',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project, Tasks',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','project','hr_timesheet'],
    'images': ['static/description/banner.jpg'],
    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
