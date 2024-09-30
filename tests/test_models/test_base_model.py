#!/usr/bin/python3
"""Unittest module for BaseModel class."""

import io
import os
import contextlib
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models


class TestBaseModelClass(unittest.TestCase):
    """Class containing testing functions for BaseModel."""

    @classmethod
    def setUpClass(cls):
        """Set up any state specific to the test case."""
        print("Setting up class resources for TestBaseModelClass...")
        cls.storage = FileStorage()
        cls.base = BaseModel()

    def setUp(self):
        """Set up any state tied to the execution of the test method."""
        print("Setting up for a test...")
        self.storage = FileStorage()
        self.storage.__objects = {}
        self.base = BaseModel()

    def test_base_id_is_set(self):
        """Test if id is set on initialization."""
        self.assertIsNotNone(self.base.id)
        self.assertIsInstance(self.base.id, str)

    def test_to_dict(self):
        """Test to_dict method."""
        base_dict = self.base.to_dict()
        self.assertEqual(base_dict['__class__'], 'BaseModel')
        self.assertEqual(base_dict['id'], self.base.id)
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

        created_at = datetime.fromisoformat(base_dict['created_at'])
        updated_at = datetime.fromisoformat(base_dict['updated_at'])
        self.assertIsInstance(created_at, datetime)
        self.assertIsInstance(updated_at, datetime)

    def test_base_model_init(self):
        """Test BaseModel initialization from a dictionary."""
        date_str = '2022-10-10T10:00:00'
        data = {
            'id': '1234',
            'created_at': date_str,
            'updated_at': date_str
        }
        obj = BaseModel(**data)
        self.assertEqual(obj.created_at.isoformat(timespec='seconds'), '2022-10-10T10:00:00')
        self.assertEqual(obj.updated_at.isoformat(timespec='seconds'), '2022-10-10T10:00:00')

    def test_base_model_save(self):
        """Test that BaseModel.save() updates updated_at and stores in storage."""
        last_update = self.base.updated_at
        self.base.save()
        new_update = self.base.updated_at
        print("Storage contents after saving BaseModel:", self.storage.all())
        key = f"BaseModel.{self.base.id}"
        print("Expected key:", key)
        self.assertIn(key, self.storage.all().keys())
        self.assertNotEqual(last_update, new_update)

    def test__str__(self):
        """Test if __str__ returns the expected string format."""
        expected_str = "[BaseModel] ({}) {}".format(self.base.id, self.base.__dict__)
        self.assertEqual(str(self.base), expected_str)

    def test_init_from_kwargs(self):
        """Test initialization from kwargs."""
        date = "2022-10-10T10:00:00"
        data = {'id': '1234', 'created_at': date, 'updated_at': date}
        base = BaseModel(**data)
        self.assertEqual(base.id, '1234')
        self.assertEqual(base.created_at.isoformat(timespec='seconds'), date)
        self.assertEqual(base.updated_at.isoformat(timespec='seconds'), date)


if __name__ == '__main__':
    unittest.main()
