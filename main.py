from fastapi import Depends
from fastapi import FastAPI

# HTTP (FastAPI) Routers
from app.adapters.http.customer_api import router as customer_router
from app.adapters.http.orders_api import router as order_router
from app.adapters.http.products_api import router as product_router

# ORM session for DB
from app.adapters.models.session import get_db

# Concrete Repositories (SQLAlchemy)
from app.adapters.repositories.customer_repository import SQLCustomerRepository
from app.adapters.repositories.order_repository import SQLOrderRepository
from app.adapters.repositories.product_repository import SQLProductRepository

# Service / Use Cases
from app.application.use_cases.customer_use_cases import CustomerUseCases
from app.application.use_cases.order_use_cases import OrderUseCases
from app.application.use_cases.product_use_cases import ProductUseCases


# Dependency factories
def get_customer_use_cases(db=Depends(get_db)):
    repo = SQLCustomerRepository(session=db)
    return CustomerUseCases(customer_repository=repo)


def get_order_use_cases(db=Depends(get_db)):
    repo = SQLOrderRepository(session=db)
    return OrderUseCases(order_repository=repo)


def get_product_use_cases(db=Depends(get_db)):
    repo = SQLProductRepository(session=db)
    return ProductUseCases(product_repository=repo)


app = FastAPI()

app.include_router(
    customer_router,
    prefix="/customers",
    tags=["customers"],
    dependencies=[Depends(get_customer_use_cases)],
)

app.include_router(
    order_router, prefix="/orders", tags=["orders"], dependencies=[Depends(get_order_use_cases)]
)

app.include_router(
    product_router,
    prefix="/products",
    tags=["products"],
    dependencies=[Depends(get_product_use_cases)],
)
