import requests
from unittest import TestCase

base_url = "https://reqres.in/api/"


class TestResource(TestCase):
    def test_multiple_resources(self):
        resource = "unknown"
        url = base_url + resource
        response = requests.get(url)
        print(response.text)
        assert response.status_code == 200

    def test_single_resource(self):
        resource = "unknown/4"
        url = base_url + resource
        response = requests.get(url)
        print(response.text)
        assert response.status_code == 200


    def test_invalid_resource(self):
        resource = "unknown/4A"
        url = base_url + resource
        response = requests.get(url)
        print(response.text)
        assert response.status_code == 404