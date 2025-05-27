from http import HTTPStatus
import pytest
from datetime import datetime, timezone
from models.order import Order

class TestStoreFlows:
    """Test cases for store-related operations."""

    @pytest.mark.e2e
    def test_get_inventory(self, store_api):
        """
        Test getting store inventory.
        Verifies:
        1. Successful response
        2. Response contains expected inventory status counts
        3. Response headers are correct
        """
        # Get inventory
        response = store_api.get_inventory()
        
        # Verify response status
        assert response.status_code == HTTPStatus.OK
        
        # Verify response contains inventory counts
        inventory = response.json()
        assert isinstance(inventory, dict)
        assert all(isinstance(count, int) for count in inventory.values())
        
        # Verify response headers
        headers = response.headers
        assert headers['content-type'] == 'application/json'
        assert headers['access-control-allow-origin'] == '*'
        assert 'GET' in headers['access-control-allow-methods'].split(',')

    @pytest.mark.e2e
    def test_create_order(self, store_api):
        """
        Test creating a store order.
        Verifies:
        1. Successful order creation
        2. Response matches input data
        3. Response headers are correct
        """
        # Create order data
        order = Order(
            id=10,
            petId=198772,
            quantity=7,
            shipDate=datetime.now(timezone.utc).isoformat(),
            status="approved",
            complete=True
        )
        
        # Create order
        response = store_api.create_order(order)
        
        # Print headers for debugging
        print("\nActual Response Headers:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")
        
        # Verify response status
        assert response.status_code == HTTPStatus.OK
        
        # Verify response data
        order_response = response.json()
        assert order_response['id'] == order.id
        assert order_response['petId'] == order.petId
        assert order_response['quantity'] == order.quantity
        assert order_response['status'] == order.status
        assert order_response['complete'] == order.complete
        
        # Verify response headers
        headers = response.headers
        assert headers['content-type'] == 'application/json'
        assert headers['access-control-allow-origin'] == '*'
        
        # Split methods and strip whitespace
        allowed_methods = [m.strip() for m in headers['access-control-allow-methods'].split(',')]
        expected_methods = ['GET', 'POST', 'DELETE', 'PUT']
        
        for method in expected_methods:
            assert method in allowed_methods, f"Expected {method} in allowed methods, but got: {allowed_methods}"
