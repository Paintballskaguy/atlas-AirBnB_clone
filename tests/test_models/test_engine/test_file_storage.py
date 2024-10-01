#!/usr/bin/python3

import unittest, os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ working comment:

    private class attributes:
        __file_path = "file.json"
        __objects = {}

    public instance methods:
        all(self) 
            returns __objects
        new(self, obj) 
            __objects.update({key: obj})
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
        print("Setting up class resources for TestFileStorage...")
        cls.storage = FileStorage()
        cls.test_file = "test_file.json"

    @classmethod
    def tearDownClass(cls):
        print("Tearing down class resources for TestFileStorage...")
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)

    def setUp(self):
        self.storage = FileStorage()
        self.base = BaseModel()
        FileStorage._FileStorage__objects = {}
        self.test_file = "test_file.json"
    
    def tearDown(self):
        FileStorage._FileStorage__objects = {}
        self.storage._FileStorage__objects = {}

    def test_file_path(self):
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects_initially_empty(self):
        self.assertEqual(self.storage._FileStorage__objects, {})

    def test_all_returns_objects(self):
        self.assertEqual(self.storage.all(), self.storage._FileStorage__objects)

    def test_new_adds_object(self):
        obj = BaseModel()
        self.storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_save(self):
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_base_model_init(self):
        data = {
            'id': '1234',
            'created_at': '2022-10-10T10:00:00.000000',
            'updated_at': '2022-10-10T10:00:00.000000'
        }
        obj = BaseModel(**data)
        self.assertEqual(obj.id, '1234')
        self.assertEqual(obj.created_at.isoformat(timespec='seconds'), '2022-10-10T10:00:00')

    def test_base_model_save(self):
        last_update = self.storage.all()
        self.base.save()
        key = f"BaseModel.{self.base.id}"
        self.assertIn(key, self.storage.all())

if __name__ == '__main__':
    unittest.main()
