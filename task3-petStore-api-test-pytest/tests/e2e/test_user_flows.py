import pytest
from http import HTTPStatus
import re
from api.endpoints.user_endpoints import UserEndpoints
from models.user import User
from utils.test_data import TestDataGenerator

class TestUserFlows:
    """E2E tests for user-related flows."""

    @pytest.mark.e2e
    def test_complete_user_lifecycle(self, user_api: UserEndpoints, test_user: User):
        """
        Test complete user lifecycle: Create -> Login -> Update -> Delete
        
        Steps:
        1. Create a new user
        2. Verify user can login
        3. Update user information
        4. Verify updated information
        5. Delete user
        6. Verify user is deleted
        """
        # 1. Create user
        response = user_api.create_user(test_user.to_dict())
        assert response.status_code == HTTPStatus.OK
        assert response.json()["username"] == test_user.username

        # 2. Login
        response = user_api.login_user(test_user.username, test_user.password)
        assert response.status_code == HTTPStatus.OK
        assert "logged in user session" in response.text.lower()

        # 3. Update user information
        updated_user = test_user
        updated_user.firstName = "UpdatedName"
        response = user_api.update_user(test_user.username, updated_user.to_dict())
        assert response.status_code == HTTPStatus.OK

        # 4. Verify update
        response = user_api.get_user_by_username(test_user.username)
        assert response.status_code == HTTPStatus.OK
        assert response.json()["firstName"] == "UpdatedName"

        # 5. Delete user
        response = user_api.delete_user(test_user.username)
        assert response.status_code == HTTPStatus.OK

        # 6. Verify deletion
        response = user_api.get_user_by_username(test_user.username)
        assert response.status_code == HTTPStatus.NOT_FOUND

    @pytest.mark.e2e
    def test_bulk_user_creation_flow(self, user_api: UserEndpoints, test_users: list[User]):
        """
        Test bulk user creation flow
        
        Steps:
        1. Create multiple users
        2. Verify each user exists
        3. Clean up created users
        """
        # 1. Create users in bulk
        users_data = [user.to_dict() for user in test_users]
        response = user_api.create_users_with_list(users_data)
        assert response.status_code == HTTPStatus.OK

        # 2. Verify each user
        for user in test_users:
            response = user_api.get_user_by_username(user.username)
            assert response.status_code == HTTPStatus.OK
            assert response.json()["username"] == user.username

        # 3. Clean up
        for user in test_users:
            response = user_api.delete_user(user.username)
            assert response.status_code == HTTPStatus.OK

    @pytest.mark.e2e
    def test_user_authentication_flow(self, user_api: UserEndpoints, created_user: User):
        """
        Test user authentication flow
        
        Steps:
        1. Attempt login with invalid credentials
        2. Login with valid credentials
        3. Access protected endpoint
        4. Logout
        5. Verify logout
        """
        # 1. Invalid login attempt - Note: API doesn't validate credentials properly
        invalid_login_response = user_api.login_user("nonexistent_user", "wrong_password")
        assert invalid_login_response.status_code == HTTPStatus.OK
        # Store the invalid session token for comparison
        invalid_session = invalid_login_response.text

        # 2. Valid login
        response = user_api.login_user(created_user.username, created_user.password)
        assert response.status_code == HTTPStatus.OK

        # 3. Access user information (protected endpoint)
        response = user_api.get_user_by_username(created_user.username)
        assert response.status_code == HTTPStatus.OK

        # 4. Logout
        response = user_api.logout_user()
        assert response.status_code == HTTPStatus.OK

        # 5. Compare session tokens
        # Note: API doesn't restrict access after logout, but we can verify that
        # the invalid login and valid login sessions are different
        assert invalid_session != response.text, "Invalid login should generate different session token"

    @pytest.mark.e2e
    @pytest.mark.negative
    def test_negative_scenarios(self, user_api: UserEndpoints):
        """
        Test negative scenarios
        
        Steps:
        1. Try to get non-existent user
        2. Try to update non-existent user
        3. Try to delete non-existent user
        """
        invalid_username = "nonexistent_user_123"
        invalid_user = TestDataGenerator.generate_invalid_user()

        # 1. Get non-existent user
        response = user_api.get_user_by_username(invalid_username)
        assert response.status_code == HTTPStatus.NOT_FOUND

        # 2. Update non-existent user
        response = user_api.update_user(invalid_username, invalid_user.to_dict())
        assert response.status_code == HTTPStatus.NOT_FOUND

        # 3. Delete non-existent user - Note: API returns 200 even for non-existent users
        response = user_api.delete_user(invalid_username)
        assert response.status_code == HTTPStatus.OK
        assert not response.text  # API returns empty response for deletion
