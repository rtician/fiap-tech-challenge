from datetime import datetime, UTC

from sqlalchemy import Column, ForeignKey, DateTime
from sqlalchemy import Integer
from sqlalchemy.orm import relationship

from app.adapters.models.session import Base


class OrderModel(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey(""))
    created = Column(DateTime, default=datetime.now(UTC))

    customer = relationship("CustomerModel", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("order.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    quantity = Column(Integer, nullable=False)

    order = relationship("OrderModel", back_populates="items")
    product = relationship("ProductModel", back_populates="items")
