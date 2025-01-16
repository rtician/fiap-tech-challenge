from sqlalchemy import Column, DateTime, Float, Integer, String, func
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
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), default=func.now())

    order_items = relationship("OrderItem", back_populates="product")
