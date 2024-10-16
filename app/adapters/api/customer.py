from fastapi import APIRouter, Depends
from app.domain.entities.customer import Customer
from app.domain.services.customer_service import CustomerService

router = APIRouter()


@router.post("/customers", response_model=Customer)
def register_customer(customer: Customer, service: CustomerService = Depends()):
    return service.register_customer(customer)
