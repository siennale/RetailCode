#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
from sqlite3 import Error

# connect db
def create_connection(db_file):
	""" create a database connection to a SQLite database """
	conn = None
	try:
		conn = sqlite3.connect(db_file)
		print("Connected to DB :" + sqlite3.version)
		return conn
	except Error as e:
		print(e)

# Initialize DB
def initialize_db(conn):

	commands = [("""CREATE TABLE IF NOT EXISTS Users (
			user_id TEXT PRIMARY KEY,
			name TEXT,
			password TEXT
		)"""),

		("""CREATE TABLE IF NOT EXISTS Products (
			product_id INTEGER PRIMARY KEY,
			product_barcode INTEGER UNIQUE,
			product_name TEXT,
			product_selling_price REAL,
			product_tax INTEGER,
			product_total_quantity INTEGER,
			product_sold_quantity INTEGER,
			product_instock_quantity INTEGER	
		)"""),

		# when products in, update products
		("""CREATE TABLE IF NOT EXISTS ProductsIn (
			product_id INTEGER PRIMARY KEY,
			product_barcode INTEGER,
			order_place TEXT,
			order_quantity INTEGER,
			product_purchase_price REAL,
			FOREIGN KEY (product_id) REFERENCES Products(product_id)
		)"""),

		# when products out, update products
		("""CREATE TABLE IF NOT EXISTS SoldItems (
			product_id INTEGER PRIMARY KEY,
			product_barcode INTEGER,
			product_selling_price INTEGER,
			quantity INTEGER,
			FOREIGN KEY (product_id) REFERENCES Products(product_id)
		)"""),

		("""CREATE TABLE IF NOT EXISTS Transactions (
			transaction_id INTEGER PRIMARY KEY,
			user_id TEXT,
			date TEXT,
			transaction_total REAL,
			bills_offered REAL,
			FOREIGN KEY (user_id) REFERENCES Users(user_id)
		)""")]
	with conn:
		c = conn.cursor()
		for command in commands:
			c.execute(command)


def insert_db(conn):
	with conn:
		c = conn.cursor()
		# c.execute("INSERT INTO Users VALUES (?, ?, ?, ?)", ('userid', 'name', 'password'))
		c.execute("INSERT INTO Products VALUES (123456,101,'Icecream', 10, 1, 1,1)")
		print ("added data")
		# c.execute("INSERT INTO ProductsIn VALUES (?, ?, ?, ?, ?)", (0, 0, 'product', 0, 0, 0))
		# c.execute("INSERT INTO Transactions VALUES (?, ?, ?, ?, ?)", (0, 'userid', 'date', 0, 0))
		# c.execute("INSERT INTO SoldItems VALUES (?, ?, ?, ?)", (0, 0, 0, 0))

def get_price_by_barcode(barcode, conn):
	c = conn.cursor()
	c.execute("SELECT * FROM Products WHERE product_barcode = " + str(barcode))
	return c.fetchone()

from csv import reader

def ingestData(conn):
	c = conn.cursor()
	with open('pos_data.csv', 'r') as read_obj:
		csv_reader = reader(read_obj)
		for row in csv_reader:
			print (row)
			print ("----")
			c.execute(" INSERT OR IGNORE INTO Products(product_barcode, product_name, product_selling_price, product_tax, product_total_quantity, product_sold_quantity, product_instock_quantity ) VALUES(?,?,?,?,?,?, ?)", row)

		conn.commit()


if __name__ == '__main__':
	conn = create_connection('retail.db')
	initialize_db(conn)
	ingestData(conn)
	print (get_price_by_barcode(815154000000, conn))
	conn.close()


















# def connect_db():

#     # TODO: Move it to env variable

#     connection = psycopg2.connect(user='postgres', password='test',
#                                   host='127.0.0.1', port='5432',
#                                   database='postgres')

#     cursor = connection.cursor()

#     # Print PostgreSQL Connection properties

#     print (connection.get_dsn_parameters(), '\n')

#     # Print PostgreSQL version

#     cursor.execute('SELECT version();')
#     record = cursor.fetchone()
#     print ('You are connected to - ', record, '\n')
#     initialize_db(cursor)


#     # except (Exception, psycopg2.Error) as error :
#     #     print ("Error while connecting to PostgreSQL", error)

# def initialize_db(cursor):

#     commands = \
#         ("""
# 		CREATE TABLE  IF NOT EXISTS products (
# 			product_barcode             NUMERIC PRIMARY KEY,
# 			product_name                char(50) NULL,
# 			product_purchase_price      NUMERIC NOT NULL,
# 			product_selling_price       NUMERIC NOT NULL,
# 			product_instock_quantity    NUMERIC NULL,
# 			product_total_quantity      NUMERIC NULL
# 		)
# 		""",
#          """
# 		CREATE TABLE IF NOT EXISTS orders (
# 			order_id                    SERIAL PRIMARY KEY,
# 			product_barcode             NUMERIC NOT NULL,
# 			order_place                 char(50) NOT NULL,
# 			order_quantity              NUMERIC NOT NULL,
# 			product_purchase_price      NUMERIC NOT NULL,
# 			FOREIGN KEY (product_barcode) REFERENCES products(product_barcode)
# 		)
# 		""",
#          """
# 		CREATE TABLE IF NOT EXISTS sales (
# 				sale_id             NUMERIC PRIMARY KEY,
# 				total_sale          NUMERIC NOT NULL
# 		)
# 		""",
#          """
# 		CREATE TABLE IF NOT EXISTS transactions (
# 				sale_id NUMERIC,
# 				transactions_id NUMERIC PRIMARY KEY,
# 				product_barcode NUMERIC NOT NULL,
# 				FOREIGN KEY (product_barcode)
# 					REFERENCES products (product_barcode),
# 				FOREIGN KEY (sale_id)
# 					REFERENCES sales (sale_id)
# 		)
# 		""")

#     for command in commands:
#         cursor.execute(command)

#     print('created all table')


# connect_db()

## Function for putting a entry in db. Payload is json form data e.g. { product_barcode : [ 12344, 123231, 123213]}
# def set_tranasction(cursor, payload):
#     # add it to the Transaction table.
#     # Also reduce the quantity from the Products table.

## this is the whole puchase. Payload is e.g. { total_sale_price: 89, product_barcode :[12321, 12312, 12321]}
# def set_sale(cursor, payload):
#     # add it to the sales table and then call set_transaction to add a product sale.

## Orders is e.g. Json { Product_barcode: 34, order_place: "costco", order_quantity: 34, product_purchase_price: 2}
# def set_orders(cursor, orders):

################################################################################################
#                               HELPER FUNCTIONS
################################################################################################

################################################################################################

## TODO -----------------------------------------------------
# def get_product_price_by_barcode(barcode, cursor):
#     # return the price

# finally:
#     #closing database connection.
#         if(connection):
#             cursor.close()
#             connection.close()
#             print("PostgreSQL connection is closed")W
