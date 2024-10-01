#!/usr/bin/python3
"""Unit tests for the User class"""

import unittest, os
from models.user import User
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.storage = FileStorage()
        cls.test_file = "file.json"
        cls.user = User()

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)

    def test_user__init__(self):
        new_user = User()
        self.assertIsInstance(new_user, User)
        self.assertEqual(new_user.email, "")
        self.assertEqual(new_user.password, "")
        self.assertEqual(new_user.first_name, "")
        self.assertEqual(new_user.last_name, "")

    def test_user_to_dict(self):
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], "User")

    def test_user_save_reload(self):
        new_user = User()
        old_updated_at = new_user.updated_at
        key = f"User.{new_user.id}"

        new_user.save()
        self.storage.reload()

        self.assertNotEqual(old_updated_at, new_user.updated_at)
        self.assertIn(key, self.storage.all())

    def test_user_in_file_storage(self):
        self.storage.new(self.user)
        self.storage.save()
        with open(self.test_file, "r") as f:
            content = f.read()
            self.assertIn("User", content)
            self.assertIn(self.user.email, content)

if __name__ == '__main__':
    unittest.main()
