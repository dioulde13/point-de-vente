# -*- coding: utf-8 -*-
{
    'name': "Weblearns Points Of Sale",
    'summary': "Short (1 phrase/line) summary of the module's purpose, used as subtitle on modules listing or apps.openerp.com",
    'description': "Long description of module's purpose",
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'web', 'point_of_sale'],
    'qweb': ['static/src/view/action_button.xml'],
    'data': [
        "views/view.xml",
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
