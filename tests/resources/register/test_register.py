import requests
from pytest import mark

@mark.register
class RegisterTests:
    """
    Test case for user registration.

    This test suite includes tests for:
    1. Registration with valid email and password
    2. Registration with an undefined user
    3. Registration with an invalid email
    4. Registration with a blank password
    5. Registration with a missing password
    """

    def test_registration_with_valid_email_and_password(self, register_uri):
        """
        Test user registration with a valid email and password.

        Sends a POST request to the registration endpoint with a valid user.
        Compares the response with the expected data.

        Args:
            register_uri (str): The URI for user registration.

        Returns:
            None
        """
        valid_user = {"email": "eve.holt@reqres.in", "password": "pistol"}
        response = requests.post(register_uri, json=valid_user)
        actual = response.json()
        expected = {
            "id": 4,
            "token": "QpwL5tke4Pnpja7X4"
        }
        assert expected == actual
        assert response.status_code == 200

    def test_registration_with_undefined_user(self, register_uri):
        """
        Test user registration with an undefined user.

        Sends a POST request to the registration endpoint with an incomplete email.
        Compares the response with the expected error message.

        Args:
            register_uri (str): The URI for user registration.

        Returns:
            None
        """
        user_incomplete_email = {"email": "ailey.holt@rgmail.", "password": "nicest"}
        response = requests.post(register_uri, json=user_incomplete_email)
        data = response.json()
        assert data["error"] == "Note: Only defined users succeed registration"
        assert response.status_code == 400

    def test_invalid_email_registration(self, register_uri):
        """
        Test user registration with an invalid email.

        Sends a POST request to the registration endpoint with an invalid email.
        Compares the response with the expected error message.

        Args:
            register_uri (str): The URI for user registration.

        Returns:
            None
        """
        user_invalid_email = {"email": "eve.holt&reqres.in", "password": "nicest"}
        response = requests.post(register_uri, json=user_invalid_email)
        data = response.json()
        assert data["error"] == "Note: Only defined users succeed registration"
        assert response.status_code == 400

    def test_blank_password_registration(self, register_uri):
        """
        Test user registration with a blank password.

        Sends a POST request to the registration endpoint with a blank password.
        Compares the response with the expected error message.

        Args:
            register_uri (str): The URI for user registration.

        Returns:
            None
        """
        user_blank_password = {"email": "eve.holt@reqres.in", "password": ""}
        response = requests.post(register_uri, json=user_blank_password)
        data = response.json()
        assert data["error"] == "Missing password"
        assert response.status_code == 400

    def test_missing_password_registration(self, register_uri):
        """
        Test user registration with a missing password.

        Sends a POST request to the registration endpoint without providing a password.
        Compares the response with the expected error message.

        Args:
            register_uri (str): The URI for user registration.

        Returns:
            None
        """
        user_no_password = {"email": "eve.holt@reqres.in"}
        response = requests.post(register_uri, json=user_no_password)
        data = response.json()
        assert data["error"] == "Missing password"
        assert response.status_code == 400
