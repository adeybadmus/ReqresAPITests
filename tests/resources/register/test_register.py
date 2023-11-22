import requests


class RegisterTests():
    def test_registration_with_valid_email_and_password(self, register_uri):
        valid_user = {"email": "eve.holt@reqres.in", "password": "pistol"}
        response = requests.post(register_uri, json=valid_user)
        print(response.text)
        actual = response.json()
        expected = {
            "id": 4,
            "token": "QpwL5tke4Pnpja7X4"
        }
        assert expected == actual
        assert response.status_code == 200

    def test_registration_with_undefined_user(self, register_uri):
        user_incomplete_email = {"email": "ailey.holt@rgmail.", "password": "nicest"}
        response = requests.post(register_uri, json=user_incomplete_email)
        data = response.json()
        assert data["error"] == "Note: Only defined users succeed registration"
        assert response.status_code == 400

    def test_invalid_email_registration(self, register_uri):
        user_invalid_email = {"email": "eve.holt&reqres.in", "password": "nicest"}
        response = requests.post(register_uri, json=user_invalid_email)
        data = response.json()
        assert data["error"] == "Note: Only defined users succeed registration"
        assert response.status_code == 400

    def test_blank_password_registration(self, register_uri):
        user_blank_password = {"email": "eve.holt@reqres.in", "password": ""}
        response = requests.post(register_uri, json=user_blank_password)
        data = response.json()
        assert data["error"] == "Missing password"
        assert response.status_code == 400

    def test_missing_password_registration(self, register_uri):
        user_no_password = {"email": "eve.holt@reqres.in"}
        response = requests.post(register_uri, json=user_no_password)
        data = response.json()
        assert data["error"] == "Missing password"
        assert response.status_code == 400