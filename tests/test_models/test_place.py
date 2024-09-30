#!/usr/bin/python3

import unittest, os
from models.place import Place
from models.engine.file_storage import FileStorage


class TestPlace(unittest.TestCase):
    storage = FileStorage()

    def setUp(self):
        self.place = Place()

    def test_initialization(self):
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.anemity_ids, [])

    def test_to_dict(self):
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict['city_id'], "")
        self.assertEqual(place_dict['__class__'], "Place")
        
if __name__ == "__main__":
    unittest.main()
