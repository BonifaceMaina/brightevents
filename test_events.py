import unittest
from flask import json

from app import app

class ViewTesting(unittest.TestCase):
    def test_registration(self):
        client = app.test_client(self)
        resp = client.post('/api/auth/register')
        self.assertEqual(resp.status_code, 200)

    def test_(self):
        client = app.test_client(self)
        resp = client.get('/api/auth/login', follow_redirects=True)
        self.assertEqual(resp.status_code, 405)



class UserTesting(unittest.TestCase):
    """Testing user cases"""

    def test_routes(self):
        client = app.test_client(self)
        tst = client.post('/api/auth/register')
        assert tst.content_type == 'application/json'

    def test_registration_does_not_allow_get(self):
        """test user registration"""
        client = app.test_client(self)
        resp = client.get('/api/auth/register')
        self.assertEqual(resp.status_code, 405)

    def test_login_success(self):
        client = app.test_client(self)
        resp = client.post('/api/auth/login', data=dict(
                                            email="john@gmail.com", 
                                            password="pass123"),
                                            follow_redirects=True)
        self.assertEqual(resp.status_code, 200)

    def test_multiple_registration(self):
        # something
        client = app.test_client(self)


if __name__ == '__main__':
    unittest.main()