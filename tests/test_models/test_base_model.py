#!/usr/bin/python3

import unittest, contextlib, io, os 
from datetime import datetime
from uuid import uuid4
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """
    contained test
        test_base__init__
            self.id type str
            self.created_at type datetime
            self.updated_at type datetime
        test_base__init__kwargs
            if new instance make sure it is save in storage
        test_base__str__
            form "[{class}] ({id}) {__dict__}"
        test_base_save
            check self.updated_at is modified
            check it is stored in storage.all()
        test_base_to_dict
            analyze expected return
    """

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
        base_obj = BaseModel(**data)
        self.assertEqual(base_obj.id, base_id)
        self.assertEqual(base_obj.created_at.isoformat(), date)
        self.assertEqual(base_obj.updated_at.isoformat(), date)

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
        self.base.save()
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
