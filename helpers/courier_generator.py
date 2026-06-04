import random
import string
from api.courier_api import CourierAPI

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def register_new_courier_and_return_login_password():
    login_pass = []
    login = generate_random_string()
    password = generate_random_string()
    first_name = generate_random_string()

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = CourierAPI.create(payload)

    if response.status_code == 201:
        login_pass.extend([login, password, first_name])

    return login_pass