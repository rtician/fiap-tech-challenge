from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel


class OrderStatus(str, Enum):
    PLACED = "Order placed"
    CONFIRMED = "Order confirmed"
    PREPARING = "Preparing"
    READY_FOR_PICKUP = "Ready for pickup"
    OUT_FOR_DELIVERY = "Out for delivery"
    DELIVERED = "Delivered"
    CANCELED = "Canceled"
    REFUNDED = "Refunded"


class OrderItem(BaseModel):
    product_id: int
    quantity: int


class OrderItemDb(OrderItem):
    id: int
    order_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Order(BaseModel):
    customer_id: int
    items: List[OrderItem]


class OrderDb(Order):
    id: int
    status: OrderStatus
    created_at: datetime
    updated_at: datetime
    items: List[OrderItemDb]

    class Config:
        from_attributes = True
