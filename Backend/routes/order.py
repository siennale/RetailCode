from __main__ import app
import datetime
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
        print(str(barcode) + " " + str(qty))
        c.execute("INSERT INTO SoldItems (product_barcode, quantity, transaction_id) VALUES(?,?,?)",
                  (barcode, qty, transaction_id))
    conn.commit()
    return "Success"


######################################################################################################
######################################################################################################
#                                    FLASK CODE GOES BELOW
######################################################################################################


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
    print(request.get_json())
    data = request.get_json()
    try:
        with create_connection('retail.db') as conn:
            transaction_id = set_transaction(
                data['user_id'], data['total_sale'], data["total_items"], conn)
            return set_sold_items(data['item_list'].items(), transaction_id, conn)
    except Error as ex:
        return jsonify({"result": ex})
