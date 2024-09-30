#!/usr/bin/python3
"""Unit tests for the User class"""

import unittest
from models.user import User
from models.engine.file_storage import FileStorage
from datetime import datetime
import os


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    @classmethod
    def setUpClass(cls):
        """Set up resources for all tests in the class"""
        cls.user = User()
        cls.user.email = "test@mail.com"
        cls.user.first_name = "John"
        cls.user.last_name = "Doe"
        cls.user.password = "password123"
        cls.test_file = "file.json"
        cls.storage = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """Tear down resources after all tests in the class"""
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)

    def setUp(self):
        """Set up resources before each test"""
        self.user = TestUser.user

    def tearDown(self):
        """Clean up resources after each test"""
        pass

    def test_initialization(self):
        """Test that User initializes with the correct attributes"""
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.email, "test@mail.com")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.password, "password123")

    def test_to_dict(self):
        """Test the to_dict method of the User class"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['email'], "test@mail.com")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")
        self.assertEqual(user_dict['password'], "password123")
        self.assertEqual(user_dict['__class__'], "User")
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)

    def test_save(self):
        """Test the save method updates the updated_at attribute"""
        old_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(old_updated_at, self.user.updated_at)
        self.assertTrue(self.user.updated_at > old_updated_at)

    def test_file_storage_save_reload(self):
        """Test that User instances are properly saved and reloaded by FileStorage"""
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Bar"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        my_user.save()

        key = f"User.{my_user.id}"
        self.storage.reload()
        self.assertIn(key, self.storage.all())

    def test_user_in_file_storage(self):
        """Test that FileStorage correctly serializes and deserializes User"""
        self.storage.new(self.user)
        self.storage.save()
        with open(self.test_file, "r") as f:
            content = f.read()
            self.assertIn("User", content)
            self.assertIn(self.user.email, content)

    def test_user_properties(self):
        new_user = User()
        self.assertEqual(new_user.email, "")
        self.assertEqual(new_user.password, "")
        self.assertEqual(new_user.first_name, "")
        self.assertEqual(new_user.last_name, "")

if __name__ == '__main__':
    unittest.main()
