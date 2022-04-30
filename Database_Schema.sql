
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



CREATE role team;

GRANT SELECT ON owners_info to team;
GRANT SELECT ON customers to team;
GRANT DELETE ON accounts to team;
GRANT SELECT ON accounts_info to team;
GRANT SELECT ON sellers to team;
GRANT SELECT ON buyers to team;
GRANT ALL ON items to team;
GRANT SELECT ON orders to team;
GRANT SELECT ON ordered_items to team;
GRANT SELECT ON support to team;
GRANT SELECT, DELETE ON feedback to team;
GRANT SELECT ON payments to team;
GRANT SELECT ON transactions to team;
GRANT SELECT ON sells to team;

CREATE USER owner1@localhost identified by 'prerak';
CREATE USER owner2@localhost identified by 'vineet';
CREATE USER owner3@localhost identified by 'janhavi';
CREATE USER owner4@localhost identified by 'abhinav';

GRANT team TO owner1@localhost;
GRANT team TO owner2@localhost;
GRANT team TO owner3@localhost;
GRANT team TO owner4@localhost;




CREATE USER seller@localhost IDENTIFIED by 'seller';
GRANT SELECT ON owners_info to seller@localhost;
# allow to change PERSONAL details
# allow to see what he/she sells
# allow to see maximum selling product for his items only

CREATE USER buyer@localhost IDENTIFIED by 'buyer';
GRANT SELECT ON owners_info to buyer@localhost;
# allow to change/see PERSONAL details
# names of sellers who sell particular item
# allow to see what's inside the cart
# allow to Empty cart (not sure)





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
