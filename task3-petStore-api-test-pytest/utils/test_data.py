from faker import Faker
import random
from typing import List
from models.user import User

fake = Faker()

class TestDataGenerator:
    """Utility class for generating test data."""
    
    @staticmethod
    def generate_user() -> User:
        """Generate a random user with fake data."""
        username = fake.user_name()
        return User(
            id=random.randint(1000, 9999),
            username=username,
            firstName=fake.first_name(),
            lastName=fake.last_name(),
            email=f"{username}@petstore.com",
            password=fake.password(),
            phone=fake.phone_number(),
            userStatus=1
        )
    
    @staticmethod
    def generate_users(count: int = 3) -> List[User]:
        """Generate multiple random users."""
        return [TestDataGenerator.generate_user() for _ in range(count)]
    
    @staticmethod
    def generate_invalid_user() -> User:
        """Generate an invalid user for negative testing."""
        return User(
            id=None,
            username="",
            firstName="",
            lastName="",
            email="invalid-email",
            password="",
            phone="invalid-phone",
            userStatus=999
        )
