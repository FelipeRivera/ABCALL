from flask import Flask, request, jsonify
import requests
from collections import Counter
from typing import Any, Dict, List
import concurrent.futures
import logging

# Configura el logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

SERVICES = [
    "http://app_product_service_1:8080",
    "http://app_product_service_2:8080",
    "http://app_product_service_3:8080"
]

def make_hashable(obj: Any) -> Any:
    """Convert a dict, list, or other object to a hashable form."""
    if isinstance(obj, dict):
        return tuple(sorted((k, make_hashable(v)) for k, v in obj.items()))
    elif isinstance(obj, list):
        return tuple(make_hashable(i) for i in obj)
    else:
        return obj

def majority_vote(responses: List[requests.Response]) -> Dict:
    """Return the most common response among the list of responses."""
    if len(responses) == 1:
        return responses[0].json()

    resp_dicts = [response.json() for response in responses if response.ok]

    if not resp_dicts:
        logging.debug("No valid responses found.")
        return None

    hashable_dicts = [make_hashable(d) for d in resp_dicts]
    counter = Counter(hashable_dicts)

    most_common = counter.most_common(1)

    if most_common:
        most_common_dict = dict(most_common[0][0])
        logging.debug(f"Most common dict: {most_common_dict}")
        for response in responses:
            response_hashable = make_hashable(response.json())
            if response_hashable == make_hashable(most_common_dict):
                logging.debug(f"Correct response found: {response.json()}")
                return response.json()

    logging.debug("No correct response found.")
    return None

def fetch_service_response(service: str, path: str) -> requests.Response:
    """Fetch response from a service and handle exceptions."""
    try:
        return requests.get(f"{service}{path}")
    except requests.RequestException as e:
        logging.error(f"Error requesting {service}: {e}")
        return None

@app.route('/validate', methods=['GET'])
def validate():
    """Validate responses from services and return the majority vote result."""
    path = request.args.get('path')

    responses = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(fetch_service_response, service, path) for service in SERVICES]
        for future in concurrent.futures.as_completed(futures):
            response = future.result()
            if response:
                responses.append(response)

    correct_response = majority_vote(responses)

    if correct_response is None:
        return jsonify({'message': 'No se encontró una respuesta correcta'}), 404

    return jsonify(correct_response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)