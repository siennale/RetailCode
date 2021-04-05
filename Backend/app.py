#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
from sqlite3 import Error
import flask
from flask import request
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

###################################### HELPER FUNCTION FOR DB ########################################
######################################################################################################

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
			product_barcode INTEGER,
			product_name TEXT,
			product_selling_price REAL,
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
		c.execute("INSERT INTO Products VALUES (123456789, 'Apple', 10, 1, 1,1,1)")
		# c.execute("INSERT INTO ProductsIn VALUES (?, ?, ?, ?, ?)", (0, 0, 'product', 0, 0, 0))
		# c.execute("INSERT INTO Transactions VALUES (?, ?, ?, ?, ?)", (0, 'userid', 'date', 0, 0))
		# c.execute("INSERT INTO SoldItems VALUES (?, ?, ?, ?)", (0, 0, 0, 0))

def get_price_by_barcode(barcode, conn):
	c = conn.cursor()
	c.execute("SELECT * FROM Products WHERE product_barcode = " + str(barcode))
	return c.fetchone()
	


conn = create_connection('retail.db')
initialize_db(conn)

######################################################################################################
######################################################################################################
######################################################################################################
#                                    FLASK CODE GOES BELOW
######################################################################################################

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/getPriceByBarcode', methods=['POST'])
def POST_price_by_barcode():
    print (request.get_json(), flush=True)
    with create_connection('retail.db') as conn:
        return jsonify(get_price_by_barcode(request.get_json()['barcode'], conn))
    

app.run()