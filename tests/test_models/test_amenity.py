#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
import os


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    @classmethod
    def setUpClass(cls):
        cls.amenity = Amenity()
        cls.amenity.name = "Wi-Fi"
        cls.test_file = "file.json"
        cls.storage = FileStorage()

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)

    def test_initialization(self):
        """Test that Amenity initializes with the correct attributes"""
        self.assertEqual(self.amenity.name, "Wi-Fi")

    def test_to_dict(self):
        """Test the to_dict method of the Amenity class"""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['name'], "Wi-Fi")
        self.assertEqual(amenity_dict['__class__'], "Amenity")

if __name__ == "__main__":
    unittest.main()
