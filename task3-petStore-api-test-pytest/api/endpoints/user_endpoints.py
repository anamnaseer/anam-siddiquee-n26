from typing import Dict, List, Optional
from requests import Response
from ..base_client import BaseAPIClient

class UserEndpoints(BaseAPIClient):
    """User-related API endpoints."""
    
    def __init__(self, base_url: str):
        super().__init__(base_url)
        self.base_endpoint = '/user'
    
    def create_user(self, user_data: Dict) -> Response:
        """
        Create a new user.
        
        Args:
            user_data: Dictionary containing user information
        """
        return self.request(
            method="POST",
            endpoint=self.base_endpoint,
            json=user_data
        )
    
    def create_users_with_list(self, users: List[Dict]) -> Response:
        """
        Create multiple users with a list input.
        
        Args:
            users: List of user dictionaries
        """
        return self.request(
            method="POST",
            endpoint=f"{self.base_endpoint}/createWithList",
            json=users
        )
    
    def login_user(self, username: str, password: str) -> Response:
        """
        Logs user into the system.
        
        Args:
            username: Username for login
            password: Password for login
        """
        return self.request(
            method="GET",
            endpoint=f"{self.base_endpoint}/login",
            params={"username": username, "password": password}
        )
    
    def logout_user(self) -> Response:
        """Logs out current logged in user session."""
        return self.request(
            method="GET",
            endpoint=f"{self.base_endpoint}/logout"
        )
    
    def get_user_by_username(self, username: str) -> Response:
        """
        Get user by username.
        
        Args:
            username: The name that needs to be fetched
        """
        return self.request(
            method="GET",
            endpoint=f"{self.base_endpoint}/{username}"
        )
    
    def update_user(self, username: str, user_data: Dict) -> Response:
        """
        Update user information.
        
        Args:
            username: Name of user to update
            user_data: Updated user data
        """
        return self.request(
            method="PUT",
            endpoint=f"{self.base_endpoint}/{username}",
            json=user_data
        )
    
    def delete_user(self, username: str) -> Response:
        """
        Delete user.
        
        Args:
            username: The name that needs to be deleted
        """
        return self.request(
            method="DELETE",
            endpoint=f"{self.base_endpoint}/{username}"
        )
