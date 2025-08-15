import unittest
from unittest.mock import patch, MagicMock
import json
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def _mock_row(self, id: int, name: str, breed: str):
        row = MagicMock()
        row.id = id
        row.name = name
        row.breed = breed
        return row

    def _setup_query_chain(self, mock_query, results):
        chain = MagicMock()
        mock_query.return_value = chain
        chain.join.return_value = chain
        chain.filter.return_value = chain
        chain.all.return_value = results
        return chain

    @patch('app.db.session.query')
    def test_get_dogs_success(self, mock_query):
        rows = [self._mock_row(1, 'Buddy', 'Labrador'), self._mock_row(2, 'Max', 'German Shepherd')]
        self._setup_query_chain(mock_query, rows)
        resp = self.client.get('/api/dogs')
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.data)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0], {'id': 1, 'name': 'Buddy', 'breed': 'Labrador'})
        self.assertEqual(data[1], {'id': 2, 'name': 'Max', 'breed': 'German Shepherd'})

    @patch('app.db.session.query')
    def test_get_dogs_empty(self, mock_query):
        self._setup_query_chain(mock_query, [])
        resp = self.client.get('/api/dogs')
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.data)
        self.assertEqual(data, [])

    @patch('app.db.session.query')
    def test_get_dogs_structure(self, mock_query):
        rows = [self._mock_row(1, 'Buddy', 'Labrador')]
        self._setup_query_chain(mock_query, rows)
        resp = self.client.get('/api/dogs')
        data = json.loads(resp.data)
        self.assertTrue(isinstance(data, list))
        self.assertEqual(len(data), 1)
        self.assertEqual(set(data[0].keys()), {'id', 'name', 'breed'})

    @patch('app.db.session.query')
    def test_get_dogs_filter_by_breed_id(self, mock_query):
        rows = [self._mock_row(1, 'Buddy', 'Labrador')]
        chain = self._setup_query_chain(mock_query, rows)
        resp = self.client.get('/api/dogs?breedId=1')
        self.assertEqual(resp.status_code, 200)
        chain.filter.assert_called()

    @patch('app.db.session.query')
    def test_get_dogs_filter_by_breed_name(self, mock_query):
        rows = [self._mock_row(1, 'Buddy', 'Labrador')]
        chain = self._setup_query_chain(mock_query, rows)
        resp = self.client.get('/api/dogs?breed=Labrador')
        self.assertEqual(resp.status_code, 200)
        chain.filter.assert_called()

    @patch('app.db.session.query')
    def test_get_dogs_available_only(self, mock_query):
        rows = [self._mock_row(1, 'Buddy', 'Labrador')]
        chain = self._setup_query_chain(mock_query, rows)
        resp = self.client.get('/api/dogs?available=true')
        self.assertEqual(resp.status_code, 200)
        chain.filter.assert_called()

    @patch('app.db.session.query')
    def test_get_breeds_success(self, mock_query):
        breed1 = MagicMock(); breed1.id = 1; breed1.name = 'Labrador'
        breed2 = MagicMock(); breed2.id = 2; breed2.name = 'German Shepherd'
        mock_query.return_value.all.return_value = [breed1, breed2]
        resp = self.client.get('/api/breeds')
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.data)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0], {'id': 1, 'name': 'Labrador'})
        self.assertEqual(data[1], {'id': 2, 'name': 'German Shepherd'})

    @patch('app.db.session.query')
    def test_get_breeds_empty(self, mock_query):
        mock_query.return_value.all.return_value = []
        resp = self.client.get('/api/breeds')
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.data)
        self.assertEqual(data, [])

    @patch('app.db.session.query')
    def test_get_breeds_structure(self, mock_query):
        breed = MagicMock(); breed.id = 1; breed.name = 'Labrador'
        mock_query.return_value.all.return_value = [breed]
        resp = self.client.get('/api/breeds')
        data = json.loads(resp.data)
        self.assertTrue(isinstance(data, list))
        self.assertEqual(len(data), 1)
        self.assertEqual(set(data[0].keys()), {'id', 'name'})


if __name__ == '__main__':
    unittest.main()