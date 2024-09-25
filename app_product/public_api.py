import logging
import os
from flask import Blueprint

log_dir = './logs/'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configura el logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s)',
                    filename=os.path.join(log_dir, 'public.log'),
                    filemode='a')

api = Blueprint('public_api', __name__)
HOST_NAME = os.environ.get('HOST_NAME')

@api.get('/all')
def public_get_product():
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
    }, 200
