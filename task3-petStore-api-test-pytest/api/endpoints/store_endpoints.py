from typing import Dict
from requests import Response
from ..base_client import BaseAPIClient
from models.order import Order

class StoreEndpoints(BaseAPIClient):
    """Client for store-related endpoints."""

    def get_inventory(self) -> Response:
        """
        Get store inventory.
        
        Returns:
            Response: API response containing inventory status counts
        """
        return self._get('/store/inventory')

    def create_order(self, order: Order) -> Response:
        """
        Place an order for a pet.
        
        Args:
            order: Order instance containing order details
            
        Returns:
            Response: API response containing created order
        """
        return self._post('/store/order', json=order.to_dict())

    def get_order_by_id(self, order_id: int) -> Response:
        """
        Find purchase order by ID.
        
        Args:
            order_id: ID of the order to retrieve
            
        Returns:
            Response: API response containing order details
        """
        return self._get(f'/store/order/{order_id}')

    def delete_order(self, order_id: int) -> Response:
        """
        Delete purchase order by ID.
        
        Args:
            order_id: ID of the order to delete
            
        Returns:
            Response: API response indicating deletion status
        """
        return self._delete(f'/store/order/{order_id}')
