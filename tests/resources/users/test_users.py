import requests

class UserTests():

    def test_calling_single_user_request(self, users_uri):
        uri = f"{users_uri}/2"
        response = requests.get(uri)
        data = response.json()
        assert data["data"]["email"] == "janet.weaver@reqres.in"
        assert data["data"]["first_name"] == "Janet"
        assert response.status_code == 200

    def test_calling_multiple_users_request(self, users_uri):
        uri = f"{users_uri}/?page=2"
        response = requests.get(uri)
        data = response.json()
        assert data["page"] == 2
        assert data["data"][0]["id"] == 7
        assert data["data"][0]["first_name"] == "Michael"
        assert data["data"][1]["id"] == 8
        assert data["data"][1]["first_name"] == "Lindsay"
        assert response.status_code == 200

    def test_calling_unavailable_single_user(self, users_uri):
        uri = f"{users_uri}/800"
        response = requests.get(uri)
        data = response.json()
        assert data == {}
        assert response.status_code == 404

    def test_calling_an_invalid_single_user(self, users_uri):
        uri = f"{users_uri}/aaa"
        response = requests.get(uri)
        data = response.json()
        assert data == {}
        assert response.status_code == 404

    def test_creating_a_single_user(self, users_uri):
        user = {"name": "Ade", "Job": "Leader" }
        response = requests.post(users_uri, json=user)
        data = response.json()
        # print(response.text)
        assert data["name"] == "Ade"
        assert data["Job"] == "Leader"
        assert response.status_code == 201

    def test_updating_a_single_user_record(self, users_uri):
        user = {"name": "Ade B", "Job": "CEO"}
        response = requests.post(users_uri, json=user)
        data = response.json()
        print(data)


        user_id = data["id"]
        user_update  = {"name": "Ade Badmus", "Job": "VP" }
        update_uri = f"{users_uri}/{user_id}"
        new_response = requests.put(update_uri, json=user_update)
        print(new_response.text)
        data2 = new_response.json()
        assert data2["name"] == "Ade Badmus"
        assert data2["Job"] == "VP"
        assert response.status_code == 201

    def test_delete_single_user(self, users_uri):
        uri = f"{users_uri}/2"
        response = requests.delete(uri)
        assert response.status_code == 204