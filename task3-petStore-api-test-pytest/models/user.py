from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    """User data model."""
    
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    id: Optional[int] = None
    userStatus: int = 1

    def to_dict(self) -> dict:
        """Convert user object to dictionary."""
        return {
            "id": self.id,
            "username": self.username,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "password": self.password,
            "phone": self.phone,
            "userStatus": self.userStatus
        }
