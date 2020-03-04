# Import everything that we need from Flask
from flask import Flask, request, session, flash
# This may not be used, but it's for url parsing
from markupsafe import escape
# Store all of our data, potentially logins
import sqlite3
# Random vars
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route('/')
def home():
    flash("Hello!")
    return "If you're seeing this, you're in good shape"

@app.route('/clue', methods=['POST'])
def clue():
    if request.method == 'POST':
        json_data = request.get_json()
        clue = json_data['clue']
        
if __name__ == '__main__':
    app.debug = True
    app.run(use_reloader=True, host='0.0.0.0', port='5000')