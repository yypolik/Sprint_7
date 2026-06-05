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

@pytest.fixture
def generate_courier_data_and_delete():
    data = CourierData.generate_full_courier_payload()
    
    backup_login = data["login"]
    backup_password = data["password"]
    
    yield data
    
    login_data = CourierData.login_payload(backup_login, backup_password)
    login_response = CourierAPI.login(login_data)
    
    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")
        CourierAPI.delete(courier_id)

@pytest.fixture
def already_registered_courier(generate_courier_data_and_delete):
    CourierAPI.create(generate_courier_data_and_delete)
    return generate_courier_data_and_delete