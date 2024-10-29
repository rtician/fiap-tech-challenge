from enum import Enum

from pydantic import BaseModel


class ProductCategory(str, Enum):
    MAIN_ITEM = "Main Item"
    SIDE = "Side"
    DRINK = "Drink"
    DESSERT = "Dessert"


class ProductRequest(BaseModel):
    name: str
    description: str
    category: ProductCategory
    price: float
    quantity: int


class Product(BaseModel):
    id: int
    name: str
    description: str
    category: str
    price: float
    quantity: int

    class Config:
        from_attributes = True
