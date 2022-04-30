
use buynget;

drop view owners_info;
drop view accounts_info;
drop view customers_info;
drop view items_info;

drop user owner1@localhost;
drop user owner2@localhost;
drop user owner3@localhost;
drop user owner4@localhost;
drop user seller1@localhost;
drop user seller2@localhost;
drop user buyer1@localhost;
drop user buyer2@localhost;

drop role team;
drop role buy;
drop role sell;

drop trigger insertion;
drop trigger stock_updation;
drop trigger low_rating;
drop trigger order_completed;
