#!/usr/bin/python3

import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def test_city__init__(self):
        new_city = City()
        self.assertEqual(new_city.name, "")
        self.assertEqual(new_city.state_id, "")

if __name__ == "__main__":
    unittest.main()
