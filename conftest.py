import random
import string
from pytest import fixture

# Base URI for the Football API
uri = "https://reqres.in/api"


@fixture(scope='function', autouse=True)
def users_uri():
    """
    Fixture to provide the URI for the users resource.

    Returns:
        str: The URI for the users resource.
    """
    return f"{uri}/users"


@fixture(scope='function', autouse=True)
def register_uri():
    """
    Fixture to provide the URI for the register resource.

    Returns:
        str: The URI for the register resource.
    """
    return f"{uri}/register"


@fixture(scope='function', autouse=True)
def resource_uri():
    """
    Fixture to provide the URI for the resource.

    Returns:
        str: The URI for the resource.
    """
    return f"{uri}/unknown"


@fixture(scope='function')
def random_string():
    """
    Fixture to generate a random string of lowercase letters.

    Returns:
        str: A random string of lowercase letters.
    """
    letters = string.ascii_letters.lower()
    return ''.join(random.choice(letters) for i in range(10))
