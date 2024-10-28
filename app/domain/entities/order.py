from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

from app.domain.entities.product import Product


class OrderItem(BaseModel):
    product_id: int
    quantity: int
    product: Optional[Product] = None  # Include product details if needed

    class Config:
        from_attributes = True


class Order(BaseModel):
    id: Optional[int] = None
    customer_id: int
    date_created: Optional[datetime] = None
    items: List[OrderItem]

    class Config:
        from_attributes = True
