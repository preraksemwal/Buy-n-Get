

CREATE TABLE owners(
	owner_id INT PRIMARY KEY,
	owner_name VARCHAR(50) NOT NULL,
	email VARCHAR(50) UNIQUE NOT NULL CHECK(POSITION("@" IN email) != 0),
	password VARCHAR(50) NOT NULL CHECK(LENGTH(password) >= 12),
	phone_no VARCHAR(20) UNIQUE NOT NULL
);


CREATE TABLE accounts (
	username VARCHAR(50) PRIMARY KEY,
	email VARCHAR(50) NOT NULL UNIQUE CHECK(POSITION("@" IN email) != 0),
	password VARCHAR(50) NOT NULL CHECK(LENGTH(password) >= 6),
	customer_id INT UNIQUE AUTO_INCREMENT
);

CREATE TABLE customers (
	customer_id INT PRIMARY KEY AUTO_INCREMENT,
	customer_name VARCHAR(50) NOT NULL,
	age INT CHECK(age >= 16),
	gender VARCHAR(50),
	phone_no VARCHAR(50) NOT NULL, 
	country VARCHAR(50) NOT NULL,
	state VARCHAR(50) NOT NULL,
	street_name VARCHAR(50) NOT NULL,
	street_no INT NOT NULL,
	pincode VARCHAR(5) NOT NULL
);



CREATE TABLE carts(
	cart_id INT PRIMARY KEY AUTO_INCREMENT, 
	customer_id INT UNIQUE NOT NULL,
	items varchar(16000)             
);


CREATE TABLE buyers(
	customer_id INT PRIMARY KEY,
	cart_id INT NOT NULL,
	FOREIGN KEY(cart_id) REFERENCES carts(cart_id),
    	FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);



CREATE TABLE orders(
	order_id INT PRIMARY KEY AUTO_INCREMENT,
    	item_id INT NOT NULL,
    	customer_id INT NOT NULL,
    	quantity INT CHECK(quantity > 0),
    	order_date DATE NOT NULL,
    	delivery_date DATE NOT NULL,
    	FOREIGN KEY(customer_id) REFERENCES buyers(customer_id)
);


CREATE TABLE sellers(
	customer_id INT PRIMARY KEY,
	items_id VARCHAR(12000) NOT NULL,
    	FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);


CREATE TABLE items(
	item_id INT PRIMARY KEY AUTO_INCREMENT,
	item_name VARCHAR(50) NOT NULL,
	item_type VARCHAR(20) NOT NULL,
	quantity INT CHECK(quantity > 0),
	cost_price FLOAT NOT NULL CHECK(cost_price > 0),
	selling_price FLOAT NOT NULL CHECK(selling_price > 0)
);


CREATE TABLE feedback(
	customer_id INT PRIMARY KEY,
	rating INT CHECK(stars_rate BETWEEN 1 AND 5)
);


CREATE TABLE support(
	support_id INT PRIMARY KEY AUTO_INCREMENT,
	customer_id INT,
	issue VARCHAR(1000)
);



CREATE TABLE payments(
	payment_id INT PRIMARY KEY AUTO_INCREMENT,
	customer_id INT NOT NULL,
	mode VARCHAR(20) NOT NULL,
	amount INT NOT NULL	
);

CREATE TABLE transactions(
	transaction_id INT PRIMARY KEY AUTO_INCREMENT,
	order_id INT NOT NULL,
	customer_id INT NOT NULL,
	mode VARCHAR(20) NOT NULL,
	amount INT NOT NULL		
);
