#!/usr/bin/python3

import unittest
from models.review import Review

class TestReview(unittest.TestCase):

    def test_review__init__(self):
        new_rev = Review()
        self.assertEqual(new_rev.place_id, "")
        self.assertEqual(new_rev.user_id, "")
        self.assertEqual(new_rev.text, "")

if __name__ == "__main__":
    unittest.main()
        
