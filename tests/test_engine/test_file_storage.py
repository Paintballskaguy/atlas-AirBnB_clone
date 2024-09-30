#!/usr/bin/python3

import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    
    def test_file_path(self):
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__file_path, "file.json")
        
    def test_objects_initially_empty(self):
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__objects, {})
        
    def test_alll_returns_objects(self):
        storage = FileStorage()
        self.assertEqual(storage.all(), storage.__FileStorage__objects)
        
    def test_new_adds_object(self):
        from models.base_model import BaseModel
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key], obj)
        
    def test_save(self):
        from models.base_model import BaseModel
        import os
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        
        self.assertTrue(os.path.exists("file.json"))
        
    def test_reload(self):
        from models. base_model import BaseModel
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        storage.__FileStorage__objects = {}
        storage.reload()
        
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, storage.all())
        
    def test_base_model_init(self):
        from models.base_model import BaseModel
        data = {
            'id': '1234',
            'created_at': '2022-10-10T10:00:00.000000'
            'updated_at': '2022-10-10T10:00:00.000000'
        }
        obj = BaseModel(**data)
        self.assertEqual(obj.id, '1234')
        self.assertEqual(str(obj.created_at), '2022-10-10T10:00:00.000000')
        
    def test_base_model_save(self):
        from models.base_model import BaseModel
        storage = FileStorage()
        obj = BaseModel()
        old_update_at = obj.updated_at
        obj.save()
        
        self.assertNotEqual(obj.updated_at, old_update_at)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, storage.all())
        