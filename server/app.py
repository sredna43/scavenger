from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)
app.secret_key = ""

@app.route('/clue', methods=['POST'])
def clue():
    if request.method == 'POST':
        json_data = request.get_json()
        clue = json_data['clue']
        