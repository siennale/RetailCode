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
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection('retail.db')

# Initilize DB
def initilaize_db():

	with conn:
        c = conn.cursor()

        c.execute("""CREATE TABLE Users (
        				user_id TEXT PRIMARY KEY,
        				name TEXT,
        				password TEXT
        )""")

        c.execute("""CREATE TABLE Products (
                        product_id INTEGER PRIMARY KEY,
                        product_barcode INTEGER,
                        product_name TEXT,
                        product_selling_price REAL,
                        product_total_quantity INTEGER,
                        product_sold_quantity INTEGER,
                        product_instock_quantity INTEGER	
        )""")

        c.execute("""CREATE TABLE ProductsIn (
                        product_id INTEGER PRIMARY KEY,
                        product_barcode INTEGER,
                        order_place TEXT,
                        order_quantity INTEGER,
                        product_purchase_price REAL
        )""")

        c.execute("""CREATE TABLE Transactions (
                        transaction_id INTEGER PRIMARY KEY,
                        user_id TEXT,
                        date TEXT,
                        transaction_total REAL,
                        bills_offered REAL
        )""")

        c.execute("""CREATE TABLE SoldItems (
                        id INTEGER PRIMARY KEY,
                        product_barcode INTEGER,
                        product_selling_price INTEGER,
                        quantity INTEGER
 
        )""")


def insert_db(conn):
    with conn:
        c = conn.cursor()
        c.execute("INSERT INTO Users VALUES (?, ?, ?, ?)", ('userid', 'name', 'password'))
        c.execute("INSERT INTO Products VALUES (?, ?, ?, ?, ?,?,?)", (0, 0, 'name', 0, 0, 0, 0, 0))
        c.execute("INSERT INTO ProductsIn VALUES (?, ?, ?, ?, ?)", (0, 0, 'product', 0, 0, 0))
        c.execute("INSERT INTO Transactions VALUES (?, ?, ?, ?, ?)", (0, 'userid', 'date', 0, 0))
        c.execute("INSERT INTO SoldItems VALUES (?, ?, ?, ?)", (0, 0, 0, 0))




















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
