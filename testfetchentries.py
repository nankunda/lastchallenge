import unittest
import datetime
from unittest.mock import patch
from flask import request, jsonify, json
from app import fetchentries
from app import app
from createentry import auto_increment_id, get_current_date


class TestFetchEntries(unittest.TestCase):

    def test_api_fetches_welcome_message(self):
        with app.test_client() as client:
            response = client.get('/')

            self.assertEqual(response.get_data(as_text=True),
                             'Welcome to my dairy application')
            self.assertEqual(response.status_code, 200)

    def test_api_fetches_all_entries(self):
        with app.test_client() as client:
            response = client.get('/api/v1/entries')

            self.assertEqual(
                response.status_code, 200)
            self.assertEqual(response.json,  {'entries': []})

    def test_api_returns_empty_list_before_post(self):
        with app.test_client() as client:
            response = client.get('/api/v1/entries')
            self.assertEqual(
                response.json, {'entries': []})
            self.assertIsNotNone(response.json)

    def test_generate_id(self):
        self.assertIsNotNone(auto_increment_id())
        self.assertEqual(auto_increment_id(), 1)

    def test_capture_current_date(self):
        self.assertIsNotNone(get_current_date())
        self.assertEqual(get_current_date(), '2018-09-27')

    def mock_create_new_entry():
        new_entry = {
            'entryId': 1,
            'creation_date': "2018-09-27",
            'content': "hi there"}
        return new_entry

    @patch('app.create_entry.create_new_entry', side_effect=mock_create_new_entry)
    def test_api_can_create_new_entry(self, create_new_entry):
        self.assertIsNotNone(create_new_entry())
        self.assertIsInstance(create_new_entry(), dict)

    new_item = {
        'entryId': 1,
        'creation_date': "12/12/2018",
        'content': "hi there"
    }
    entries = []
    # def test_api_can_add_new_entry(self):
    #     with app.test_client() as client:
    #         response = client.post(
    #             '/api/v1/entries', content_type='application/json', data=json.dumps(self.new_item))
    #         print(response.json)
    #         self.assertEqual(
    #             response.json(), [{'content': 'hi there', 'creation_date': [24 chars]: 1}])
    #         self.assertIsNotNone(response.json)
    # def test_api_retrieves_single_entry(self):


if __name__ == '__main__':
    unittest.main()