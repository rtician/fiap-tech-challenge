from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.adapters.models.session import Base


class ProductModel(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    category = Column(String)
    price = Column(Float)
    quantity = Column(Integer)

    order_items = relationship("OrderModel", back_populates="product")
