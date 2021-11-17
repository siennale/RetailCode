#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
from sqlite3 import Error
import datetime
import flask
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

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


def get_price_by_barcode(barcode, conn):
    c = conn.cursor()
    c.execute("SELECT * FROM Products WHERE product_barcode = " + str(barcode))
    return c.fetchone()


def set_product(barcode, name, price, tax, total_qty, total_sold_qty, total_instock_qty, conn):
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO Products (product_barcode, product_name, product_selling_price, product_tax, product_sold_quantity,product_total_quantity,product_instock_quantity) VALUES (?,?,?,?,?,?,?)",
              (barcode, name, price, tax, total_qty, total_sold_qty, total_instock_qty))
    conn.commit()
    return c.lastrowid


def set_transaction(user_id, total_sale, total_item, conn):
    c = conn.cursor()
    transaction = (user_id, datetime.datetime.utcnow(),
                   total_item, total_sale, 0)
    c.execute("INSERT INTO Transactions (user_id, date, total_items, total_sale, bills_offered) VALUES(?,?,?,?,?)", transaction)
    conn.commit()
    return c.lastrowid


def set_sold_items(items, transaction_id, conn):
    c = conn.cursor()
    for barcode, qty in items:
        print(str(barcode) + " " + str(qty), flush=True)
        c.execute("INSERT INTO SoldItems (product_barcode, quantity, transaction_id) VALUES(?,?,?)",
                  (barcode, qty, transaction_id))
    conn.commit()
    return "Success"


conn = create_connection('retail.db')
initialize_db(conn)
######################################################################################################
######################################################################################################
#                                    FLASK CODE GOES BELOW
######################################################################################################


@app.route('/', methods=['GET'])
def home():
    return "<h1>POS system</h1><p>This site is a prototype API for POS.</p>"


@app.route('/product', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def POST_price_by_barcode():
    print(request.args.get('barcode'), flush=True)
    barcode = request.args.get('barcode')
    if (not barcode):
        return jsonify({"result": "Pelase provide any detail of the product in query"})
    try:
        with create_connection('retail.db') as conn:
            return jsonify(get_price_by_barcode(barcode, conn))
    except Error as ex:
        return jsonify({"result": ex})


@app.route('/product', methods=['POST'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def POST_save_product():
    data = request.get_json()
    try:
        with create_connection('retail.db') as conn:
            result = set_product(data["product_barcode"], data["product_name"], data["product_selling_price"],
                                 data["product_tax"], data["product_total_qty"], data["product_sold_qty"], data["product_instock_qty"], conn)
            return (str(result))
    except KeyError:
        return "Make sure you have all keys are correct"
    except Error as ex:
        print(ex, flush=True)
        return "Failed with serverside issue"
    except:
        return "unknow issue"


@app.route('/order', methods=['POST'])
def POST_save_order():
    """
    json structure 
    {
            "user_id" : "testing",
            "total_sale": 2,
            "total_items": 2,
            "item_list": {
                    "9278349723": 1,
                    "123123": 9
            }
    }
    """
    print(request.get_json(), flush=True)
    data = request.get_json()
    try:
        with create_connection('retail.db') as conn:
            transaction_id = set_transaction(
                data['user_id'], data['total_sale'], data["total_items"], conn)
            return set_sold_items(data['item_list'].items(), transaction_id, conn)
    except Error as ex:
        return jsonify({"result": ex})


app.run(port=5001)
