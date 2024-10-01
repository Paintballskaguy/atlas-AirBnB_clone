#!/usr/bin/python3

import unittest, os
from models.state import State

class TestState(unittest.TestCase):

    def test_state__init__(self):
        new_state = State()
        self.assertEqual(new_state.name, "")

if __name__ == "__main__":
    unittest.main()
