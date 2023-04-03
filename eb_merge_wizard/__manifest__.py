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
    'author': "Cona Cons (RISTE KABRANOV)",
    'website': "http://simplify-erp.com",
    'category': 'Project, Tasks',
    'version': '15.0.1.0.0',
    'depends': ['base', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
