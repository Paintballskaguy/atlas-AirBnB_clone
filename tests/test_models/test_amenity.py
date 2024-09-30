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
        cls.storage = FileStorage()

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)

    def test_initialization(self):
        self.assertEqual(self.amenity.name, "")

    def test_to_dict(self):
        """Test the to_dict method of the Amenity class"""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['name'], "")
        self.assertEqual(amenity_dict['__class__'], "Amenity")

if __name__ == "__main__":
    unittest.main()
