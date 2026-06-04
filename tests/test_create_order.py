import pytest
import allure
from api.order_api import OrderAPI
from data.data import OrderData

class TestCreateOrder:

    @allure.title("Создание заказа с различными конфигурациями цветов")
    @pytest.mark.parametrize("color_option", OrderData.COLOR_OPTIONS)
    def test_create_order_with_different_colors(self, color_option):
        data = OrderData.generate_order_payload(color=color_option)
        
        response = OrderAPI.create(data)
        
        assert response.status_code == 201
        assert "track" in response.json()