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




# if transaction is completed then corresponding entry in orders is dropped
delimiter //
CREATE TRIGGER transaction_completed AFTER INSERT ON transactions
   FOR EACH ROW
   BEGIN
   DECLARE Oid int;
   SET Oid = NEW.order_id;
		DELETE FROM orders where order_id = Oid;
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
