from typing import List

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from app.application.use_cases.product_use_cases import ProductUseCases
from app.domain.entities.product import Product, ProductCategory, ProductDb

router = APIRouter()

@router.post("", response_model=ProductDb)
def add_product(
    product: Product,
    use_cases: ProductUseCases = Depends()
):
    return use_cases.add_product(product)

@router.put("/{product_id}", response_model=ProductDb)
def update_product(
    product_id: int,
    product: Product,
    use_cases: ProductUseCases = Depends()
):
    updated_product = use_cases.update_product(product_id, product)
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_id: int,
    use_cases: ProductUseCases = Depends()
):
    success = use_cases.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {}

@router.get("", response_model=List[ProductDb])
def get_all_products(use_cases: ProductUseCases = Depends()):
    return use_cases.get_all_products()

@router.get("/{category}", response_model=ProductDb)
def get_product_by_category(
    category: ProductCategory,
    use_cases: ProductUseCases = Depends()
):
    product = use_cases.get_product_by_category(category)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
