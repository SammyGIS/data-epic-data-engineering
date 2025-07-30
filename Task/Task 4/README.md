# **Project: API-Based ETL Pipeline with Polars or Pandas (IMDB via RapidAPI)**

## **Overview**
This project demonstrates how to build a robust, scalable, and maintainable ETL (Extract, Transform, Load) pipeline to fetch, transform, and load movie data from the IMDB API (via RapidAPI) into a database. The pipeline adheres to modern software engineering best practices, ensuring reliability, readability, and extensibility.

---

## **Project Requirements**
1. **Fetch data from the IMDB API** (via [RapidAPI](https://rapidapi.com/)).
2. **Parse and transform** the data using **Polars** (and optionally **Pandas**).
3. **Load** the cleaned data into a **database** (e.g., PostgreSQL or SQLite).
4. Adhere to **software engineering best practices**:
   - Automated testing with **pytest**.
   - Code formatting with **black**.
   - Type hints in Python.
   - **Poetry** for dependency management.

---

## **Project Structure**

The project is organized as follows:

```
etl_pipeline/
├── .gitignore
├── README.md
├── pyproject.toml
├── poetry.lock
├── env.example
├── database/
│   ├── __init__.py
│   ├── crud.py
│   ├── db_setup.py
│   ├── model.py
│   ├── utils.py
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── web_scraper.py
│   ├── data_transform.py
│   ├── db_loader.py
├── tests/
│   ├── __init__.py
│   ├── test_scraper.py
│   ├── test_transform.py
│   ├── test_db_loader.py
├── notebooks/
│   └── exploration.ipynb  # Optional for data exploration
├── data/
│   └── raw_data.json
│   └── processed_data.parquet
└── scripts/
    └── run_pipeline.py
```
---

## **Task Breakdown**

### **Task A: API Handling (IMDB via RapidAPI)**
1. **Sign up** for (or log in to) [RapidAPI](https://rapidapi.com/) and locate the **IMDB API** of your choice (e.g., IMDb Alternative API, IMDb – Official RapidAPI, or any that provides movie/TV show data).
2. **Fetch** data using the **IMDB API** endpoints (e.g., top 250 movies, search by keyword, get details by movie ID, etc.).
3. **Store your API key** securely (e.g., in an `.env` file) and **save** the raw response in the `data/` folder (JSON, CSV, etc.).
4. Handle **possible edge cases**:
   - Rate limits or request quotas.
   - Missing or incomplete data (e.g., movies without a release date).

### **Task B: Data Wrangling with Polars & Pandas**
1. **Load** the raw data into a **Polars** `DataFrame` (you may also demonstrate usage of **Pandas** if desired).
2. Perform **cleaning and transformation**:
   - Remove duplicates.
   - Handle missing values.
   - Parse dates, numeric columns, etc.
3. Create a **final** Polars `DataFrame` ready to be loaded into a database.
4. Save intermediate or final data as a `.parquet` or `.csv` file in `data/processed_data.parquet` (or `.csv`).

### **Task C: Database Fundamentals**
1. Use a **PostgreSQL** database.
2. Create your **entity relationship diagram (ERD)** and attach it to your README.
3. Define your database **models**.
4. Insert the cleaned data into your table.
   - Ensure you have your DB credentials set up (e.g., via a `.env` file).

### **Task D: Data Pipelines & ETL**
1. Combine **scraping → transformation → loading** steps in a single pipeline script (`scripts/run_pipeline.py`).
2. Ensure each step is modular:
   - `web_scraper.fetch_data()`
   - `data_transform.clean_data()`
   - `db_loader.load_data()`

---

## **Workflow**
![](https://github.com/Data-Epic/adedoyin-imdb-pipeline/blob/feat/etl-development/etl_pipeline/images/architecture.jpg)

---

## **Entity Relationship Diagram (ERD)**
![](https://github.com/Data-Epic/adedoyin-imdb-pipeline/blob/feat/etl-development/etl_pipeline/images/erd.png)

## **How to Run the Code**

1. Clone the repository:
   ```bash
   git clone https://github.com/Data-Epic/adedoyin-imdb-pipeline.git
   ```

2. Change to the development branch:
   ```bash
   git checkout feat/etl-development
   ```

3. Rename `env.example` to `.env` and provide all the required environment variables (e.g., API key, database credentials).

4. Install **pgAdmin** and **PostgreSQL** on your machine:
   - Open pgAdmin and create a new database named `imdb`.

   ![](https://github.com/Data-Epic/adedoyin-imdb-pipeline/blob/feat/etl-development/etl_pipeline/images/create_db.png)

5. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

6. Format the code using Black:
   ```bash
   poetry run black .
   ```
7. Start the Virtual Environment
   ```bash
   poetry shell
   ```

8. Run tests with pytest:
   ```bash
   pytest
   ```

9. Run the ETL pipeline:
   ```bash
   cd scripts
   poetry run python run_pipeline.py
   ```



---
## **Demo Video**
A short demo video of the project is available in the PR description.

