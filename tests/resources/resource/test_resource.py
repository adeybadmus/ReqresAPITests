import requests


class ResourceTests():
    def test_calling_multiple_resources(self, resource_uri):
        response = requests.get(resource_uri)
        data = response.json()
        assert data["data"][0]["name"] == "cerulean"
        assert data["data"][1]["name"] == "fuchsia rose"
        assert data["data"][2]["name"] == "true red"
        assert data["data"][3]["name"] == "aqua sky"
        assert response.status_code == 200

    def test_calling_single_resource(self, resource_uri):
        valid_resource_id = "/2"
        updated_uri = f"{resource_uri}{valid_resource_id}"
        response = requests.get(updated_uri)
        data = response.json()
        assert data["data"]["name"] == "fuchsia rose"
        assert response.status_code == 200


    def test_calling_invalid_resource(self, resource_uri):
        invalid_resource_id = "/4A"
        updated_uri = f"{resource_uri}{invalid_resource_id}"
        response = requests.get(updated_uri)
        data = response.json()
        assert  data == {}
        assert response.status_code == 404