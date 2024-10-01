#!/usr/bin/python3

import unittest, os
from datetime import datetime
from uuid import uuid4
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """ working comment:

    save(self) 
        json serializes __objects into a __file_path
        check state of __file_path before and after

    reload(self)
        deserializes __file_path into __objects
        check state of __objects before and after

    check how this is integrated into BaseModel
        __init__ calls FileStorage.new(obj)
        save calls FileStorage.save()
    """

    @classmethod
    def setUpClass(cls):
        cls.storage = FileStorage()
        cls.json_file = "file.json"
        if os.path.exists(cls.json_file):
            os.remove(cls.json_file)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.json_file):
            os.remove(cls.json_file)

    def test_fs_properties(self):
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.storage.all().clear()
        self.assertEqual(self.storage.all(), {})

    def test_fs_all(self):
        self.assertIsNotNone(self.storage.all())

    def test_fs_new(self):
        time = datetime.now().isoformat()
        base_id = str(uuid4())
        kwargs = {'id': base_id, 'created_at': time, 'updated_at': time}

        new = BaseModel(**kwargs)
        key = self.storage.construct_key(new)

        self.assertNotIn(key, self.storage.all().keys())
        self.storage.new(new)
        self.assertIn(key, self.storage.all().keys())

    def test_fs_save(self):
        self.assertFalse(os.path.exists(self.storage._FileStorage__file_path))
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_fs_reload(self):
        self.storage.all().clear()
        old_state = self.storage.all()
        new = BaseModel()
        new.save()
        self.storage.reload()
        new_state = self.storage.all()
        self.assertNotEqual(new_state, old_state)

    """
    def test_fs_construct_key(self):
        new = BaseModel()
        key = self.storage.construct_key(new)
        self.assertEqual

    def test_reload(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
    """

if __name__ == '__main__':
    unittest.main()
