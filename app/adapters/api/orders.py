from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from app.application.services.order_service import OrderService
from app.application.services.order_service import get_order_service
from app.domain.entities.order import Order
from app.domain.entities.order import OrderDb

router = APIRouter(prefix="/orders")


@router.post("", response_model=OrderDb)
def checkout(order: Order, service: OrderService = Depends(get_order_service)):
    return service.add_order(order)


@router.get("/{order_id}", response_model=OrderDb)
def get_order(order_id: int, service: OrderService = Depends(get_order_service)):
    order = service.get_order(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Not found")
    return order


@router.get("", response_model=List[OrderDb])
def get_all_order(service: OrderService = Depends(get_order_service)):
    return service.get_all_orders()
