import unittest

from app import app

class FlaskTesting(unittest.TestCase):
    def test_index_loads(self):
        client = app.test_client(self)
        resp = client.get('/', content_type='html/text')
        self.assertEqual(resp.status_code, 200)

    def test_registration(self):
        client = app.test_client(self)
        resp = client.post('/', data=dict(name="john", 
                                            email="john@gmail.com", 
                                            password="pass123", 
                                            confirm="pass123"), 
                                            follow_redirects=True)
        self.assertTrue(b'Events' in resp.data)
        


if __name__ == '__main__':
    unittest.main()