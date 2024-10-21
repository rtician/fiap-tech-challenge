from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.adapters.models.session import Base


class CustomerModel(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    cpf = Column(String, index=True)
    email = Column(String)
