# Import everything that we need from Flask
from flask import Flask, request, session, flash, jsonify, g
from flask_cors import CORS
# This may not be used, but it's for url parsing
from markupsafe import escape
# Store all of our data, potentially logins
import sqlite3
# Random vars
import os
# Get a database going
import sqlite3
from db_helper import *
DATABASE = 'clues.db'

## Quick DB setup
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db_setup(db.cursor())
    return db


app = Flask(__name__)
app.secret_key = os.urandom(16)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def home():
    return "If you're seeing this, you're in good shape"

@app.route('/clue', methods=['GET','POST'])
def clue():
    print(request.method)
    if request.method == 'POST':
        print(request.get_json())
        json_data = request.get_json()
        passphrase = json_data['passphrase']
        passphrase = passphrase.lower()
        cur = get_db().cursor()
        clue = search_db(cur, passphrase)
        if clue is not None:
            return jsonify(clue=clue[2], hint1=clue[3], hint2=clue[4])
        else:
            return jsonify("Not Found")

    elif request.method == 'GET':
        print("Get")
        return jsonify("Not Found")

@app.teardown_appcontext
def close_db_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        
if __name__ == '__main__':
    app.debug = False
    app.run(use_reloader=True, host='0.0.0.0', port='5000')