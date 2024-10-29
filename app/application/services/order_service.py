from typing import List
from typing import Optional

from app.adapters.models.session import get_db
from app.adapters.repository.order_repository import SQLOrderRepository
from app.domain.entities.order import Order
from app.domain.entities.order import OrderDb
from app.domain.entities.order import OrderStatus
from app.domain.repositories.order_repository import IOrderRepository


class OrderService:
    def __init__(self, order_repository: IOrderRepository):
        self.order_repository = order_repository

    def add_order(self, order: Order) -> OrderDb:
        return self.order_repository.add_order(order, status=OrderStatus.PLACED)

    def get_order(self, order_id: int) -> Optional[OrderDb]:
        return self.order_repository.get_order(order_id)

    def get_all_orders(self) -> List[OrderDb]:
        return self.order_repository.get_all_orders()


def get_order_service() -> OrderService:
    session = next(get_db())
    repository = SQLOrderRepository(session=session)
    return OrderService(repository)
