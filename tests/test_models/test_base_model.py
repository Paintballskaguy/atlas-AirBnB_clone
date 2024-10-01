#!/usr/bin/python3

import unittest, contextlib, io, os 
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """
    contained test
        test_base__init__
        test_base__str__
        test_base_save
        test_base_to_dict
    """

    @classmethod
    def setUpClass(cls):
        cls.storage = FileStorage()
        cls.base = BaseModel()

    def test_base__init__(self):
        base = BaseModel()
        self.assertIsNotNone(base.id)
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)

    def test_base__init__kwargs(self):
        date = "2022-10-10T10:00:00"
        data = {'id': '1234', 'created_at': date, 'updated_at': date}
        base = BaseModel(**data)
        self.assertEqual(base.id, '1234')
        self.assertEqual(base.created_at.isoformat(timespec='seconds'), date)
        self.assertEqual(base.updated_at.isoformat(timespec='seconds'), date)

    def test_to_dict(self):
        base_dict = self.base.to_dict()
        self.assertEqual(base_dict['__class__'], 'BaseModel')

    def test__str__(self):
        expected_str = "[BaseModel] ({}) {}".format(self.base.id, self.base.__dict__)
        self.assertEqual(str(self.base), expected_str)

    # in here, test that the data in file is different after the call to save()
    def test_base_model_save(self):
        last_update = self.base.updated_at
        self.storage.reload()
        old_storage = self.storage.all().items()

        self.base.save()

        new_update = self.base.updated_at
        self.storage.reload()
        new_storage = self.storage.all().items()

        self.assertNotEqual(last_update, new_update)
        self.assertNotEqual(old_storage, new_storage)
        self.assertIn(key, self.storage.all().keys())

if __name__ == '__main__':
    unittest.main()
