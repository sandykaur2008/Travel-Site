import unittest 
import trace 
import sys 
from app import app


class Routes(unittest.TestCase):
    def test_success(self):
        with app.test_client() as client:
            response1 = client.get('/')
            response2 = client.get('/about')
            response3 = client.get('/uruguay')
            self.assertEqual(response1.status_code, 200)
            self.assertEqual(response2.status_code, 200)
            self.assertEqual(response3.status_code, 200)


if __name__ == '__main__':
    unittest.main()