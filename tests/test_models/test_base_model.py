#!/usr/bin/python3

import unittest, os
from datetime import datetime
from uuid import uuid4
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.storage = FileStorage()
        cls.json_file = "file.json"

    @classmethod
    def tearDownClass(cls):
        cls.storage.all().clear()

    def test_base__init__(self):
        base_obj = BaseModel()
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

    def test_base_storage_save(self):
        with open(self.json_file, 'r') as json_file:
            old_json = json_file.read()

        base_obj = BaseModel()
        base_obj.save()

        with open(self.json_file, 'r') as json_file:
            new_json = json_file.read()

        self.assertNotEqual(old_json, new_json)

if __name__ == '__main__':
    unittest.main()
