import requests
from pytest import mark


@mark.user
class UserTests:
    """
    Test case for interacting with user-related API endpoints.

    This test suite includes tests for:
    1. Calling a single user request
    2. Calling multiple users request
    3. Calling an unavailable single user
    4. Calling an invalid single user
    5. Creating a user record
    6. Updating a user record
    7. Deleting a single user
    8. Patching a user record
    """

    def test_calling_single_user_request(self, users_uri):
        """
        Test calling a single user request.

        Sends a GET request to the user endpoint with a specific user ID.
        Checks if the response contains data for the specified user.
        Compares the response with the expected email, first name, and status code.

        Args:
            users_uri (str): The URI for the users.

        Returns:
            None
        """
        uri = f"{users_uri}/2"
        response = requests.get(uri)
        data = response.json()

        # Verify that the response contains the specified user's data
        assert data["data"]["email"] == "janet.weaver@reqres.in"
        assert data["data"]["first_name"] == "Janet"
        assert response.status_code == 200

    def test_calling_multiple_users_request(self, users_uri):
        """
        Test calling multiple users request.

        Sends a GET request to the users endpoint with a specific page.
        Checks if the response contains data for multiple users.
        Compares the response with the expected page, user IDs, first names, and status code.

        Args:
            users_uri (str): The URI for the users.

        Returns:
            None
        """
        uri = f"{users_uri}/?page=2"
        response = requests.get(uri)
        data = response.json()

        # Verify that the response contains data for multiple users
        assert data["page"] == 2
        assert data["data"][0]["id"] == 7
        assert data["data"][0]["first_name"] == "Michael"
        assert data["data"][1]["id"] == 8
        assert data["data"][1]["first_name"] == "Lindsay"
        assert response.status_code == 200

    def test_calling_unavailable_single_user(self, users_uri):
        """
        Test calling an unavailable single user.

        Sends a GET request to the users endpoint with an invalid user ID.
        Checks if the response is empty and the status code is 404.

        Args:
            users_uri (str): The URI for the users.

        Returns:
            None
        """
        uri = f"{users_uri}/800"
        response = requests.get(uri)
        data = response.json()

        # Verify that the response is empty for an unavailable user
        assert data == {}
        assert response.status_code == 404

    def test_calling_an_invalid_single_user(self, users_uri):
        """
        Test calling an invalid single user.

        Sends a GET request to the users endpoint with an invalid user ID.
        Checks if the response is empty and the status code is 404.

        Args:
            users_uri (str): The URI for the users.

        Returns:
            None
        """
        uri = f"{users_uri}/aaa"
        response = requests.get(uri)
        data = response.json()

        # Verify that the response is empty for an invalid user
        assert data == {}
        assert response.status_code == 404

    def test_creating_user_record(self, users_uri, random_string):
        """
        Test creating a user record.

        Sends a POST request to the users endpoint with user data.
        Checks if the response contains the created user's data.
        Compares the response with the expected name, job, and status code.

        Args:
            users_uri (str): The URI for the users.
            random_string (str): A random string for creating a unique user.

        Returns:
            None
        """
        name = f"{random_string}"
        user = {"name": name, "Job": "Leader"}
        response = requests.post(users_uri, json=user)
        data = response.json()

        # Verify that the response contains the created user's data
        assert data["name"] == name
        assert data["Job"] == "Leader"
        assert response.status_code == 201

    @mark.chain
    def test_update_a_user_record(self, users_uri, random_string):
        """
        Test updating a user record.

        Sends a POST request to the users endpoint to create a user.
        Sends a PUT request to update the created user's data.
        Checks if the response contains the updated user's data.
        Compares the response with the expected name, job, and status code.

        Args:
            users_uri (str): The URI for the users.
            random_string (str): A random string for creating a unique user.

        Returns:
            None
        """
        name = f"{random_string}"
        user = {"name": name, "Job": "CEO"}
        response = requests.post(users_uri, json=user)
        data = response.json()

        # Verify that the response contains the created user's data
        assert data["name"] == name

        user_id = data["id"]
        name2 = f"{name}2"
        user_update = {"name": name2, "Job": "VP"}
        update_uri = f"{users_uri}/{user_id}"
        new_response = requests.put(update_uri, json=user_update)
        data2 = new_response.json()

        # Verify that the response contains the updated user's data
        assert data2["name"] == name2
        assert data2["Job"] == "VP"
        assert new_response.status_code == 200

    @mark.chain
    def test_delete_single_user(self, users_uri, random_string):
        """
        Test deleting a single user.

        Sends a POST request to the users endpoint to create a user.
        Sends a DELETE request to delete the created user.
        Checks if the response status code is 204.

        Args:
            users_uri (str): The URI for the users.
            random_string (str): A random string for creating a unique user.

        Returns:
            None
        """
        name = f"{random_string}"
        user = {"name": name, "Job": "Leader"}
        response = requests.post(users_uri, json=user)
        assert response.status_code == 201
        data = response.json()
        user_id = data["id"]

        delete_uri = f"{users_uri}/{user_id}"
        response = requests.delete(delete_uri)

        # Verify that the response status code indicates a successful deletion (HTTP 204 No Content)
        assert response.status_code == 204

    @mark.chain
    def test_patch_user_record(self, users_uri, random_string):
        """
        Test patching a user record.

        Sends a POST request to the users endpoint to create a user.
        Sends a PATCH request to patch the created user's data.
        Checks if the response contains the patched user's data.
        Compares the response with the expected name, job, and status code.

        Args:
            users_uri (str): The URI for the users.
            random_string (str): A random string for creating a unique user.

        Returns:
            None
        """
        name = f"{random_string}"
        user = {"name": name, "Job": "CEO"}
        response = requests.post(users_uri, json=user)
        data = response.json()

        # Verify that the response contains the created user's data
        assert data["name"] == name

        user_id = data["id"]
        name2 = f"{name}2"
        user_update = {"name": name2, "Job": "VP"}
        update_uri = f"{users_uri}/{user_id}"

        new_response = requests.patch(update_uri, json=user_update)
        data2 = new_response.json()

        # Verify that the response contains the patched user's data
        assert data2["name"] == name2
        assert data2["Job"] == "VP"
        assert new_response.status_code == 200
