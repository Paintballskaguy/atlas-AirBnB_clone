#!/usr/bin/python3

import unittest
from datetime import datetime
from uuid import uuid4
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.storage = FileStorage()

    @classmethod
    def tearDownClass(cls):
        cls.storage.all().clear()

    def test_base__init__(self):
        base_obj = BaseModel()
        self.assertIsNotNone(base_obj.id)
        self.assertIsInstance(base_obj.id, str)
        self.assertIsInstance(base_obj.created_at, datetime)
        self.assertIsInstance(base_obj.updated_at, datetime)
        self.assertIn(base_obj, self.storage.all().values())

    def test_base__init__kwargs(self):
        time = datetime.now().isoformat()
        base_id = str(uuid4())
        kwargs = {'id': base_id, 'created_at': time, 'updated_at': time}
        base_obj = BaseModel(**kwargs)
        self.assertEqual(base_obj.id, base_id)
        self.assertEqual(base_obj.created_at.isoformat(), time)
        self.assertEqual(base_obj.updated_at.isoformat(), time)

    def test_base_to_dict(self):
        base_obj = BaseModel()
        base_dict = base_obj.to_dict()
        self.assertEqual(base_dict['__class__'], 'BaseModel')

    def test_base__str__(self):
        base_obj = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(base_obj.id, base_obj.__dict__)
        self.assertEqual(str(base_obj), expected_str)

    def test_base_save(self):
        base_obj = BaseModel()
        last_update = base_obj.updated_at
        base_obj.save()
        new_update = base_obj.updated_at
        self.assertNotEqual(last_update, new_update)

    """
    # in here, test that the data in file is different after the call to save()
    def test_base_storage_save(self):
        self.storage.reload()
        old_storage = self.storage.all().items()
        self.storage.reload()
        new_storage = self.storage.all().items()
        self.assertNotEqual(old_storage, new_storage)
        self.assertIn(key, self.storage.all().keys())
    """

if __name__ == '__main__':
    unittest.main()
