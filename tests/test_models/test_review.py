#!/usr/bin/python3

import unittest
from models.review import Review
from models.engine.file_storage import FileStorage
import os


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""
    
    @classmethod
    def setUpClass(cls):
        cls.review = Review()
        cls.review.place_id = "place123"
        cls.review.user_id = " user123"
        cls.review.text = "Great place to stay!"
        cls.test_file = "file.json"
        cls.storage = "file.json"
        
    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)
            
    def test_initialization(self):
        """tests that review initializes correctly"""
        self.assertEqual(self.review.place_id, "place123")
        self.assertEqual(self.review.user_id, "user123")
        self.assertEqual(self.review.text, "Great place to stay!")
        
    def test_to_dict(self):
        """"Test the to_dict method of the Review class"""
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['place_id'], "place123")
        self.assertEqual(review_dict['user_id'], "user123")
        self.assertEqual(review_dict['text'], "Great place to stay!")
        self.assertEqual(review_dict['__class__'], "Review")
        
if __name__ == "__main__":
    unittest.main()
        