
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
	FOREIGN KEY(customer_id) REFERENCES buyers(customer_id) ON DELETE CASCADE
	#FOREIGN KEY(order_id) REFERENCES orders(order_id) ON DELETE CASCADE
);







CREATE VIEW owners_info AS
SELECT owner_name AS Name, email 
FROM owners;

CREATE VIEW accounts_info AS
SELECT username, email 
FROM accounts;

CREATE VIEW customers_info AS 
SELECT customer_name, gender, phone_no, country, state, street_name, street_no, pincode
FROM customers;

CREATE VIEW items_info AS
SELECT item_id, item_name, item_type, quantity, selling_price
FROM items;




CREATE ROLE ownit;

GRANT SELECT ON owners_info TO ownit;
GRANT SELECT ON customers TO ownit;
GRANT DELETE ON accounts TO ownit;
GRANT SELECT ON accounts_info TO ownit;
GRANT SELECT ON sellers TO ownit;
GRANT SELECT ON buyers TO ownit;
GRANT ALL ON items TO ownit;
GRANT SELECT ON orders TO ownit;
GRANT SELECT ON ordered_items TO ownit;
GRANT SELECT ON support TO ownit;
GRANT SELECT, DELETE ON feedback TO ownit;
GRANT SELECT ON payments TO ownit;
GRANT SELECT ON transactions TO ownit;
GRANT SELECT ON sells TO ownit;

CREATE USER owner1@localhost IDENTIFIED BY 'prerak';
CREATE USER owner2@localhost IDENTIFIED BY 'vineet';
CREATE USER owner3@localhost IDENTIFIED BY 'janhavi';
CREATE USER owner4@localhost IDENTIFIED BY 'abhinav';

GRANT ownit TO owner1@localhost;
GRANT ownit TO owner2@localhost;
GRANT ownit TO owner3@localhost;
GRANT ownit TO owner4@localhost;



CREATE ROLE buyit;
 
GRANT SELECT ON owners_info TO buyit;
GRANT UPDATE ON customers_info TO buyit;
GRANT SELECT ON transactions TO buyit;
GRANT ALL ON support TO buyit;
GRANT SELECT ON items TO buyit;

CREATE USER buyer1@localhost IDENTIFIED BY 'buyer1';
CREATE USER buyer2@localhost IDENTIFIED BY 'buyer2';

GRANT buyit TO buyer1@localhost;
GRANT buyit TO buyer2@localhost;




CREATE ROLE sellit;
 
GRANT SELECT ON owners_info TO sellit;
GRANT UPDATE ON customers_info TO sellit;
GRANT SELECT ON payments TO sellit;
GRANT ALL ON support TO sellit;
GRANT SELECT ON items TO sellit;

CREATE USER seller1@localhost IDENTIFIED BY 'seller1';
CREATE USER seller2@localhost IDENTIFIED BY 'seller2';

GRANT sellit TO seller1@localhost;
GRANT sellit TO seller2@localhost;








# if age is NULL replace with 18
delimiter //
CREATE TRIGGER insertion BEFORE INSERT ON customers
   FOR EACH ROW
   BEGIN
	   IF NEW.age IS NULL THEN
		   SET NEW.age = 18;
	   END IF;
   END;//
delimiter ;

# after each order, update the stock
delimiter //
CREATE TRIGGER stock_updation AFTER INSERT ON ordered_items
   FOR EACH ROW
   BEGIN
   DECLARE id int;
   DECLARE q int;
   SET id = NEW.item_id;	
   SET q = NEW.quantity;
   
   UPDATE items SET items.quantity = items.quantity - q where item_id = id;
   
   END;//
delimiter ;

# if new rating entry inserted is less than the average, automatically issue a support entry
delimiter //
CREATE TRIGGER low_rating AFTER INSERT ON feedback
   FOR EACH ROW
   BEGIN
   DECLARE new_rating int;
   DECLARE Cid int;
   SET new_rating = NEW.rating;
   SET Cid = NEW.customer_id;
   
		IF new_rating < (SELECT AVG(rating) FROM feedback) THEN
			INSERT INTO support (customer_id, issue, issue_date) values (Cid, 'Not Happy with Buynget Services', current_date());
		END IF;
   END;//
delimiter ;

# delete all those order-entries from 'orders' table which are completed
delimiter //
CREATE TRIGGER order_completed BEFORE INSERT ON carts
   FOR EACH ROW
   BEGIN
		DELETE FROM orders where delivery_date < current_date();
   END;//
delimiter ;

# if order exceeds, $100 => min(0.1 * amount, $15) )
-- delimiter //
-- CREATE TRIGGER provide_discount BEFORE INSERT ON transactions
--    FOR EACH ROW
--    BEGIN
--    DECLARE total int;
--    DECLARE O_id int;
--    DECLARE discount int;
--    SET total = NEW.amount;
--    SET O_id = NEW.order_id;
--    SET discount = total * 0.1;

-- 		IF (total > 100) THEN

-- 			IF (discount > 15) THEN
-- 				SET discount = 15;
-- 			END IF;
			
-- 			UPDATE transactions SET amount = amount - discount WHERE order_id = O_id;
-- 		END IF;
--    END;//
-- delimiter ;
