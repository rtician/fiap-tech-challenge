from abc import ABC
from abc import abstractmethod
from typing import List

from app.domain.entities.order import Order
from app.domain.entities.order import OrderDb


class IOrderRepository(ABC):
    @abstractmethod
    def create_order(self, order: Order) -> OrderDb:
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
