use buynget;

drop view owners_info;
drop view accounts_info;
drop view customers_info;

drop user owner1@localhost;
drop user owner2@localhost;
drop user owner3@localhost;
drop user owner4@localhost;
drop user seller@localhost;
drop user buyer@localhost;

drop role ownerselect;

drop trigger insertion;
drop trigger stock_updation;
drop trigger low_rating;
drop trigger order_completed ;
