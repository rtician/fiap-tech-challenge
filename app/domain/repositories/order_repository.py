from abc import ABC, abstractmethod
from typing import List

from app.domain.entities.order import Order, OrderDb, OrderStatus


class IOrderRepository(ABC):
    @abstractmethod
    def add_order(self, order: Order, status: OrderStatus) -> OrderDb:
        pass

    @abstractmethod
    def cancel_order(self, order_id: int) -> bool:
        pass

    @abstractmethod
    def get_order(self, order_id: int) -> OrderDb:
        pass

    @abstractmethod
    def get_all_orders(self) -> List[OrderDb]:
        pass
