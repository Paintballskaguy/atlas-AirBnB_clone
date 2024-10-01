#!/usr/bin/python3
"""Unit tests for the User class"""

import unittest, os
from models.user import User
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = User()
        cls.user.email = "test@mail.com"
        cls.user.first_name = "John"
        cls.user.last_name = "Doe"
        cls.user.password = "password123"
        cls.test_file = "file.json"
        cls.storage = FileStorage()

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)

    def setUp(self):
        self.user = TestUser.user

    def test_user__init__(self):
        self.assertIsInstance(self.user, User)

    def test_user_to_dict(self):
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], "User")

    def test_user_save(self):
        old_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(old_updated_at, self.user.updated_at)
        self.assertTrue(self.user.updated_at > old_updated_at)

    def test_user_file_storage_save_reload(self):
        my_user = User()
        my_user.save()
        key = f"User.{my_user.id}"
        self.storage.reload()
        self.assertIn(key, self.storage.all())

    def test_user_in_file_storage(self):
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
