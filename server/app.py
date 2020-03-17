# Import everything that we need from Flask
from flask import Flask, request, session, flash, jsonify, g, abort
from flask_cors import CORS
# This allows us to create decorated functions
from functools import wraps
# This may not be used, but it's for url parsing
from markupsafe import escape
# Store all of our data, potentially logins
import sqlite3
# Random vars
import os
# Get a database going
import sqlite3
# Import all of our specific db code here
from db_helper import *
DATABASE = 'appdata.db'

## Quick DB setup
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE, isolation_level=None)
        #db.row_factory = sqlite3.Row
    db_setup(db.cursor())
    return db

# Check the API key
def require_appkey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        if request.headers.get('key') is not None and request.headers.get('key').replace("'", '') == "317f7911-4b82-4d4f-adb6-9bd6fef3d84f":
            print("API key success")
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function

app = Flask(__name__)
app.secret_key = os.urandom(16)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def home():
    return "If you're seeing this, you're in good shape"

@app.route('/passphrase/<pp>')
@app.route('/passphrase', methods=['GET','POST'])
def passphrase(pp=None):
    print(request.method + " to /passphrase")
    if request.method == 'POST':
        print(request.get_json())
        json_data = request.get_json()
        passphrase = json_data['passphrase']
        passphrase = passphrase.lower()
        cur = get_db().cursor()
        clue = search_clue_by_passphrase(cur, passphrase)
        if clue is not None:
            print(clue)
            #return jsonify(clue=clue[2], hint1=clue[3], hint2=clue[4])
        else:
            return jsonify("Not Found")

    elif request.method == 'GET':
        cur = get_db().cursor()
        clue = search_clue_by_passphrase(cur, pp)
        if clue is not None:
            return jsonify(clue)
        return jsonify("Not Found")

@app.route('/get_clue_by_id', methods=["POST"])
@require_appkey
def get_clue_id():
    cur = get_db().cursor()
    clue_id = request.get_json()["clue_id"]
    return jsonify(get_clue_by_id(cur, clue_id))


@app.route('/add_clue', methods=["POST"])
@require_appkey
def new_clue():
    cur = get_db().cursor()
    json_data = request.get_json()
    passphrase = json_data["passphrase"]
    next_clue = json_data["next_clue"]
    hint1 = json_data["hint1"]
    hint2 = json_data["hint2"]
    return jsonify(add_clue(cur, passphrase, next_clue, hint1, hint2))

@app.route('/add_user', methods=["POST"])
@require_appkey
def new_user():
    cur = get_db().cursor()
    json_data = request.get_json()
    print(json_data)
    name = json_data["name"]
    username = json_data["username"]
    passhash = json_data["passhash"]
    last_clue_id = json_data["last_clue_id"]
    return jsonify(add_user(cur, name, username, passhash, last_clue_id))

@app.route('/get_users')
@require_appkey
def get_users():
    cur = get_db().cursor()
    return jsonify(get_all_users(cur))

@app.route('/login', methods=["POST"])
@require_appkey
def login():
    username = request.get_json()['username']
    cur = get_db().cursor()
    passhash = get_passhash_by_username(cur, username)
    print(passhash)
    return jsonify(passhash)

if __name__ == '__main__':
    app.debug = False
    app.run(use_reloader=True, host='0.0.0.0', port='5000')