from abc import ABC
from abc import abstractmethod
from typing import List

from app.adapters.models import OrderModel
from app.domain.entities.order import Order


class IOrderRepository(ABC):
    @abstractmethod
    def create_order(self, order: Order) -> OrderModel:
        pass

    @abstractmethod
    def cancel_order(self, order_id: int) -> bool:
        pass

    @abstractmethod
    def get_order(self, order_id: int) -> OrderModel:
        pass

    @abstractmethod
    def get_all_orders(self) -> List[OrderModel]:
        pass
