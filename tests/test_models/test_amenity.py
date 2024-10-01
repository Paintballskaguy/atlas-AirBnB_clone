#!/usr/bin/python3

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_amenity__init__(self):
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, Amenity)
        self.assertEqual(new_amenity.name, "")

if __name__ == "__main__":
    unittest.main()
