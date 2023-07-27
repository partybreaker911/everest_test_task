from enum import Enum


class DeliveryStatus(Enum):
    PENDING = "Pending"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"
