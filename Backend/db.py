#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3


# Create a tables 
def create_tables():
	# Create tables 



























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
