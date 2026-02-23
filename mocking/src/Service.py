import requests

from mocking.src.Database import check_availability, get_password


def is_available():
    # some code that checks for database availability
    print("Database service")
    return check_availability()


def validate_user(username, password):
    actual_password = get_password(username)
    if password == actual_password:
        return True
    else:
        return False


def get_user_city():
    response = requests.get("https://mocki.io/v1/a68af8ae-48e7-4f19-b4dc-b7a6dc7feae2")
    if response.status_code == 200:
        return list(response.json())
