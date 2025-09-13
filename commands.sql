-- Active: 1729592285641@@127.0.0.1@3306
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    city VARCHAR(50) NOT NULL
);

CREATE TABLE products(
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    product_price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    order_date DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE TABLE order_items (
    order_id INT REFERENCES orders(order_id) ON DELETE CASCADE,
    product_id INT REFERENCES products(product_id),
    quantity INT CHECK (quantity > 0),
    PRIMARY KEY (order_id, product_id)
);

INSERT INTO customers (customer_name, email, city) VALUES
('Alice Johnson', 'alice@example.com', 'New York'),
('Bob Smith', 'bob@example.com', 'Los Angeles'),
('Charlie Brown', 'charlie@example.com', 'Chicago');

INSERT INTO orders (customer_id, order_date) VALUES
(1, '2023-10-01'),
(2, '2023-10-02'),
(1, '2023-10-03');


INSERT INTO products (product_name, product_price) VALUES
('Laptop', 100000),
('Smartphone', 50000),
('Tablet', 30000),
('Keyboard', 10000);

INSERT INTO order_items (order_id, product_id, quantity) VALUES
(1, 1, 1),
(1, 2, 2),
(2, 2, 1),
(3, 3, 3);


