#!/usr/bin/python3

import unittest
from models.city import City
from models.engine.file_storage import FileStorage
import os


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    @classmethod
    def setUpClass(cls):
        cls.city = City()
        cls.city.name = "San Francisco"
        cls.city.state_id = "state123"
        cls.test_file = "file.json"
        cls.storage = FileStorage()

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)

    def test_initialization(self):
        """Test that City initializes with the correct attributes"""
        self.assertEqual(self.city.name, "San Francisco")
        self.assertEqual(self.city.state_id, "state123")

    def test_to_dict(self):
        """Test the to_dict method of the City class"""
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['name'], "San Francisco")
        self.assertEqual(city_dict['state_id'], "state123")
        self.assertEqual(city_dict['__class__'], "City")

if __name__ == "__main__":
    unittest.main()
