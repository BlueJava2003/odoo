{
    'name': 'My Custom Module',
    'version': '1.0',
    'summary': 'Short description of the module',
    'author': 'Your Name',
    'depends': ['base'],  # Liệt kê các module phụ thuộc
    'data': [
        'views/my_model_view.xml',  # Đường dẫn đến file XML view
    ],
    'installable': True,
    'application': False,
}
