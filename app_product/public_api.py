import os
import random
from flask import Blueprint

api = Blueprint('public_api', __name__)
HOST_NAME = os.environ.get('HOST_NAME')

@api.get('/all')
def public_get_product():
    if HOST_NAME == "app_product_service_3":
        return {
            "data": [
                {
                    "idERROR": "0",
                    "titlesERROR": "CORRUPT DATA",
                    "descriptionsERROR": "NOT WORKING NOT WORKING"
                }
            ],
            "source": HOST_NAME,
            "infoDetails": { },
        }, 200
    else:
        return {
            "data": [
                {
                    "id": "7",
                    "title": "iPhone 9",
                    "description": "An apple mobile which is nothing like apple"
                },
                {
                    "id": "8",
                    "title": "Microsoft Surface Laptop 4",
                    "description": "Style and speed. Stand out on ..."
                },
                {
                    "id": "9",
                    "title": "Infinix INBOOK",
                    "description": "Infinix Inbook X1 Ci3 10th 8GB..."
                }
            ],
            "source": HOST_NAME,
            "infoDetails": {
                "totalRecords": 3,
                "recordsProcessed": 3,
                "dateProcessed": "2024-09-06"
            },
            "timestamp": "2024-09-06T10:05:00Z",
            "requestID": "req_67890"
        },200