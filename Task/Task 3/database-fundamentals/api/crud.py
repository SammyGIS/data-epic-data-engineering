"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 07-03-2025

https://fastapi.tiangolo.com/tutorial/body-fields/#import-field
https://gerrysabar.medium.com/fastapi-simple-crud-with-mysql-sqlalchemy-e60dd04a5c7e
https://docs.sqlalchemy.org/en/14/orm/query.html
https://www.geeksforgeeks.org/sqlalchemy-core-joins/
"""

from sqlalchemy.orm import Session
from sqlalchemy import func
from database.model import Customer, Order, Product, OrderItem


def get_customers(db: Session):
    """get all customers"""
    return db.query(Customer.id, Customer.customer_id, Customer.gender)

def get_customer_by_id(db: Session, customer_id: str):
    """Get customer by customer_id"""
    return (
        db.query(Customer.id, Customer.customer_id, Customer.gender)
        .filter(Customer.customer_id == customer_id)
        .all()
    )


def get_order(db: Session):
    """get all orders"""
    return db.query(
        Order.order_id,
        Order.customer_id,
        Order.order_date,
        Order.order_priority,
        Order.payment_method,
        Order.device_type,
        Order.login_type,
    )


def get_order_by_id(db: Session, order_id: str):
    """get order by order_id"""
    return (
        db.query(
            Order.order_id,
            Order.customer_id,
            Order.order_date,
            Order.order_priority,
            Order.payment_method,
            Order.device_type,
            Order.login_type,
        )
        .filter(Order.order_id == order_id)
        .all()
    )


def get_all_products(db: Session):
    """get all products"""
    return db.query(Product.product_id, Product.product_category, Product.product_name)


def get_top_products(db: Session):
    """retrieve top-selling products based on order count."""
    return (
        db.query(
            OrderItem.product_id,
            Product.product_category,
            Product.product_name,
            func.count(OrderItem.product_id).label("total_count"),
        )
        .join(Product, Product.product_id == OrderItem.product_id)
        .group_by(OrderItem.product_id, Product.product_category, Product.product_name)
        .order_by(func.count(OrderItem.product_id).desc())
        .all()
    )


def get_revenues(db: Session):
    """get total revenue"""
    return db.query(
        func.sum(OrderItem.sales).label("total_sales"),
        func.sum(OrderItem.profit).label("total_profit"),
        func.sum(OrderItem.shipping_cost).label("total_shipping_cost"),
    ).all()
