from abc import ABC
from abc import abstractmethod
from typing import Optional

from app.domain.entities.customer import Customer


class ICustomerRepository(ABC):
    @abstractmethod
    def add_customer(self, name: str, email: str, cpf: str) -> Customer:
        pass

    @abstractmethod
    def get_customer_by_cpf(self, cpf: str) -> Optional[Customer]:
        pass
