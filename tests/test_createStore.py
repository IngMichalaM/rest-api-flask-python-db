import unittest
import json
from app import app, stores


class TestCreateStore(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_store(self):
        initial_count = len(stores)
        payload = {"name": "Hydroponia Store"}

        response = self.app.post(
            "/store",
            data=json.dumps(payload),
            content_type="application/json"
        )

        self.assertEqual(201, response.status_code)
        data = response.get_json()
        self.assertIsInstance(data, dict)
        self.assertEqual("Hydroponia Store", data["name"])
        self.assertEqual([], data["item"])
        self.assertIn(data, stores)
        self.assertEqual(initial_count+1, len(stores))


if __name__ == "__main__":
    unittest.main()
