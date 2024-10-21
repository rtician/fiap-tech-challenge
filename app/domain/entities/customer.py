from typing import Optional

from pydantic import BaseModel


class CustomerRequest(BaseModel):
    name: str
    cpf: str
    email: Optional[str] = None


class Customer(BaseModel):
    id: Optional[int] = None
    name: str
    cpf: str
    email: Optional[str] = None

    class Config:
        from_attributes = True
