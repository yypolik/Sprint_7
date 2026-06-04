from helpers.courier_generator import generate_random_string

class CourierData:
    MISSING_FIELDS_CREATION = ["login", "password"]
    MISSING_FIELDS_LOGIN = ["login", "password"]

    @staticmethod
    def generate_full_courier_payload():
        return {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

    @staticmethod
    def login_payload(login, password):
        return {
            "login": login,
            "password": password
        }


class OrderData:
    COLOR_OPTIONS = [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ]

    @staticmethod
    def generate_order_payload(color=None):
        return {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2026-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color if color is not None else []
        }