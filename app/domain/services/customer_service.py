from app.adapters.models.session import get_db
from app.adapters.repository.customer_repository import SQLCustomerRepository
from app.domain.entities.customer import Customer
from app.domain.repositories.customer_repository import ICustomerRepository
from app.domain.services.exceptions import CpfAlreadyExists
from app.domain.services.exceptions import NotFound


class CustomerService:
    def __init__(self, customer_repository: ICustomerRepository):
        self.customer_repository = customer_repository

    def register_customer(self, customer: Customer) -> Customer:
        existing_customer = self.customer_repository.get_customer_by_cpf(customer.cpf)
        if existing_customer:
            raise CpfAlreadyExists("Customer with this CPF already exists.")
        return self.customer_repository.add_customer(customer)

    def get_customer(self, cpf: str) -> Customer:
        customer = self.customer_repository.get_customer_by_cpf(cpf)
        if not customer:
            raise NotFound("Customer with this CPF not found.")
        return customer


def get_customer_service() -> CustomerService:
    session = next(get_db())
    repository = SQLCustomerRepository(session=session)
    return CustomerService(repository)
