
import mysql.connector as myConnector
import csv

myDataBase = myConnector.connect(host="localhost",user="prerak",passwd="prerak",database="buynget")
myCursor = myDataBase.cursor()
myCursor.execute("use buynget")

myCursor.execute("drop table accounts") 
myCursor.execute("drop table customers") 

myCursor.execute("create table accounts (username VARCHAR(50), email VARCHAR(50), password VARCHAR(50), customer_id INT);")
myCursor.execute("create table customers(customer_id INT, customer_name VARCHAR(50), age INT, gender VARCHAR(50), phone VARCHAR(50), country VARCHAR(50), state VARCHAR(50), street_name VARCHAR(50), street_no INT, pincode INT);")


customer_id = 1

with open('accounts.csv','r') as csv_file:
	csv_reader = csv.reader(csv_file)

	next(csv_reader)

	for row in csv_reader:
		query = "insert into accounts values('{}', '{}', '{}', {})".format(row[0], row[1], row[2], customer_id)
		myCursor.execute(query)
		myDataBase.commit()
		customer_id += 1
		

customer_id = 1
with open('customers.csv','r') as csv_file:   
	csv_reader = csv.reader(csv_file)

	next(csv_reader)

	for row in csv_reader:
		query = "insert into customers values({}, '{}' , {}, '{}', '{}', '{}', '{}', '{}', {}, {})".format(customer_id, row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
		myCursor.execute(query)
		myDataBase.commit()
		customer_id += 1
