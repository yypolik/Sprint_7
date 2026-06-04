import requests
import allure
from urls.urls import ORDERS_URL

class OrderAPI:
    @staticmethod
    def create(payload):
        with allure.step(f"Отправка POST-запроса на создание заказа: {ORDERS_URL}"):
            return requests.post(ORDERS_URL, json=payload)

    @staticmethod
    def get_list():
        with allure.step(f"Отправка GET-запроса на получение списка заказов: {ORDERS_URL}"):
            return requests.get(ORDERS_URL)