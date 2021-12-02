#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import sqlite3
from sqlite3 import Error
import datetime
import flask
from flask import request, send_from_directory, jsonify
from flask_cors import CORS, cross_origin
from utils.db_helper import create_connection, initialize_db
app = flask.Flask(__name__, static_folder='build')
app.config["DEBUG"] = True


conn = create_connection('retail.db')
initialize_db(conn)

######################################################################################################
#                                    FLASK CODE GOES BELOW
######################################################################################################


# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        print (app.static_folder)
        return send_from_directory(app.static_folder, 'index.html')



from routes import order
from routes import product


app.run(port=5001)
