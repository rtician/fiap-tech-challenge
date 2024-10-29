from abc import ABC
from abc import abstractmethod
from typing import List
from typing import Optional

from app.domain.entities.product import Product
from app.domain.entities.product import ProductCategory


class IProductRepository(ABC):
    @abstractmethod
    def add_product(
        self, name: str, description: str, category: ProductCategory, price: float, quantity: int
    ) -> Product:
        pass

    @abstractmethod
    def update_product(
        self,
        product_id: int,
        name: str,
        description: str,
        category: ProductCategory,
        price: float,
        quantity: int,
    ) -> Optional[Product]:
        pass

    @abstractmethod
    def delete_product(self, product_id: int) -> bool:
        pass

    @abstractmethod
    def get_all_products(self) -> List[Product]:
        pass

    @abstractmethod
    def get_product_by_category(self, category: ProductCategory) -> Optional[Product]:
        pass
