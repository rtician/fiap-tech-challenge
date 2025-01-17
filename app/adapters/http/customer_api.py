from fastapi import APIRouter, Depends, HTTPException

from app.application.use_cases.customer_use_cases import CustomerUseCases
from app.application.exceptions import CpfAlreadyExists, NotFound
from app.domain.entities.customer import Customer, CustomerDb

router = APIRouter()

@router.post("", response_model=CustomerDb)
def register_customer(
    customer: Customer,
    use_cases: CustomerUseCases = Depends()
):
    try:
        return use_cases.register_customer(customer)
    except CpfAlreadyExists as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("", response_model=CustomerDb)
def get_customer_by_cpf(
    cpf: str,
    use_cases: CustomerUseCases = Depends()
):
    try:
        return use_cases.get_customer(cpf)
    except NotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
