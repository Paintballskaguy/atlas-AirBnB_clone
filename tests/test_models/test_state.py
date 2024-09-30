#!/usr/bin/python3

import unittest
from models.state import State
from models.engine.file_storage import FileStorage
import os

class TestState(unittest.TestCase):
    """Test cases for the State class"""

    @classmethod
    def setUpClass(cls):
        cls.state = State()
        cls.state.name = "California"
        cls.test_file = "file.json"
        cls.storage = FileStorage()

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)

    def test_initialization(self):
        """Test that State initializes with the correct attributes"""
        self.assertEqual(self.state.name, "California")

    def test_to_dict(self):
        """Test the to_dict method of the State class"""
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['name'], "California")
        self.assertEqual(state_dict['__class__'], "State")

    def test_save(self):
        """Test the save method of the State class"""
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(old_updated_at, self.state.updated_at)

if __name__ == "__main__":
    unittest.main()
