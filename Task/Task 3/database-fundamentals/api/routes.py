"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 07-03-2025


https://uriyyo-fastapi-pagination.netlify.app/#quickstart
https://fastapi.tiangolo.com/reference/apirouter/#fastapi.APIRouter


/GET	Get all customers
/customers/{customer_id}	GET	Get details of a specific customer
/orders/	GET	Get all orders
/orders/{order_id}	GET	Get details of a specific order
/products/	GET	Get all products
/analytics/top-products/	GET	Get top-selling products
/analytics/revenue/	GET	Get total revenue & profit
"""

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi_pagination import add_pagination, Params, Page
from fastapi_pagination.ext.sqlalchemy import paginate
from typing import List


import sys

sys.path.append("../")
from api.schema import Customer, Order, Product, AnalyticsTopProducts, AnalyticsRevenue
from database.db_setup import get_db
import api.crud as crud


router = APIRouter()


@router.get(
    "/customers",
    response_model=Page[Customer],
    description="Get all Customers with pagination",
    tags=["Customer"],
)
async def get_all_customers(db: Session = Depends(get_db), params: Params = Depends()):
    customers = crud.get_customers(db=db)
    if not customers:
        raise HTTPException(status_code=404, detail="No customers found")
    return paginate(customers, params)


@router.get(
    "/customers/{customer_id}",
    response_model=List[Customer],
    description="Get Customers by id",
    tags=["Customer"],
)
async def get_customers_by_id(customer_id: str, db: Session = Depends(get_db)):
    customers = crud.get_customer_by_id(db, customer_id)
    if not customers:
        raise HTTPException(
            status_code=404, detail=f"Customer with ID {customer_id} not found"
        )
    return customers


@router.get(
    "/orders",
    response_model=Page[Order],
    description="Get all Orders with pagination",
    tags=["Order"],
)
async def get_all_orders(db: Session = Depends(get_db), params: Params = Depends()):
    orders = crud.get_order(db=db)
    if not orders:
        raise HTTPException(status_code=404, detail="No orders found")
    return paginate(orders, params)


@router.get(
    "/orders/{order_id}",
    response_model=List[Order],
    description="Get Order by id",
    tags=["Order"],
)
async def get_order_by_id(order_id: int, db: Session = Depends(get_db)):
    orders = crud.get_order_by_id(db, order_id)
    if not orders:
        raise HTTPException(
            status_code=404, detail=f"Order with ID {order_id} not found"
        )
    return orders


@router.get(
    "/products",
    response_model=Page[Product],
    description="Get all Products with pagination",
    tags=["Product"],
)
async def get_all_products(db: Session = Depends(get_db), params: Params = Depends()):
    products = crud.get_all_products(db=db)
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    return paginate(products, params)


@router.get(
    "/analytics/top-products/",
    response_model=List[AnalyticsTopProducts],
    description="Get the list of the top selling products",
    tags=["Analytics"],
)
async def get_top5_selling_products(db: Session = Depends(get_db)):
    top5_selling_products = crud.get_top_products(db=db)
    if not top5_selling_products:
        raise HTTPException(status_code=404, detail="No top-selling products found")
    return top5_selling_products


@router.get(
    "/analytics/revenue",
    response_model=List[AnalyticsRevenue],
    description="Get total revenues",
    tags=["Analytics"],
)
async def get_revenue(db: Session = Depends(get_db)):
    total_revenue = crud.get_revenues(db=db)
    if not total_revenue:
        raise HTTPException(status_code=404, detail="No revenue data found")
    return total_revenue


add_pagination(router)
