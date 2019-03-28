# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Auto Install Modules',
    'version' : '1.0',
    'author':'Emipro Technologies',
    'category': 'Sales',
    'maintainer': 'Emipro Technologies',
    'description': """

        When you install this module it can directly install sale,purchase,accounting,Inventory modules.

    """,
    'summary': """Enable Auto Install modules like Sales Purchase and accounting Inventory """,

    'website': 'https://www.emiprotechnologies.com.com/',
    'license': 'LGPL-3',
    'support':'info@emirotechnologies.com',
    'depends' : ['sale_management'],
    'data': [
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,
}
