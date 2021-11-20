#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import sqlite3
from sqlite3 import Error
import datetime
import flask
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
from utils.db_helper import create_connection, initialize_db
app = flask.Flask(__name__)
app.config["DEBUG"] = True


conn = create_connection('retail.db')
initialize_db(conn)

######################################################################################################
#                                    FLASK CODE GOES BELOW
######################################################################################################


@app.route('/', methods=['GET'])
def home():
    return "<h1>POS system</h1><p>This site is a prototype API for POS.</p>"


from routes import order
from routes import product


app.run(port=5001)
