import requests
from pytest import fixture

# Base URI for the Football API
uri = "https://reqres.in/api"


@fixture(scope='function', autouse=True)
def create_user(users_uri, random_string):
    """
    Fixture to provide the URI for the users resource.

    Returns:
        str: The URI for the users resource.
    """
    # return f"{uri}/users"
    name = f"{random_string}"
    user = {"name": name, "Job": "CEO"}
    response = requests.post(users_uri, json=user)
    data = response.json()
    return data, name
