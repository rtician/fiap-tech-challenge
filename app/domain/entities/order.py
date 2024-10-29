from datetime import datetime
from typing import List

from pydantic import BaseModel


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
    created_at: datetime
    updated_at: datetime
    items: List[OrderItemDb]

    class Config:
        from_attributes = True
