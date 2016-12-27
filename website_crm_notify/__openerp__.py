# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Website CRM Notification',
    'category': 'Website',
    'version': '9.0.1.1.0',
    'author': 'Rooms For (Hong Kong) Limited T/A OSCG',
    'website': 'https://www.odoo-asia.com/',
    'licence': 'AGPL-3',
    'depends': ['website_crm'],
    'summary':"""Send notification and reminder when submit contact form""",
    'description': """
Send notification and reminder when submit contact form
    """,
    'data': [
        'data/website_crm_notify_data.xml',
    ],
    'installable': True,
    'applitcation': False,
}
