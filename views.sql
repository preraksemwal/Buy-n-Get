CREATE VIEW owners_info AS
SELECT owner_name AS Name, email 
FROM owners;


CREATE VIEW accounts_info AS
SELECT username, email 
FROM accounts;


CREATE VIEW customers_info AS 
SELECT customer_name, gender, phone_no, country, state, street_name, street_no, pincode
FROM customers;
