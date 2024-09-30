#!/usr/bin/python3

import unittest
from models.place import Place
from models.engine.file_storage import FileStorage
import os


class TestPlace(unittest.TestCase):
    """Test cases for the Places class"""
    
    @classmethod
    def setUpClass(cls):
        cls.place = Place()
        cls.place.city_id = "city123"
        cls.place.user_id = "user123"
        cls.place.name = "Cozy Apartment"
        cls.place.number_rooms = 3
        cls.place.number_bathrooms = 2
        cls.test_file = "file.json"
        cls.storage = FileStorage()
        
    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)
            
    def test_initialization(self):
        """test that place initalizes with the correct stuff"""
        self.assertEqual(self.place.city_id, "city123")
        self.assertEqual(self.place.user_id, "user123")
        self.assertEqual(self.place.name, "Cozy Apartment")
        self.assertEqual(self.place.number_rooms, 3)
        self.assertEqual(self.place.number_bathrooms, 2)

    def test_to_dict(self):
        """test the to_dict method of the Place class."""
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict['city_id'], "city123")
        self.assertEqual(place_dict['user_id'], "user123")
        self.assertEqual(place_dict['name'], "Cozy Apartment")
        self.assertEqual(place_dict['__class__'], "Place")
        
if __name__ == "__main__":
    unittest.main()