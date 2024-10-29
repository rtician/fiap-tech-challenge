from typing import List
from typing import Optional

from sqlalchemy.orm import Session

from app.adapters.models import ProductModel
from app.domain.entities.product import Product
from app.domain.entities.product import ProductCategory
from app.domain.repositories.product_repository import IProductRepository


class SQLProductRepository(IProductRepository):
    def __init__(self, session: Session):
        self.session = session

    def add_product(
        self, name: str, description: str, category: ProductCategory, price: float, quantity: int
    ) -> Product:
        db_product = ProductModel(
            name=name,
            description=description,
            category=category.value,
            price=price,
            quantity=quantity,
        )
        self.session.add(db_product)
        self.session.commit()
        self.session.refresh(db_product)
        return Product.from_orm(db_product)

    def update_product(
        self,
        product_id: int,
        name: str,
        description: str,
        category: ProductCategory,
        price: float,
        quantity: int,
    ) -> Optional[Product]:
        db_product = self.session.query(ProductModel).filter_by(id=product_id).first()
        if db_product:
            db_product.name = name
            db_product.description = description
            db_product.category = category.value
            db_product.price = price
            db_product.quantity = quantity
            self.session.commit()

            return Product.from_orm(db_product)

    def delete_product(self, product_id: int) -> bool:
        db_product = self.session.query(ProductModel).filter_by(id=product_id).first()
        if not db_product:
            return False
        self.session.delete(db_product)
        self.session.commit()
        return True

    def get_all_products(self) -> List[Product]:
        return [Product.from_orm(instance) for instance in self.session.query(ProductModel).all()]

    def get_product_by_category(self, category: ProductCategory) -> Optional[Product]:
        instance = self.session.query(ProductModel).filter_by(category=category.value).first()
        return Product.from_orm(instance) if instance else None
