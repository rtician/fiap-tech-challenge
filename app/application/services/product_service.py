from typing import List
from typing import Optional

from app.adapters.models.session import get_db
from app.adapters.repository.product_repository import SQLProductRepository
from app.domain.entities.product import Product
from app.domain.entities.product import ProductCategory
from app.domain.entities.product import ProductRequest
from app.domain.repositories.product_repository import IProductRepository


class ProductService:
    def __init__(self, product_repository: IProductRepository):
        self.product_repository = product_repository

    def add_product(self, product: ProductRequest) -> Product:
        return self.product_repository.add_product(
            product.name, product.description, product.category, product.price, product.quantity
        )

    def update_product(self, product_id: int, product: ProductRequest) -> Optional[Product]:
        return self.product_repository.update_product(
            product_id,
            product.name,
            product.description,
            product.category,
            product.price,
            product.quantity,
        )

    def delete_product(self, product_id: int) -> bool:
        return self.product_repository.delete_product(product_id)

    def get_all_products(self) -> List[Product]:
        return self.product_repository.get_all_products()

    def get_product_by_category(self, category: ProductCategory) -> Optional[Product]:
        return self.product_repository.get_product_by_category(category)


def get_product_service() -> ProductService:
    session = next(get_db())
    repository = SQLProductRepository(session=session)
    return ProductService(repository)
