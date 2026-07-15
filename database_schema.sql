CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(50)
);

CREATE TABLE warehouses(
    id INTEGER PRIMARY KEY,
    warehouse_name VARCHAR(100),
    location VARCHAR(150),
    manager_name VARCHAR(100),
    is_active BOOLEAN
);

CREATE TABLE products(
    id INTEGER PRIMARY KEY,
    product_name VARCHAR(100),
    sku VARCHAR(100) UNIQUE,
    stock_quantity INTEGER,
    unit_price FLOAT
);

CREATE TABLE transfers(
    id INTEGER PRIMARY KEY,
    from_warehouse INTEGER,
    to_warehouse INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    transfer_date DATE,
    status VARCHAR(50)
);
