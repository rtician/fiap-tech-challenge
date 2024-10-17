from typing import Optional

from fastapi import Depends
from sqlalchemy.orm import Session

from app.adapters.models.session import get_db
from app.domain.repositories.customer_repository import ICustomerRepository
from app.domain.entities.customer import Customer


class SQLCustomerRepository(ICustomerRepository):
    def __init__(self, session: Session):
        self.session = session

    def add_customer(self, customer: Customer) -> Customer:
        self.session.add(customer)
        self.session.commit()
        self.session.refresh(customer)
        return customer

    def get_customer_by_cpf(self, cpf: str) -> Optional[Customer]:
        return self.session.query(Customer).filter_by(cpf=cpf).first()


def get_customer_repository(session: Session = Depends(get_db)) -> SQLCustomerRepository:
    return SQLCustomerRepository(sesson=session)
