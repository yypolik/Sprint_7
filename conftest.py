import pytest
from api.courier_api import CourierAPI
from helpers.courier_generator import register_new_courier_and_return_login_password
from data.data import CourierData

@pytest.fixture
def clean_courier():
    courier_data = register_new_courier_and_return_login_password()
    yield courier_data
    
    if courier_data:
        login_data = CourierData.login_payload(courier_data[0], courier_data[1])
        login_response = CourierAPI.login(login_data)
        
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
            CourierAPI.delete(courier_id)