from typing import List, Optional

from app.domain.entities.order import Order, OrderDb, OrderStatus
from app.domain.repositories.order_repository import IOrderRepository


class OrderUseCases:
    def __init__(self, order_repository: IOrderRepository):
        self.order_repository = order_repository

    def add_order(self, order: Order) -> OrderDb:
        return self.order_repository.add_order(order, status=OrderStatus.PLACED)

    def get_order(self, order_id: int) -> Optional[OrderDb]:
        return self.order_repository.get_order(order_id)

    def get_all_orders(self) -> List[OrderDb]:
        return self.order_repository.get_all_orders()
