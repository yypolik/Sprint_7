import pytest
import allure
from api.courier_api import CourierAPI
from data.data import CourierData

class TestCreateCourier:
    
    @allure.title("Успешное создание курьера с заполнением всех обязательных полей")
    def test_create_courier_success(self):
        data = CourierData.generate_full_courier_payload()
        response = CourierAPI.create(data)
        
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_identical_couriers_fails(self):
        data = CourierData.generate_full_courier_payload()
        
        CourierAPI.create(data)
        response = CourierAPI.create(data)
        
        assert response.status_code == 409

    @allure.title("Ошибка при создании курьера, если отсутствует обязательное поле")
    @pytest.mark.parametrize("missing_field", CourierData.MISSING_FIELDS_CREATION)
    def test_create_courier_missing_fields(self, missing_field):
        data = CourierData.generate_full_courier_payload()
        data.pop(missing_field)
        
        response = CourierAPI.create(data)
        
        assert response.status_code == 400