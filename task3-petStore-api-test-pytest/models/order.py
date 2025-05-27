from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Order:
    """Model representing a store order."""
    id: int
    petId: int
    quantity: int
    shipDate: str
    status: str
    complete: bool

    @classmethod
    def from_dict(cls, data: dict) -> 'Order':
        """Create an Order instance from a dictionary."""
        return cls(
            id=data['id'],
            petId=data['petId'],
            quantity=data['quantity'],
            shipDate=data['shipDate'],
            status=data['status'],
            complete=data['complete']
        )

    def to_dict(self) -> dict:
        """Convert Order instance to dictionary."""
        return {
            'id': self.id,
            'petId': self.petId,
            'quantity': self.quantity,
            'shipDate': self.shipDate,
            'status': self.status,
            'complete': self.complete
        }
