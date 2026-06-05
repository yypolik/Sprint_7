import pytest
import allure
from api.courier_api import CourierAPI
from helpers.courier_generator import generate_random_string
from data.data import CourierData

class TestLoginCourier:
    
    @allure.title("Курьер может успешно авторизоваться, система возвращает id")
    def test_courier_can_login_returns_id(self, clean_courier):
        data = CourierData.login_payload(clean_courier[0], clean_courier[1])
        response = CourierAPI.login(data)
        
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Ошибка авторизации, если не передано одно из обязательных полей")
    @pytest.mark.parametrize("missing_field, expected_status", CourierData.LOGIN_MISSING_FIELDS_DATA)
    def test_login_missing_fields(self, clean_courier, missing_field, expected_status):
        data = CourierData.login_payload(clean_courier[0], clean_courier[1])
        data.pop(missing_field)
        response = CourierAPI.login(data)
        assert response.status_code == expected_status

    @allure.title("Ошибка авторизации, если указан неверный пароль или логин")
    def test_login_wrong_credentials(self, clean_courier):
        data = CourierData.login_payload(clean_courier[0], "wrong_password_123")
        response = CourierAPI.login(data)
        assert response.status_code == 404

    @allure.title("Ошибка авторизации под несуществующим пользователем")
    def test_login_nonexistent_user(self):
        data = CourierData.login_payload(generate_random_string(15), generate_random_string(10))
        response = CourierAPI.login(data)
        assert response.status_code == 404