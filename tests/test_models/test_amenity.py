#!/usr/bin/python3

import unittest, os
from models.amenity import Amenity
# from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):

    """
    @classmethod
    def setUpClass(cls):
        cls.storage = FileStorage()
        cls.test_file = "file.json"

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)
    """

    def test_amenity__init__(self):
        new_amenity = Amenitiy()
        self.assertIsInstance(new_amenity, Amenity)
        self.assertEqual(new_amenity.name, "")

if __name__ == "__main__":
    unittest.main()
