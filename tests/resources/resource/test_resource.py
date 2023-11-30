import requests
from pytest import mark


@mark.resource
class ResourceTests:
    """
    Test case for calling resources.

    This test suite includes tests for:
    1. Calling multiple resources
    2. Calling a single resource
    3. Calling an invalid resource
    """

    def test_calling_multiple_resources(self, resource_uri):
        """
        Test calling multiple resources.

        Sends a GET request to the resource endpoint and checks if the response
        contains data for multiple resources. Compares the response with the
        expected names of resources.

        Args:
            resource_uri (str): The URI for the resource.

        Returns:
            None
        """
        response = requests.get(resource_uri)

        # Check if the response status code is successful (HTTP 200 OK)
        assert response.status_code == 200

        data = response.json()

        # Verify that the response contains data for multiple resources
        assert data["data"][0]["name"] == "cerulean"
        assert data["data"][1]["name"] == "fuchsia rose"
        assert data["data"][2]["name"] == "true red"
        assert data["data"][3]["name"] == "aqua sky"

    def test_calling_single_resource(self, resource_uri):
        """
        Test calling a single resource.

        Sends a GET request to the resource endpoint with a valid resource ID.
        Checks if the response contains data for the specified resource.
        Compares the response with the expected name of the resource.

        Args:
            resource_uri (str): The URI for the resource.

        Returns:
            None
        """
        valid_resource_id = "/2"
        updated_uri = f"{resource_uri}{valid_resource_id}"
        response = requests.get(updated_uri)

        # Check if the response status code is successful (HTTP 200 OK)
        assert response.status_code == 200

        data = response.json()

        # Verify that the response contains data for the specified resource
        assert data["data"]["name"] == "fuchsia rose"

    def test_calling_invalid_resource(self, resource_uri):
        """
        Test calling an invalid resource.

        Sends a GET request to the resource endpoint with an invalid resource ID.
        Checks if the response is empty and the status code is 404.

        Args:
            resource_uri (str): The URI for the resource.

        Returns:
            None
        """
        invalid_resource_id = "/4A"
        updated_uri = f"{resource_uri}{invalid_resource_id}"
        response = requests.get(updated_uri)

        # Check if the response status code indicates a resource not found (HTTP 404 Not Found)
        assert response.status_code == 404

        data = response.json()

        # Verify that the response is empty for an invalid resource
        assert data == {}
