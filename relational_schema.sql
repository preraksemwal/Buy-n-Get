CREATE TABLE owners(
	owner_id INT PRIMARY KEY,
	owner_name VARCHAR(50) NOT NULL,
	email UNIQUE VARCHAR(50) NOT NULL,
	password VARCHAR(50) NOT NULL CHECK(LENGTH(password) >= 12),
	phone_no UNIQUE VARCHAR(20)
);


CREATE TABLE accounts (
	username VARCHAR(50)  PRIMARY KEY,
	email VARCHAR(50) NOT NULL UNIQUE CHECK(POSITION("@" IN email) != 0),
	password VARCHAR(50) NOT NULL CHECK(LENGTH(password) >= 6),
	customer_id INT UNIQUE AUTO_INCREMENT
);

CREATE TABLE customers (
	customer_id INT PRIMARY KEY AUTO_INCREMENT,
	customer_name VARCHAR(50) NOT NULL,
	age INT CHECK(age >= 16),
	gender VARCHAR(50),
	phone VARCHAR(50) NOT NULL, 
	country VARCHAR(50) NOT NULL,
	state VARCHAR(50) NOT NULL,
	street_name VARCHAR(50) NOT NULL,
	street_no INT NOT NULL,
	pincode INT NOT NULL CHECK(pincode > 9999)
);


CREATE TABLE buyers(
	customer_id INT PRIMARY KEY,
	cart_id INT NOT NULL,
	FOREIGN KEY(cart_id) REFERENCES carts(cart_id)
);


CREATE TABLE carts(
	cart_id INT PRIMARY KEY AUTO_INCREMENT, 
	customer_id INT UNIQUE NOT NULL,
	items varchar(16000),
	FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);


CREATE TABLE orders(
	order_id INT PRIMARY KEY AUTO_INCREMENT,
    item_id INT NOT NULL,
    customer_id INT NOT NULL,
    quantity INT CHECK(quantity > 0),
    order_date DATE,
    delivery_date DATE,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY(item_id) REFERENCES items(item_id)
);


CREATE TABLE sellers(
	customer_id INT PRIMARY KEY,
	items_id VARCHAR(12000) NOT NULL,
);


CREATE TABLE items(
	item_id INT PRIMARY KEY,
	item_name VARCHAR(50) NOT NULL,
	item_type VARCHAR(20) NOT NULL,
	quantity INT CHECK(quantity > 0),
	price INT NOT NULL CHECK(price > 0),
);



