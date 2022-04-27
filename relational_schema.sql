
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
	customer_id INT UNIQUE NOT NULL AUTO_INCREMENT
);

CREATE TABLE customers (
	customer_id INT PRIMARY KEY,
	customer_name VARCHAR(50) NOT NULL,
	age INT CHECK(age >= 16),
	gender VARCHAR(50),
	phone_no VARCHAR(50) NOT NULL, 
	country VARCHAR(50) NOT NULL,
	state VARCHAR(50) NOT NULL,
	street_name VARCHAR(50) NOT NULL,
	street_no INT NOT NULL,
	pincode VARCHAR(5) NOT NULL,
	FOREIGN KEY(customer_id) REFERENCES accounts(customer_id) ON DELETE CASCADE
);



CREATE TABLE buyers(
	customer_id INT PRIMARY KEY,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

CREATE TABLE carts(
	cart_id INT PRIMARY KEY AUTO_INCREMENT, 
	customer_id INT UNIQUE NOT NULL,
	FOREIGN KEY(customer_id) REFERENCES buyers(customer_id) ON DELETE CASCADE    
);

CREATE TABLE stores(
	cart_id INT NOT NULL, 
	item_id INT NOT NULL,
	quantity INT NOT NULL,
	FOREIGN KEY(cart_id) REFERENCES carts(cart_id) ON DELETE CASCADE        
);



CREATE TABLE items(
	item_id INT PRIMARY KEY AUTO_INCREMENT,
	item_name VARCHAR(50) NOT NULL,
	item_type VARCHAR(20) NOT NULL,
	quantity INT CHECK(quantity > 0),
	cost_price FLOAT NOT NULL CHECK(cost_price > 0),
	selling_price FLOAT NOT NULL CHECK(selling_price > 0)
);


CREATE TABLE orders(
	order_id INT PRIMARY KEY AUTO_INCREMENT,
	customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    delivery_date DATE NOT NULL,
    FOREIGN KEY(customer_id) REFERENCES buyers(customer_id) ON DELETE CASCADE
);

CREATE TABLE ordered_items(
	order_id INT NOT NULL,
	item_id INT NOT NULL,
    quantity INT CHECK(quantity > 0),
    FOREIGN KEY(order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY(item_id) REFERENCES items(item_id) ON DELETE CASCADE
);




CREATE TABLE sellers(
	customer_id INT PRIMARY KEY,
	FOREIGN KEY(customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

CREATE TABLE sells(
	customer_id INT NOT NULL,
	item_id INT NOT NULL,
	FOREIGN KEY(customer_id) REFERENCES sellers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY(item_id) REFERENCES items(item_id) ON DELETE CASCADE
);



CREATE TABLE feedback(
	customer_id INT PRIMARY KEY,
	rating INT CHECK(rating BETWEEN 1 AND 5),
	FOREIGN KEY(customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

CREATE TABLE support(
	support_id INT PRIMARY KEY AUTO_INCREMENT,
	customer_id INT,
	issue VARCHAR(1000),
	issue_date date,
	FOREIGN KEY(customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

CREATE TABLE payments(
	payment_id INT PRIMARY KEY AUTO_INCREMENT,
	customer_id INT NOT NULL,
	mode VARCHAR(20) NOT NULL,
	amount INT NOT NULL	,
	FOREIGN KEY(customer_id) REFERENCES sellers(customer_id) ON DELETE CASCADE
);

CREATE TABLE transactions(
	order_id INT PRIMARY KEY,
	customer_id INT NOT NULL,
	mode VARCHAR(20) NOT NULL,
	amount INT NOT NULL,
	FOREIGN KEY(customer_id) REFERENCES buyers(customer_id) ON DELETE CASCADE,
	#FOREIGN KEY(order_id) REFERENCES orders(order_id) ON DELETE CASCADE
);
