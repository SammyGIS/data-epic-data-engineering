"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 07-03-2025

https://fastapi.tiangolo.com/tutorial/body-fields/#import-field
"""
from pydantic import BaseModel, Field
from datetime import date


class Customer(BaseModel):
    id:int
    customer_id:str
    gender:str

    class config:
        from_attributes = True
        
class Order(BaseModel):
    order_id:int
    customer_id:int
    order_date:date
    order_priority:str
    payment_method:str
    device_type:str
    login_type:str


    class config:
        from_attributes = True

class Product(BaseModel):
    product_id:int
    product_category:str
    product_name:str

    class config:
        from_attributes = True

class AnalyticsTopProducts(BaseModel):
    product_id:int
    product_category:str
    product_name:str
    total_count:int

    class config:
        from_attributes = True

class AnalyticsRevenue(BaseModel):
    total_sales:float = Field(gt=0)
    total_profit:float = Field(gt=0)
    total_shipping_cost: float = Field(gt=0)

    class config:
        from_attributes = True
