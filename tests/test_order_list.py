import allure
from api.order_api import OrderAPI

class TestOrderList:

    @allure.title("Запрос списка заказов")
    def test_get_order_list_returns_orders_array(self):
        response = OrderAPI.get_list()
        
        assert response.status_code == 200
        
        response_body = response.json()
        assert "orders" in response_body
        assert isinstance(response_body["orders"], list)