"""
Author: Ajeyomi Adedoyin Samuel
Date: 01-03-2025
Email: adedoyinsamuel25@gmail.com

### **Task 5: API Integration**
4. Expose results via a FastAPI endpoint (`/aggregate`).
1. Create a `/process-data` endpoint.
2. This endpoint should:
   - Load dataset
   - Clean and aggregate data
   - Return processed results in JSON format.
3. Implement error handling for invalid input formats.
1. Save processed data in **JSON** and **Parquet** formats.
2. Implement API endpoints to download these files (`/download-json`, `/download-parquet`).

https://fastapi.tiangolo.com/tutorial/query-params/
"""
import sys 
# Set all dependencies (module) part
sys.path.append('../')
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from processor.aggregate import PolarsAggregation, PandasAggregation
from processor.clean import pd_transform_data, pl_transform_data
from processor.utils import pl_download_data, pd_download_data
from processor.load_data import download_extract_zip_file
from api.config import URL

# Access data
data_path = download_extract_zip_file(URL, "online_retail.zip")

# Transformed data using both pandas and polars
pd_transformed_data = pd_transform_data(data_path)
pl_transformed_data = pl_transform_data(data_path)
pandas_agg = PandasAggregation(pd_transformed_data)
polars_agg = PolarsAggregation(pl_transformed_data)

# Set API router
router = APIRouter()

# Get processed data
@router.get("/processed_data/", tags=["Pandas"])
async def pd_get_processed_data(skip: int = 0, limit: int = 20):
    json_compatible_item_data = jsonable_encoder(pd_transformed_data)
    return JSONResponse(content=json_compatible_item_data[skip: skip + limit])

@router.get("/pl_processed_data/", tags=["Polars"])
async def pl_get_processed_data(skip: int = 0, limit: int = 20):
    json_compatible_item_data = jsonable_encoder(pl_transformed_data)
    return JSONResponse(content=json_compatible_item_data[skip: skip + limit])

# Download data using pandas
@router.get("/download-json/", tags=["Pandas"])
async def pd_download_json():
    pd_download_data("json")
    return {"message": "Saved successfully!"}

@router.get("/download-parquet/", tags=["Pandas"])
async def pd_download_parquet():
    pd_download_data("parquet")
    return {"message": "Saved successfully!"}

# Download data using polars
@router.get("/pl_download-json/", tags=["Polars"])
async def pl_download_json():
    pl_download_data("json")
    return {"message": "Saved successfully!"}

@router.get("/pl_download-parquet/", tags=["Polars"])
async def pl_download_parquet():
    pl_download_data("parquet")
    return {"message": "Saved successfully!"}

# Get aggregate using pandas
@router.get("/aggregate/transaction_per_country", tags=["Pandas"])
async def pd_get_transaction_per_country(skip: int = 0, limit: int = 20):
    data = pandas_agg.pd_transaction_per_country()
    json_compatible_item_data = jsonable_encoder(data[skip: skip + limit])
    return JSONResponse(content=json_compatible_item_data)

@router.get("/aggregate/transaction_revenue_per_country", tags=["Pandas"])
async def pd_get_transaction_revenue_per_country(skip: int = 0, limit: int = 20):
    data = pandas_agg.pd_transaction_revenue_per_country()
    json_compatible_item_data = jsonable_encoder(data[skip: skip + limit])
    return JSONResponse(content=json_compatible_item_data)

@router.get("/aggregate/unique_customers_per_country", tags=["Pandas"])
async def pd_get_unique_customers_per_country(skip: int = 0, limit: int = 20):
    data = pandas_agg.pd_unique_customers_per_country()
    json_compatible_item_data = jsonable_encoder(data[skip: skip + limit])
    return JSONResponse(content=json_compatible_item_data)

@router.get("/aggregate/average_order_value_per_country", tags=["Pandas"])
async def pd_get_average_order_value_per_country(skip: int = 0, limit: int = 20):
    data = pandas_agg.pd_average_order_value_per_country()
    json_compatible_item_data = jsonable_encoder(data[skip: skip + limit])
    return JSONResponse(content=json_compatible_item_data)

# Get aggregate using polars
@router.get("/aggregate/pl_transaction_per_country", tags=["Polars"])
async def pl_get_transaction_per_country(skip: int = 0, limit: int = 20):
    data = polars_agg.pl_transaction_per_country()
    json_compatible_item_data = jsonable_encoder(data[skip: skip + limit])
    return JSONResponse(content=json_compatible_item_data)

@router.get("/aggregate/pl_transaction_revenue_per_country", tags=["Polars"])
async def pl_get_transaction_revenue_per_country(skip: int = 0, limit: int = 20):
    data = polars_agg.pl_transaction_revenue_per_country()
    json_compatible_item_data = jsonable_encoder(data[skip: skip + limit])
    return JSONResponse(content=json_compatible_item_data)

@router.get("/aggregate/pl_unique_customers_per_country", tags=["Polars"])
async def pl_get_unique_customers_per_country(skip: int = 0, limit: int = 20):
    data = polars_agg.pl_unique_customers_per_country()
    json_compatible_item_data = jsonable_encoder(data[skip: skip + limit])
    return JSONResponse(content=json_compatible_item_data)

@router.get("/aggregate/pl_average_order_value_per_country", tags=["Polars"])
async def pl_get_average_order_value_per_country(skip: int = 0, limit: int = 20):
    data = polars_agg.pl_average_order_value_per_country()
    json_compatible_item_data = jsonable_encoder(data[skip: skip + limit])
    return JSONResponse(content=json_compatible_item_data)
