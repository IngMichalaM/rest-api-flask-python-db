import unittest
from app import app


class TestGetStore(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_store(self):
        response = self.app.get("/store/My Store")
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        print(data)
        self.assertIn("name", data)
        self.assertIn("items", data)
        self.assertIsInstance(data["items"], list)
        self.assertEqual("My Store", data["name"])
        self.assertGreater(len(data["items"]), 0)  # Ensure list isn't empty (there is always a default value)
        item = data["items"][0]
        self.assertIsInstance(item, dict)
        self.assertEqual(item["name"], "Chair")
        self.assertEqual(item["price"], 15.99)


if __name__ == "__main__":
    unittest.main()
