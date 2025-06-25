# Data Engineering Internship Portfolio – Data Epic Foundation & Circle Fund

## Overview
This repository documents my four-month Data Engineering Internship at **Data Epic** and five-week externship at **Circle Fund**. It features six major data engineering projects, a production-grade capstone backend, and business-focused automation and analytics work.  
Each project was designed to strengthen my backend engineering, data pipeline, DevOps, and cloud deployment skills—culminating in the live deployment of a scalable API platform.

## Folder Structure
```bash
.
├── capstone-project/   # Capstone project code and docs
├── Externship/         # Work samples and scripts from Circle Fund externship
├── Materials/          # Reference materials, datasets, and documentation
├── Task/               # Six major internship tasks/projects with code and reports
└── Readme.md           # Project overview and documentation (this file)
```
---

## Table of Contents

1. [Internship Summary](#internship-summary)
2. [Project Highlights](#project-highlights)
    - [1. Weather Scraper API](#1-weather-scraper-api)
    - [2. Retail Data Processing API](#2-retail-data-processing-api)
    - [3. E-commerce Backend System](#3-e-commerce-backend-system)
    - [4. IMDB ETL Pipeline](#4-imdb-etl-pipeline)
    - [5. Stock Market Data Streaming & Analysis](#5-stock-market-data-streaming--analysis)
    - [6. Bikesharing ETL Pipeline](#6-bikesharing-etl-pipeline)
3. [Capstone Project – AI Agent Directory](#capstone-project--ai-agent-directory)
4. [Externship – Circle Fund](#externship--circle-fund)
5. [Technical Skills](#technical-skills)

---

## Internship Summary

**Duration:** Feb 2024 – Jun 2024  
**Company:** Data Epic (Internship), Circle Fund (Externship)  
**Focus:** End-to-end data engineering, backend APIs, ETL, cloud, and automation

- Delivered 6 diverse data engineering projects covering ETL pipelines, streaming analytics, real-time APIs, and dashboarding.
- Completed a capstone project: Designed, deployed, and documented a public backend API directory, using production-grade best practices.
- Supported business process automation and reporting during a 5-week externship at Circle Fund.

---

## Project Highlights

### 1. Weather Scraper API

- **Stack:** Python, FastAPI, BeautifulSoup, gspread, Google Sheets, Poetry
- **Description:** Built a FastAPI microservice to scrape weather data from web sources, clean it with regex, and automate updates to Google Sheets for real-time monitoring.
- **Features:** REST API, data cleaning, Google Sheets integration, Swagger docs, poetry environment management.
- **Impact:** Automated manual data collection for timely weather insights.

---

### 2. Retail Data Processing API

- **Stack:** Python, FastAPI, Pandas, Polars
- **Description:** Developed a FastAPI backend to process retail datasets, supporting ETL (extract, clean, transform) and multiple REST endpoints for analysts.
- **Features:** Download endpoints for JSON/Parquet, aggregation endpoints, error handling, interactive docs.
- **Impact:** Enabled analysts to quickly access clean, aggregated retail data for business reporting.

---

### 3. E-commerce Backend System

- **Stack:** PostgreSQL, SQLAlchemy, FastAPI, Python
- **Description:** Modeled a normalized relational schema for e-commerce transactions; built loaders and RESTful APIs for analytics (orders, customers, products, revenue, etc.).
- **Features:** SQL query optimization, database indexing, business intelligence endpoints, Swagger docs.
- **Impact:** Provided actionable business insights and real-time analytics for e-commerce use cases.

---

### 4. IMDB ETL Pipeline

- **Stack:** RapidAPI, Polars, Pandas, PostgreSQL, Poetry
- **Description:** Built a robust ETL pipeline to fetch, clean, and load movie data from the IMDB API, applying modular software engineering practices.
- **Features:** API data ingestion, data wrangling, entity relationship modeling, automated tests, modular ETL scripts.
- **Impact:** Demonstrated best practices in building maintainable, API-driven ETL pipelines for third-party data.

---

### 5. Stock Market Data Streaming & Analysis

- **Stack:** AWS (Lambda, Kinesis, S3, Glue, Athena), FastAPI, Metabase, Python, Boto3
- **Description:** Designed a cloud-native, serverless pipeline for streaming and transforming live stock market data, with storage, partitioning, and analytics in AWS and Metabase dashboards.
- **Features:** Event-driven ingestion, real-time processing, partitioned storage, automated metrics (price/volume), FastAPI endpoints.
- **Impact:** Demonstrated scalable architecture, real-time data handling, and dashboard-driven analytics.

---

### 6. Bikesharing ETL Pipeline

- **Stack:** Apache Airflow, Docker, MinIO, PostgreSQL, Metabase, Pandas, Polars
- **Description:** Built a full-stack, dockerized pipeline for ingesting and analyzing bikeshare trip data. Automated ETL with Airflow, partitioned Parquet storage, alerting, and Metabase visualizations.
- **Features:** Scheduled DAGs, real-time flagging, S3-compatible storage, interactive dashboards.
- **Impact:** Orchestrated complex workflows and enabled instant insight into bikesharing operations.

---

## Capstone Project – AI Agent Directory

**Project:** AI Agent Directory – Backend API  
**Live API:** [ai-agent-directory.onrender.com](https://ai-agent-directory.onrender.com)  
**Docs:** [Swagger](https://ai-agent-directory.onrender.com/docs) | [ReDoc](https://ai-agent-directory.onrender.com/redoc)

- **Role:** Designed, implemented, and deployed the backend for a public directory of AI agents and tools.
- **Stack:** FastAPI, PostgreSQL, Alembic, Docker, GitHub Actions (CI/CD), Pytest
- **Features:**
    - 20+ RESTful endpoints (user, agent, review, admin, highlight)
    - JWT-based authentication and role-based authorization
    - Admin controls for trending status
    - Ratings, reviews, highlights, user management
    - Modular, tested codebase with >20 backend tests
    - Dockerized deployment; live on Render.com
- **DevOps:** Integrated CI/CD with GitHub Actions for test, lint, and deploy automation.
- **Impact:** Delivered a production-grade, cloud-hosted API platform with automated documentation and robust testing.

---

## Externship – Circle Fund

**Duration:** 5 weeks  
**Role:** Data Engineering Extern

- **Metabase Dashboards:** Developed and maintained dashboards for business reporting and visualization.
- **Workflow Automation:** Automated withdrawals (Clearary Tasks) and built a notification system (Mailer Mail) for client status.
- **PDF Data Extraction:** Used PyMuPDF to extract, parse, and store banking statement data as JSON, integrating with an in-house scoring engine.
- **Impact:** Improved operational efficiency, reduced manual processing, and supported automated decision-making for credit and withdrawals.

---

## Technical Skills

**Languages:** Python, SQL  
**Frameworks:** FastAPI, Airflow, Docker, Alembic  
**Databases:** PostgreSQL, Google Sheets, MinIO (S3-compatible), Supabase  
**Libraries:** Pandas, Polars, BeautifulSoup, PyMuPDF, SQLAlchemy, Boto3  
**Cloud & DevOps:** AWS (Lambda, S3, Glue, Kinesis, Athena), Docker Compose, Render.com, GitHub Actions (CI/CD)  
**Data Visualization:** Metabase  
**Testing & QA:** Pytest, pre-commit hooks  
**Documentation:** Swagger/OpenAPI, ReDoc

