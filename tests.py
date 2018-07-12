import json
import unittest
from flask import Flask
from flask_testing import TestCase
from app import app
from app.database import User


class TestBase(TestCase):
	""" Base configurations for the tests. """

    # Specify the create_app method, which should 
    # return a Flask instance. If you don’t define create_app 
    # a NotImplementedError will be raised.
	def create_app(self):
		return app

	def setUp(self):
		""" Set up test client. """
		self.app = app.test_client()

	def test_index(self):
		""" Test response to the index endpoint. """
		response = self.app.get('/index')
		self.assertEqual(response.status_code, 200)
		# Test a JSON response.
		self.assertEqual(response.json, ({'message': 'Hello World!'}))


if __name__ == "__main__":
	unittest.main()
