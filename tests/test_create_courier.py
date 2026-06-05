import pytest
import allure
from api.courier_api import CourierAPI
from data.data import CourierData

class TestCreateCourier:
    
    @allure.title("Успешное создание курьера с заполнением всех обязательных полей")
    def test_create_courier_success(self, generate_courier_data_and_delete):

        response = CourierAPI.create(generate_courier_data_and_delete)
        
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_identical_couriers_fails(self, already_registered_courier):
        
        response = CourierAPI.create(already_registered_courier)
        
        assert response.status_code == 409

    @allure.title("Ошибка при создании курьера, если отсутствует обязательное поле")
    @pytest.mark.parametrize("missing_field", CourierData.MISSING_FIELDS_CREATION)
    def test_create_courier_missing_fields(self, generate_courier_data_and_delete, missing_field):

        generate_courier_data_and_delete.pop(missing_field)
        
        response = CourierAPI.create(generate_courier_data_and_delete)
        
        assert response.status_code == 400