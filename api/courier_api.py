import requests
import allure
from urls.urls import COURIER_URL, LOGIN_URL

class CourierAPI:
    @staticmethod
    def create(payload):
        with allure.step(f"Отправка POST-запроса на создание курьера: {COURIER_URL}"):
            return requests.post(COURIER_URL, data=payload)

    @staticmethod
    def login(payload):
        with allure.step(f"Отправка POST-запроса на авторизацию курьера: {LOGIN_URL}"):
            return requests.post(LOGIN_URL, data=payload)
            
    @staticmethod
    def delete(courier_id):
        with allure.step(f"Отправка DELETE-запроса на удаление курьера"):
            return requests.delete(f"{COURIER_URL}/{courier_id}")