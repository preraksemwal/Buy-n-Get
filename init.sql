
create table accounts(
	username varchar(50) unique primary key,
    password varchar(50),
    email varchar(50),
    customer_id int
);

create table customer(
	customer_id int primary key,
    customer_name varchar(100),
    age int,
    gender varchar(20),
    phone_no varchar(15),
    country varchar(30),
    state varchar(60),
    street_name varchar(50),
    street_no int,
    pincode int
);

create table orders(
	order_id int primary key,
    item_id int,
    quantity int,
    customer_id int,
    foreign key(customer_id) references customers(customer_id)
);
