#!/usr/bin/python3

import unittest, contextlib, io, os 
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModelClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.storage = FileStorage()
        cls.base = BaseModel()

    @classmethod
    def tearDownClass(cls):
        cls.storage.__objects.clear()
        del self.base

    def test_base_id_is_set(self):
        self.assertIsNotNone(self.base.id)
        self.assertIsInstance(self.base.id, str)

    def test_to_dict(self):
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
        date_str = '2022-10-10T10:00:00'
        data = {
            'id': '1234',
            'created_at': date_str,
            'updated_at': date_str
        }
        obj = BaseModel(**data)
        self.assertEqual(obj.created_at.isoformat(timespec='seconds'), '2022-10-10T10:00:00')
        self.assertEqual(obj.updated_at.isoformat(timespec='seconds'), '2022-10-10T10:00:00')

    # in here, test that the data in file is different after the call to save()
    def test_base_model_save(self):

        last_update = self.base.updated_at
        storage.reload()
        old_storage = storage.all().items()

        self.base.save()

        new_update = self.base.updated_at
        storage.reload()
        new_storage = storage.all().items()

        self.assertNotEqual(last_update, new_update)
        self.assertNotEqual(old_storage, new_storage)
        self.assertIn(key, self.storage.all().keys())

    def test__str__(self):
        expected_str = "[BaseModel] ({}) {}".format(self.base.id, self.base.__dict__)
        self.assertEqual(str(self.base), expected_str)

    def test_init_from_kwargs(self):
        date = "2022-10-10T10:00:00"
        data = {'id': '1234', 'created_at': date, 'updated_at': date}
        base = BaseModel(**data)
        self.assertEqual(base.id, '1234')
        self.assertEqual(base.created_at.isoformat(timespec='seconds'), date)
        self.assertEqual(base.updated_at.isoformat(timespec='seconds'), date)

if __name__ == '__main__':
    unittest.main()
