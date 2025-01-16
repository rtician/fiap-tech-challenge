from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.application.use_cases.order_use_cases import OrderUseCases
from app.domain.entities.order import Order, OrderDb

router = APIRouter(prefix="/orders")

@router.post("", response_model=OrderDb)
def checkout(
    order: Order,
    use_cases: OrderUseCases = Depends()
):
    return use_cases.add_order(order)

@router.get("/{order_id}", response_model=OrderDb)
def get_order(
    order_id: int,
    use_cases: OrderUseCases = Depends()
):
    order = use_cases.get_order(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.get("", response_model=List[OrderDb])
def get_all_orders(use_cases: OrderUseCases = Depends()):
    return use_cases.get_all_orders()
