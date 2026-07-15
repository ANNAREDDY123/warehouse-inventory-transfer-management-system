# warehouse-inventory-transfer-management-system
FastAPI Warehouse Inventory Transfer Management System with JWT Authentication, Warehouse Management, Product Management, Stock Transfer, Reports, Search, SQLAlchemy ORM, Pagination, Logging, Docker Support, and Unit Tests.
# Warehouse Inventory Transfer Management System

## Features

- JWT Authentication
- Warehouse Management (CRUD)
- Product Management
- Stock Transfer Management
- Inventory Reports
- Product Search
- SQLAlchemy ORM
- SQLite Database
- Docker Support
- Logging
- Basic Unit Tests



## Setup Instructions

### Install Dependencies

pip install -r requirements.txt


### Run Project


py -m uvicorn main:app --reload


Swagger


http://127.0.0.1:8000/docs


## Environment Variables

SECRET_KEY=warehouse_secret_key
ALGORITHM=HS256


## API Examples

- POST `/auth/register`
- POST `/auth/login`
- POST `/warehouses`
- POST `/products`
- POST `/transfers`


## Docker Deployment


docker build -t warehouse-system .
docker run -p 8000:8000 warehouse-system


## Assumptions

- SKU must be unique.
- Stock cannot go below zero.
- Source and destination warehouses cannot be the same.
- Cancelled transfers do not affect inventory.
