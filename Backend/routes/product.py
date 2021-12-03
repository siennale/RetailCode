from __main__ import app
from flask_cors import CORS, cross_origin
from flask import request
from flask import jsonify
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connected to DB :" + sqlite3.version)
        return conn
    except Error as e:
        print(e)


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


######################################################################################################
######################################################################################################
#                                    FLASK CODE GOES BELOW
######################################################################################################


@app.route('/product', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def POST_price_by_barcode():
    print(request.args.get('barcode'))
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
        print(ex)
        return "Failed with serverside issue"
    except:
        return "unknow issue"
