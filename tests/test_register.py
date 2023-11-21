import requests
from unittest import TestCase

base_url = "https://reqres.in/api/"


class TestRegister(TestCase):
    def test_successful_registration(self):
        resource = "register"
        url = base_url + resource
        body = {"email": "eve.holt@reqres.in", "password": "nicest"}
        response = requests.post(url, body)
        print(response.text)
        assert response.status_code == 200

    def test_incomplete_email_registration(self):
        resource = "register"
        url = base_url + resource
        body = {"email": "eve.holt@reqres.", "password": "nicest"}
        response = requests.post(url, body)
        print(response.text)
        assert response.status_code == 400

    def test_invalid_email_registration(self):
        resource = "register"
        url = base_url + resource
        body = {"email": "eve.holt&reqres.in", "password": "nicest"}
        response = requests.post(url, body)
        print(response.text)
        assert response.status_code == 400

    def test_blank_password_registration(self):
        resource = "register"
        url = base_url + resource
        body = {"email": "eve.holt&reqres.in", "password": ""}
        response = requests.post(url, body)
        print(response.text)
        assert response.status_code == 400

    def test_missing_password_registration(self):
        resource = "register"
        url = base_url + resource
        body = {"email": "eve.holt&reqres.in"}
        response = requests.post(url, body)
        print(response.text)
        assert response.status_code == 400