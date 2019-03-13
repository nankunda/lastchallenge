from flask import jsonify
from app import app
from createentry import entries


@app.route("/")
def hello():
    return "Welcome to my dairy application", 200


@app.route('/api/v1/entries')
def fetch_entries():
    return jsonify({'entries': entries}), 200