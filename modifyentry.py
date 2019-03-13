import datetime
from flask import jsonify, request
from app import app
from createentry import entries


@app.route('/api/v1/entries/<int:entry_id>', methods=['PUT'])
def edit_entry(entry_id):

    if entry_id:
        for entry in entries:

            if entry['entryid'] == entry_id:
                request_data = request.get_json()
                entry['content'] = request_data['content']
                return jsonify(entry), 201
    else:
        message = "The entry you have selected does not exist"
        return message, 404