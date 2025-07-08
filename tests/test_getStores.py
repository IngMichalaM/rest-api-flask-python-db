import unittest
from app import app


class TestGetStores(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_stores(self):
        response = self.app.get("/store")
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        print(data)
        self.assertIn("stores", data)
        self.assertIsInstance(data["stores"], list)
        # Optionally check known content
        store_names = [store["name"] for store in data["stores"]]
        self.assertIn("My Store", store_names)


if __name__ == "__main__":
    unittest.main()
