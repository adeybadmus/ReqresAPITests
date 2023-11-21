import requests
from unittest import TestCase

base_url = "https://reqres.in/api/"


class TestUser(TestCase):

    def test_get_multiple_users_information(self):
        resource = "users?page=2"
        url = base_url + resource
        response = requests.get(url)
        print(response.text)
        assert response.status_code == 200

    def test_get_single_user(self):
        resource = "users/8"
        url = base_url + resource
        response = requests.get(url)
        print(response.text)
        assert response.status_code == 200

    def test_get_unavailable_single_user(self):
        resource = "users/800"
        url = base_url + resource
        response = requests.get(url)
        print(response.text)
        assert response.status_code == 404

    def test_get_invalid_single_user(self):
        resource = "users/aaa"
        url = base_url + resource
        response = requests.get(url)
        print(response.text)
        assert response.status_code == 404

    def test_create_single_user(self):
        resource = "users"
        url = base_url + resource
        body = {"name": "Mariam", "Job": "Leader" }
        response = requests.post(url, body)
        print(response.text)
        assert response.status_code == 201

    def test_update_single_user(self):
        resource = "users/839"
        url = base_url + resource
        body = {"name": "Mariam Badmus", "Job": "VP" }
        response = requests.put(url, body)
        print(response.text)
        assert response.status_code == 200

    def test_delete_single_user(self):
        resource = "users/2"
        url = base_url + resource
        response = requests.delete(url)
        print(response.text)
        assert response.status_code == 204