import pytest
from typing import Generator
from api.endpoints.user_endpoints import UserEndpoints
from api.endpoints.store_endpoints import StoreEndpoints
from utils.test_data import TestDataGenerator
from config.config import config
from models.user import User

@pytest.fixture(scope="session")
def user_api() -> UserEndpoints:
    """
    Fixture that provides the UserEndpoints instance.
    
    Returns:
        UserEndpoints instance
    """
    return UserEndpoints(config.api.base_url)

@pytest.fixture(scope="session")
def store_api() -> StoreEndpoints:
    """
    Fixture that provides the StoreEndpoints instance.
    
    Returns:
        StoreEndpoints instance
    """
    return StoreEndpoints(config.api.base_url)
    
@pytest.fixture
def test_user() -> User:
    """
    Fixture that provides a test user.
    
    Returns:
        User instance with random test data
    """
    return TestDataGenerator.generate_user()

@pytest.fixture
def test_users() -> list[User]:
    """
    Fixture that provides multiple test users.
    
    Returns:
        List of User instances
    """
    return TestDataGenerator.generate_users(3)

@pytest.fixture
def created_user(user_api: UserEndpoints, test_user: User) -> Generator[User, None, None]:
    """
    Fixture that creates a user and ensures cleanup after test.
    
    Args:
        user_api: UserEndpoints instance
        test_user: User instance to create
        
    Yields:
        Created User instance
    """
    # Create the user
    response = user_api.create_user(test_user.to_dict())
    assert response.status_code == 200, f"Failed to create test user: {response.text}"
    
    yield test_user
    
    # Cleanup: Delete the user after test
    try:
        user_api.delete_user(test_user.username)
    except Exception as e:
        pytest.fail(f"Failed to cleanup test user: {str(e)}")

@pytest.fixture
def logged_in_user(user_api: UserEndpoints, created_user: User) -> Generator[User, None, None]:
    """
    Fixture that creates a user and logs them in.
    
    Args:
        user_api: UserEndpoints instance
        created_user: User instance that's already created
        
    Yields:
        Logged in User instance
    """
    # Log in the user
    response = user_api.login_user(created_user.username, created_user.password)
    assert response.status_code == 200, f"Failed to log in test user: {response.text}"
    
    yield created_user
    
    # Cleanup: Logout
    try:
        user_api.logout_user()
    except Exception as e:
        pytest.fail(f"Failed to logout test user: {str(e)}")
