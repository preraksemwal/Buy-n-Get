
create table accounts (
	username VARCHAR(50),
	email VARCHAR(50),
	password VARCHAR(50),
	customer_id INT
);

create table customers (
	customer_id INT,
	customer_name VARCHAR(50),
	age INT,
	gender VARCHAR(50),
	phone VARCHAR(50),
	country VARCHAR(50),
	state VARCHAR(50),
	street_name VARCHAR(50),
	street_no VARCHAR(50),
	pincode VARCHAR(50)
);

create table orders(
	order_id int primary key,
    item_id int,
    quantity int,
    customer_id int,
    foreign key(customer_id) references customers(customer_id)
);
