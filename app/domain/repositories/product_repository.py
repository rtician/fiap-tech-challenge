from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.product import Product, ProductCategory, ProductDb


class IProductRepository(ABC):
    @abstractmethod
    def add_product(self, product: Product) -> ProductDb:
        pass

    @abstractmethod
    def update_product(self, product_id: int, product: Product) -> Optional[ProductDb]:
        pass

    @abstractmethod
    def delete_product(self, product_id: int) -> bool:
        pass

    @abstractmethod
    def get_all_products(self) -> List[ProductDb]:
        pass

    @abstractmethod
    def get_product_by_category(self, category: ProductCategory) -> Optional[ProductDb]:
        pass
