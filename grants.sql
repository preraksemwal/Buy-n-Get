CREATE USER owner@localhost IDENTIFIED by 'owner';
GRANT SELECT ON owners_info to owner@localhost;
GRANT SELECT ON customers to owner@localhost;
GRANT DELETE ON accounts to owner@localhost;
GRANT SELECT ON accounts_info to owner@localhost;
GRANT SELECT ON sellers to owner@localhost;
GRANT SELECT ON buyers to owner@localhost;
GRANT ALL ON items to owner@localhost;
GRANT SELECT ON orders to owner@localhost;
GRANT SELECT ON ordered_items to owner@localhost;
GRANT SELECT ON support to owner@localhost;
GRANT SELECT, DELETE ON feedback to owner@localhost;
GRANT SELECT ON payments to owner@localhost;
GRANT SELECT ON transactions to owner@localhost;
GRANT SELECT ON sells to owner@localhost;
# allow to change PERSONAL details


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
