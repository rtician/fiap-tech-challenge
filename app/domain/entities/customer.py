from pydantic import BaseModel
from typing import Optional


class Customer(BaseModel):
    id: Optional[int] = None
    name: str
    cpf: str
    email: Optional[str] = None

    class Config:
        orm_mode = True
