import requests
from pytest import fixture

# Base URI for the Football API
uri = "https://reqres.in/api"


@fixture(scope='function', autouse=True)
def users_uri():
    """
    Fixture to provide the URI for the persons resource.
    """
    return f"{uri}/users"


@fixture(scope='function', autouse=True)
def register_uri():
    """
    Fixture to provide the URI for the persons resource.
    """
    return f"{uri}/register"


@fixture(scope='function', autouse=True)
def resource_uri():
    """
    Fixture to provide the URI for the persons resource.
    """
    return f"{uri}/unknown"
