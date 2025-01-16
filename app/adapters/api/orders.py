from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.application.services.order_service import OrderService
from app.domain.entities.order import Order, OrderDb

router = APIRouter(prefix="/orders")

@router.post("", response_model=OrderDb)
def checkout(
    order: Order,
    service: OrderService = Depends()
):
    return service.add_order(order)

@router.get("/{order_id}", response_model=OrderDb)
def get_order(
    order_id: int,
    service: OrderService = Depends()
):
    order = service.get_order(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.get("", response_model=List[OrderDb])
def get_all_orders(service: OrderService = Depends()):
    return service.get_all_orders()
