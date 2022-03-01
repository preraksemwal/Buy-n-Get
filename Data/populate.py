
import mysql.connector as myConnector
import csv
import random 


myDataBase = myConnector.connect(host="localhost",user="prerak",passwd="prerak",database="buynget")
myCursor = myDataBase.cursor()
myCursor.execute("use buynget")


# populate accounts
customer_id = 1
with open('accounts.csv','r') as csv_file:        
	csv_reader = csv.reader(csv_file)

	next(csv_reader)

	for row in csv_reader:
		query = "insert into accounts values('{}', '{}', '{}', {})".format(row[0], row[1], row[2], customer_id)
		myCursor.execute(query)
		myDataBase.commit()
		customer_id += 1
		

# populate customers
customer_id = 1
with open('customers.csv','r') as csv_file:      
	csv_reader = csv.reader(csv_file)

	next(csv_reader)

	for row in csv_reader:
		query = "insert into customers values({}, '{}' , {}, '{}', '{}', '{}', '{}', '{}', {}, {})".format(customer_id, row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
		myCursor.execute(query)
		myDataBase.commit()
		customer_id += 1


# populate sellers
customer_id = 1
while customer_id <= 15:
    ids = ''
    ids += str(random.randint(1,104))
    myCursor.execute( "insert into sellers values({}, '{}')".format(customer_id, ids) )
    myDataBase.commit()
    customer_id += 1

# populate carts first then buyers
cart_id = 1
while customer_id <= 950:
    myCursor.execute( "insert into carts values({}, '{}')".format(cart_id))
    myCursor.execute( "insert into buyers values({}, '{}')".format(customer_id, cart_id))
    myDataBase.commit()
    customer_id += 1
    cart_id += 1



