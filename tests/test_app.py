from app import app
import unittest

class TestApp(unittest.TestCase):

    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'This is the about page. Please contact us through mail')

if __name__ == '__main__':
    unittest.main()
