# -*- coding: utf-8 -*-

{
    'name': "Modificación manual del tipo de cambo para Sales Order/Customer Invoice/Vendor Bills/Purchase Orders/Payments",
    'version': "13.0.0.0",
    'summary': "This module will provide you the facility to enter exchange currency rate at the time of sales order, invoice order, purchase order and payments",
    'category': 'Accounting Management',
    'description': """
    manual currency exchange rate
        manual currency exchange rate on invoice 
        manual currency exchange rate on sales order
        manual currency exchange rate on Purchase order
        manual currency exchange rate on request for quotations
        manual currency exchange rate on quotations
        manual currency exchange rate on payments
        manual currency exchange rate on customer payments
        manual currency exchange rate on vendor payments
        manual currency exchange rate on supplier payments
        custom currency exchange rate
        override currency exchange rate
        foreign exchange
        profit and loss by exchange rate
        activate manual currency exchange rate
        invoice manual currency exchange rate
        sales order manual currency exchange rate
        vendor bills manual currency exchange rate
        customer invoice manual currency exchange rate
        payments manual currency exchange rate
        inherit sales order form
        inherit invoice order
        inherit customer invoice
        inherit vendor bills
        inherit customer payments
        inherit vendor bills payments
    """,
    'author': "Devman",
    'website':"http://www.devman.com.ar",
    'depends': ['base', 'sale_management', 'purchase', 'stock', 'account'],
    'data': [
        'views/inherited_invoice_payment.xml',
        'views/inherited_invoice.xml',
        'views/inherited_purchase_order.xml',
        'views/inherited_sale_order.xml'
    ],
    'demo': [],
    "external_dependencies": {},
    "license": "AGPL-3",
    'installable': True,
    'auto_install': False,
    'live_test_url':'',
    #'images': ['static/description/banner.png'],
    "price": 80,
    "currency": 'USD',
    
}
