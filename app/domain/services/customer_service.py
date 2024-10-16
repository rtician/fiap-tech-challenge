from app.domain.repositories.customer_repository import ICustomerRepository
from app.domain.entities.customer import Customer


class CustomerService:
    def __init__(self, customer_repository: ICustomerRepository):
        self.customer_repository = customer_repository

    def register_customer(self, customer: Customer) -> Customer:
        existing_customer = self.customer_repository.get_customer_by_cpf(customer.cpf)
        if existing_customer:
            raise ValueError("Customer with this CPF already exists.")
        return self.customer_repository.add_customer(customer)
