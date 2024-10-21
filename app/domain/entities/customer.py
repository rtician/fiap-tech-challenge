from pydantic import BaseModel
from typing import Optional


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
