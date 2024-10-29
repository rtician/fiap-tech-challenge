from typing import List

from sqlalchemy.orm import Session

from app.adapters.models import OrderModel
from app.domain.entities.order import Order
from app.domain.entities.order import OrderDb
from app.domain.entities.order import OrderStatus
from app.domain.repositories.order_repository import IOrderRepository


class SQLOrderRepository(IOrderRepository):
    def __init__(self, session: Session):
        self.session = session

    def add_order(self, order: Order, status: OrderStatus) -> OrderDb:
        instance = OrderModel(**order.model_dump(), status=status)
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return OrderDb.from_orm(instance)

    def cancel_order(self, order_id: int) -> bool:
        raise NotImplementedError

    def get_order(self, order_id: int) -> OrderDb:
        instance = self.session.query(OrderModel).filter_by(id=order_id).first()
        return OrderDb.from_orm(instance) if instance else None

    def get_all_orders(self) -> List[OrderDb]:
        instances = self.session.query(OrderModel).all()
        return [OrderDb.from_orm(instance) for instance in instances]
