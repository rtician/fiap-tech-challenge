from typing import List, Optional

from app.domain.entities.product import Product, ProductCategory, ProductDb
from app.domain.repositories.product_repository import IProductRepository


class ProductService:
    def __init__(self, product_repository: IProductRepository):
        self.product_repository = product_repository

    def add_product(self, product: Product) -> ProductDb:
        return self.product_repository.add_product(product)

    def update_product(self, product_id: int, product: Product) -> Optional[ProductDb]:
        return self.product_repository.update_product(product_id, product)

    def delete_product(self, product_id: int) -> bool:
        return self.product_repository.delete_product(product_id)

    def get_all_products(self) -> List[ProductDb]:
        return self.product_repository.get_all_products()

    def get_product_by_category(self, category: ProductCategory) -> Optional[ProductDb]:
        return self.product_repository.get_product_by_category(category)
