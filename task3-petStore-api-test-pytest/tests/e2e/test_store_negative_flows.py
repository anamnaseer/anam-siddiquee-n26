from http import HTTPStatus
import pytest
from datetime import datetime, timezone
from models.order import Order

class TestStoreNegativeFlows:
    """Test cases for store-related error scenarios."""

    @pytest.mark.e2e
    @pytest.mark.negative
    def test_create_order_invalid_input(self, store_api):
        """
        Test creating an order with invalid input.
        Verifies:
        1. Response status code is 400 for invalid input
        2. Error message is returned
        """
        # Create invalid order data (missing required fields)
        invalid_order = Order(
            id="test",
            petId=None,
            quantity=None,
            shipDate=None,
            status=None,
            complete=None
        )
        
        # Attempt to create order
        response = store_api.create_order(invalid_order)
      
        # Verify response status
        assert response.status_code == HTTPStatus.BAD_REQUEST
        
        # Verify error response
        error_response = response.json()
        assert 'message' in error_response

    @pytest.mark.e2e
    @pytest.mark.negative
    def test_create_order_validation_exception(self, store_api):
        """
        Test creating an order with validation errors.
        Verifies:
        1. Response status code is 422 for validation errors
        2. Validation error details are returned
        """
        # Create order with multiple validation issues to trigger 422
        invalid_order = Order(
            id=-1,  # Invalid negative ID
            petId=-2,  # Invalid negative petId
            quantity=-3,  # Invalid negative quantity
            shipDate="invalid-date-format",  # Invalid date format
            status="INVALID_STATUS",  # Invalid status value
            complete="not-a-boolean"  # Invalid boolean type
        )
        
        # Attempt to create order
        response = store_api.create_order(invalid_order)
   
        # Verify response status
        assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
        print("response_code unexpected error request: " + str(response.status_code))
        # Verify error response
        error_response = response.json()
        assert 'message' in error_response

    @pytest.mark.e2e
    @pytest.mark.negative
    def test_create_order_unexpected_error(self, store_api):
        """
        Test handling of unexpected errors during order creation.
        Verifies:
        1. Response contains error details for unexpected errors
        """
        # Create order with data that might trigger server error
        problematic_order = Order(
            id=999999999999999999,  # Extremely large ID
            petId=999999999999999999,  # Extremely large petId
            quantity=999999999999999999,  # Extremely large quantity
            shipDate=datetime.now(timezone.utc).isoformat(),
            status="approved",
            complete=True
        )
        
        # Attempt to create order
        response = store_api.create_order(problematic_order)
     
        # Verify error response contains message
        error_response = response.json()
        assert 'message' in error_response
