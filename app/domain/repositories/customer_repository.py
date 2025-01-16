from abc import ABC, abstractmethod
from typing import Optional

from app.domain.entities.customer import Customer, CustomerDb


class ICustomerRepository(ABC):
    @abstractmethod
    def add_customer(self, customer: Customer) -> CustomerDb:
        pass

    @abstractmethod
    def get_customer_by_cpf(self, cpf: str) -> Optional[CustomerDb]:
        pass
