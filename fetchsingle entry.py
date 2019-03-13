from flask import jsonify
from app import app
from createentry import entries


@app.route('/api/v1/entries/<int:entryId>')
def get_single_entry(entryId):
    for entry in entries:
        if entry['entry_id'] == entryId:
            return jsonify({'entry': entry}), 200
        return "the id should be an integer", 404