from typing import Optional

from sqlalchemy.orm import Session

from app.adapters.models import CustomerModel
from app.domain.repositories.customer_repository import ICustomerRepository
from app.domain.entities.customer import Customer


class SQLCustomerRepository(ICustomerRepository):
    def __init__(self, session: Session):
        self.session = session

    def add_customer(self, customer: Customer) -> Customer:
        instance = CustomerModel(**customer.model_dump())
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return Customer.from_orm(instance)

    def get_customer_by_cpf(self, cpf: str) -> Optional[Customer]:
        instance = self.session.query(CustomerModel).filter_by(cpf=cpf).first()
        return Customer.from_orm(instance) if instance else None
