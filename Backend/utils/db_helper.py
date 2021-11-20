###################################### HELPER FUNCTION FOR DB ########################################
######################################################################################################
from flask_cors import CORS, cross_origin
from flask import request
from flask import jsonify
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
			sold_item_id INTEGER PRIMARY KEY,
			product_barcode INTEGER,
			quantity INTEGER,
			transaction_id INTEGER,
			FOREIGN KEY (transaction_id) REFERENCES Transactions(transaction_id)
		)"""),

                ("""CREATE TABLE IF NOT EXISTS Transactions (
			transaction_id INTEGER PRIMARY KEY,
			user_id TEXT,
			date TEXT,
			total_items INTEGER,
			total_sale REAL,
			bills_offered REAL,
			FOREIGN KEY (user_id) REFERENCES Users(user_id)
		)""")
                ]
    with conn:
        c = conn.cursor()
        for command in commands:
            c.execute(command)
