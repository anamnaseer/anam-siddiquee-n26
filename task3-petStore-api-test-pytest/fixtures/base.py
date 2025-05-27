import json
import requests
import random,string
from requests import Response




class BaseClass:

    BASE_URL = "http://localhost:8080/api/v3"

    def to_dict(self) -> dict:
        """
        Convert nested object to dict
        :return: dict
        """
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))

    def random_string(length=8):
        """Generate a random string for unique usernames."""
        return ''.join(random.choices(string.ascii_letters, k=length))

    def get(self, endpoint):
        """Generic GET request."""
        response = requests.get(endpoint)
        return response

    def post(self, endpoint, data):
        """Generic POST request."""
        response = requests.post(endpoint, json=data)
        return response

    def put(self, endpoint, data):
        """Generic PUT request."""
        response = requests.put(endpoint, json=data)
        return response

    def delete(self, endpoint):
        """Generic DELETE request."""
        response = requests.delete(endpoint)
        return response

    def request(self, method: str, url: str, **kwargs) -> Response:
        """
        Request method
        method: method for the new Request object: GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE.
        url – URL for the new Request object.
        **kwargs:
            params – (optional) Dictionary, list of tuples or bytes to send in the query string for the Request. # noqa
            json – (optional) A JSON serializable Python object to send in the body of the Request. # noqa
            headers – (optional) Dictionary of HTTP Headers to send with the Request.
        """
        return requests.request(method, url, **kwargs)