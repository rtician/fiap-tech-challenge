from typing import List, Optional

from app.adapters.models.session import get_db
from app.adapters.repositories.order_repository import SQLOrderRepository
from app.domain.entities.order import (
    Order,
    OrderDb,
    OrderStatus,
    PaymentStatus
)
from app.domain.repositories.order_repository import IOrderRepository


class OrderUseCases:
    def __init__(self, order_repository: IOrderRepository):
        self.order_repository = order_repository

    def checkout_order(self, order: Order) -> OrderDb:
        return self.order_repository.add_order(order, status=OrderStatus.PLACED)

    def cancel_order(self, order_id: int) -> bool:
        return self.order_repository.cancel_order(order_id)

    def get_payment_status(self, order_id: int) -> PaymentStatus:
        order_db = self.order_repository.get_order(order_id)
        if not order_db:
            #TODO: Should raise a NotFound?
            return PaymentStatus.DENIED
        return order_db.payment_status

    def update_payment_status(self, order_id: int, status: PaymentStatus) -> Optional[OrderDb]:
        return self.order_repository.update_payment_status(order_id, status)

    def update_order_status(self, order_id: int, status: OrderStatus) -> Optional[OrderDb]:
        return self.order_repository.update_order_status(order_id, status)

    def get_order(self, order_id: int) -> Optional[OrderDb]:
        return self.order_repository.get_order(order_id)

    def get_all_orders(self) -> List[OrderDb]:
        return self.order_repository.get_all_orders()

    def get_filtered_orders(self) -> List[OrderDb]:
        return self.order_repository.get_filtered_orders()


def get_order_use_case() -> OrderUseCases:
    session = next(get_db())
    repository = SQLOrderRepository(session=session)
    return OrderUseCases(repository)
