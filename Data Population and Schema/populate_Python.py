
import mysql.connector as myConnector
import csv
import random 


myDataBase = myConnector.connect(host="localhost", user="prerak", passwd="prerak", database="buynget")
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
while customer_id <= 20:
    myCursor.execute( "insert into sellers values({})".format(customer_id) )
    myDataBase.commit()
    temp = random.randint(1,104)
    myCursor.execute( "insert into sells values({}, {})".format(customer_id, temp) )
    myDataBase.commit()
    temp += 1;
    myCursor.execute( "insert into sells values({}, {})".format(customer_id, 1 + (temp%104) ) )
    myDataBase.commit()
    customer_id += 1



# populate carts first then buyers
customer_id = 15
cart_id = 1
while customer_id <= 950:
    myCursor.execute( "insert into buyers values({})".format(customer_id))
    myDataBase.commit()
    myCursor.execute( "insert into carts values({}, {})".format(cart_id, customer_id))
    myDataBase.commit()
    if customer_id % 3 == 0:
        myCursor.execute( "insert into stores values({}, {}, {})".format(cart_id, random.randint(1,104), 10*random.randint(1,20)))
        myDataBase.commit()
    customer_id += 1
    cart_id += 1



# populate orders first and then transaction
order_id = 1
customer_id = 23
item_id = 3
modes = ['NetBanking', 'UPI', 'Credit-Card', 'Debit-Card']
while order_id <= 49:
    
    myCursor.execute("select selling_price from items where item_id = {}".format(item_id))
    currPrice = myCursor.fetchone()
    currQuantity = random.randint(2, 10)

    myCursor.execute("insert into orders values({}, {}, current_date(), current_date())".format(order_id, customer_id))
    myDataBase.commit()

    myCursor.execute("insert into ordered_items values({}, {}, {})".format(order_id, item_id, currQuantity))
    myDataBase.commit()
    item_id += 1
    myCursor.execute("insert into ordered_items values({}, {}, {})".format(order_id, item_id + 1, currQuantity + 5))
    myDataBase.commit()

    if order_id % 2 == 0:
        myCursor.execute("insert into transactions values({}, {}, '{}', {})".format(order_id, customer_id, modes[random.randint(0,len(modes)-1)], currQuantity * currPrice[0]))
        myDataBase.commit()
    customer_id += 3
    item_id += 1
    order_id += 1
