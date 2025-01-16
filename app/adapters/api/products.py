from typing import List

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from app.application.services.product_service import ProductService
from app.domain.entities.product import Product, ProductCategory, ProductDb

router = APIRouter(prefix="/products")

@router.post("", response_model=ProductDb)
def add_product(
    product: Product,
    service: ProductService = Depends()
):
    return service.add_product(product)

@router.put("/{product_id}", response_model=ProductDb)
def update_product(
    product_id: int,
    product: Product,
    service: ProductService = Depends()
):
    updated_product = service.update_product(product_id, product)
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_id: int,
    service: ProductService = Depends()
):
    success = service.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {}

@router.get("", response_model=List[ProductDb])
def get_all_products(service: ProductService = Depends()):
    return service.get_all_products()

@router.get("/{category}", response_model=ProductDb)
def get_product_by_category(
    category: ProductCategory,
    service: ProductService = Depends()
):
    product = service.get_product_by_category(category)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
