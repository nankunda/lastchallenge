import datetime
from flask import jsonify, request
from app import app

entries = list()


def auto_increment_id():
    if not entries:
        return 1

    return entries[-1]['entryid']+1


def get_current_date():
    return datetime.date.today().strftime('%Y-%m-%d')


def create_new_entry():
    request_data = request.get_json(force=True)
    new_entry = dict()
    new_entry['entryid'] = auto_increment_id()
    new_entry['creation_date'] = get_current_date()
    new_entry['content'] = request_data['content']
    return new_entry


@app.route('/api/v1/entries', methods=['POST'])
def add_entries():
    new_entry = create_new_entry()
    entries.append(new_entry)
    return jsonify(entries), 201