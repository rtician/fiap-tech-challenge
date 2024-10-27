from enum import Enum
from typing import Optional

from pydantic import BaseModel


class ProductCategory(str, Enum):
    MAIN_ITEM = "Main Item"
    SIDE = "Side"
    DRINK = "Drink"
    DESSERT = "Dessert"


class Product(BaseModel):
    id: Optional[int] = None
    name: str
    description: str
    category: str
    price: float
    quantity: int

    class Config:
        from_attributes = True
