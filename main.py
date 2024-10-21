from fastapi import FastAPI

from app.adapters.api import customer

app = FastAPI()

app.include_router(customer.router)
