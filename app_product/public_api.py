import os
import random
from flask import Blueprint

api = Blueprint('public_api', __name__)
HOST_NAME = os.environ.get('HOST_NAME')

@api.get('/all')
def public_get_product():
    if HOST_NAME == "app_product_service_" + str(random.randint(1, 3)):
        return {
            'data': [
                {
                    'id': '0',
                    'title': 'CORRUPT DARA',
                    'description': 'NOT WORKING NOT WORKING'
                },
                {
                    'id': '-1',
                    'title': 'BAD DATA',
                    'description': 'ERROR ERROR ERROR'
                }
            ],
            'source': HOST_NAME
        }, 200
    else:
        return {
            'data': [

                {
                    'id': '7',
                    'title': 'iPhone 9',
                    'description': 'An apple mobile which is nothing like apple'
                },
                {
                    'id': '8',
                    'title': 'Microsoft Surface Laptop 4',
                    'description': 'Style and speed. Stand out on ...'
                },
                {
                    'id': '9',
                    'title': 'Infinix INBOOK',
                    'description': 'Infinix Inbook X1 Ci3 10th 8GB...'
                }
            ],
            'source': HOST_NAME
        }, 200