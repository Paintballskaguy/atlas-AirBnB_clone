#!/usr/bin/python3

import unittest
from models.review import Review
from models.engine.file_storage import FileStorage
import os


class TestReview(unittest.TestCase):

    storage = FileStorage()
    
    @classmethod
    def setUpClass(cls):
        cls.review = Review()
        cls.test_file = "file.json"
        
    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)
            
    def test_initialization(self):
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")
        
    def test_to_dict(self):
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['place_id'], "")
        self.assertEqual(review_dict['user_id'].strip(), "")
        self.assertEqual(review_dict['text'], "")
        self.assertEqual(review_dict['__class__'], "Review")
        
if __name__ == "__main__":
    unittest.main()
        
