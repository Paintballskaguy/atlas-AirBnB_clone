#!/usr/bin/python3

import unittest, os, copy
from datetime import datetime
from uuid import uuid4
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """ working comment:
    public instance methods:
        save(self) 
            json serializes __objects into a __file_path
            check state of __file_path before and after
        reload(self)
            deserializes __file_path into __objects
            check state of __objects before and after
        construct_key(self, obj)
            returns a key_string
    check how this is integrated into BaseModel
        __init__ calls FileStorage.new(obj)
        save calls FileStorage.save()
    """

    @classmethod
    def setUpClass(cls):
        #if os.path.exists("file.json"):
        #    os.remove("file.json")
        cls.storage = FileStorage()
        cls.storage.all().clear()
        cls.test_file = "test_file.json"

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)

    def test_fs_properties(self):
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
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
        pass

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
