from fastapi import FastAPI

from app.adapters.api import customer
from app.adapters.api import orders
from app.adapters.api import products

app = FastAPI()

app.include_router(customer.router)
app.include_router(products.router)
app.include_router(orders.router)
