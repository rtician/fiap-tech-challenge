from typing import Optional

from app.adapters.db.session import db_session
from app.domain.repositories.customer_repository import ICustomerRepository
from app.domain.entities.customer import Customer


class SQLCustomerRepository(ICustomerRepository):
    def add_customer(self, customer: Customer) -> Customer:
        db_session.add(customer)
        db_session.commit()
        db_session.refresh(customer)
        return customer

    def get_customer_by_cpf(self, cpf: str) -> Optional[Customer]:
        return db_session.query(Customer).filter_by(cpf=cpf).first()
