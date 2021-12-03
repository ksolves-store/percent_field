{
    'name': "Percent Field",

    'summary': """
        Percent Field v15.0""",

    'description': """
              Percent field for odoo 15.0. 
      """,
    'author': "Ksolves India Ltd.",
    'website': "https://www.ksolves.com/",
    'license': 'LGPL-3',
    'currency': 'EUR',
    'price': '0.0',
    'live_test_url': 'https://youtu.be/Guuyj7Gns00',
    'category': 'tools',
    'support': 'sales@ksolves.com',
    'version': '15.0.1.0.0',
    'images': [
        'static/description/main.jpg',
    ],
    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    "assets": {
        "web.assets_backend": [
            "ks_percent_field/static/src/js/basic_fields.js",
            "ks_percent_field/static/src/js/field_utils_format.js",
        ]
    }

}
# -*- coding: utf-8 -*-
