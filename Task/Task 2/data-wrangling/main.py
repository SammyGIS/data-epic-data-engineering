"""
Author: Ajeyomi Adedoyin Samuel
Date: 01-03-2025
Email: adedoyinsamuel25@gmail.com

### **Task 5: API Integration**
"""
from fastapi import FastAPI
from api.api import router
import uvicorn


app = FastAPI(
    title="data wrangling",
    description="This API leverages both Pandas and Polars to efficiently perform ETL (Extract, Transform, Load) operations\
                and advanced data aggregation on retail datasets. It is designed to handle large-scale data processing\
                with high performance and flexibility.",
    version="1.0.0",
    contact={
        "name": "Adedoyin Samuel",
        "email": "adedoyinsamuel25@gmail.com",
    },
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)