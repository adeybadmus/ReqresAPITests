import requests
from pytest import mark


@mark.register
class RegisterTests:
    """
    Test case for user registration.

    This test suite includes tests for:
    1. Registration with valid email and password
    2. Registration with an undefined user
    3. Registration with a blank password
    4. Registration with a missing password
    """

    def test_registration_request(self, register_uri):
        """
        Test user registration with a valid email and password.

        Sends a POST request to the registration endpoint with a valid user.
        Compares the response with the expected data.

        Args:
            register_uri (str): The URI for user registration.

        Returns:
            None
        """
        data = {"email": "eve.holt@reqres.in", "password": "pistol"}
        response = requests.post(register_uri, json=data)

        # Check if the response is successful (HTTP 200 OK)
        assert response.status_code == 200

        actual = response.json()
        expected = {
            "id": 4,
            "token": "QpwL5tke4Pnpja7X4"
        }

        # Compare the actual response data with the expected data
        assert expected == actual
        assert actual["id"] is not None
        assert actual["token"] is not None

    def test_unsuccessful_registration_undefined_user(self, register_uri, random_string):
        """
        Test user registration with an undefined user.

        Sends a POST request to the registration endpoint with an incomplete email.
        Compares the response with the expected error message.

        Args:
            register_uri (str): The URI for user registration.
            random_string (str): A random string used to create an undefined email.

        Returns:
            None
        """
        invalid_email = f"{random_string}@gmail.com"
        data = {"email": invalid_email, "password": "nicest"}
        response = requests.post(register_uri, json=data)

        # Check if the response indicates an unsuccessful registration (HTTP 400 Bad Request)
        assert response.status_code == 400

        response_data = response.json()
        expected_error = "Note: Only defined users succeed registration"

        # Compare the actual error message with the expected error message
        assert response_data["error"] == expected_error

    def test_unsuccessful_registration_blank_password(self, register_uri):
        """
        Test user registration with a blank password.

        Sends a POST request to the registration endpoint with a blank password.
        Compares the response with the expected error message.

        Args:
            register_uri (str): The URI for user registration.

        Returns:
            None
        """
        blank_password = ""
        data = {"email": "eve.holt@reqres.in", "password": blank_password}
        response = requests.post(register_uri, json=data)

        # Check if the response indicates a missing password error (HTTP 400 Bad Request)
        assert response.status_code == 400

        response_data = response.json()
        expected_error = "Missing password"

        # Compare the actual error message with the expected error message
        assert response_data["error"] == expected_error

    def test_unsuccessful_registration_missing_password(self, register_uri):
        """
        Test user registration with a missing password.

        Sends a POST request to the registration endpoint without providing a password.
        Compares the response with the expected error message.

        Args:
            register_uri (str): The URI for user registration.

        Returns:
            None
        """
        data = {"email": "eve.holt@reqres.in"}
        response = requests.post(register_uri, json=data)

        # Check if the response indicates a missing password error (HTTP 400 Bad Request)
        assert response.status_code == 400

        response_data = response.json()
        expected_error = "Missing password"

        # Compare the actual error message with the expected error message
        assert response_data["error"] == expected_error
