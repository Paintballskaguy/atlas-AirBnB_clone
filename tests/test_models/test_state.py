#!/usr/bin/python3

import unittest, os
from models.state import State
from models.engine.file_storage import FileStorage

class TestState(unittest.TestCase):
    """Test cases for the State class"""
    storage = FileStorage()

    @classmethod
    def setUpClass(cls):
        cls.state = State()
        cls.test_file = "file.json"

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)

    def test_initialization(self):
        self.assertEqual(self.state.name, "")

    def test_to_dict(self):
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['name'], "")
        self.assertEqual(state_dict['__class__'], "State")

    def test_save(self):
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(old_updated_at, self.state.updated_at)

if __name__ == "__main__":
    unittest.main()
