from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from app.domain.entities.customer import Customer
from app.domain.entities.customer import CustomerRequest
from app.domain.services.customer_service import CustomerService
from app.domain.services.customer_service import get_customer_service
from app.domain.services.exceptions import CpfAlreadyExists

router = APIRouter(prefix="/customers")


@router.post("", response_model=Customer)
def register_customer(
    customer_request: CustomerRequest, service: CustomerService = Depends(get_customer_service)
):
    customer = Customer(**customer_request.dict())
    try:
        return service.register_customer(customer)
    except CpfAlreadyExists as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("", response_model=Customer)
def get_customer_by_cpf(cpf: str, service: CustomerService = Depends(get_customer_service)):
    customer = service.get_customer(cpf)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer
