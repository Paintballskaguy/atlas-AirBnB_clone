#!/usr/bin/python3

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Set up once before all tests in the class."""
        print("Setting up class resources for TestFileStorage...")
        cls.storage = FileStorage()
        cls.test_file = "test_file.json"

    @classmethod
    def tearDownClass(cls):
        """Tear down once after all tests in the class."""
        print("Tearing down class resources for TestFileStorage...")
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)

    def setUp(self):
        """Set up any state tied to the execution of the test method."""
        self.storage = FileStorage()
        self.base = BaseModel()
        FileStorage._FileStorage__objects = {}
        self.test_file = "test_file.json"
    
    def tearDown(self):
        """Tear down after each test method."""
        FileStorage._FileStorage__objects = {}
        self.storage._FileStorage__objects = {}

    def test_file_path(self):
        """Test that the file path is set correctly."""
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects_initially_empty(self):
        """Test that objects dictionary is initially empty."""
        self.assertEqual(self.storage._FileStorage__objects, {})

    def test_all_returns_objects(self):
        """Test that all() returns the __objects dictionary."""
        self.assertEqual(self.storage.all(), self.storage._FileStorage__objects)

    def test_new_adds_object(self):
        """Test that new() adds a new object to the storage."""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_save(self):
        """Test that save() creates the file and stores serialized objects."""
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload(self):
        """Test that reload() restores objects from file."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_base_model_init(self):
        """Test BaseModel initialization from a dictionary."""
        data = {
            'id': '1234',
            'created_at': '2022-10-10T10:00:00.000000',
            'updated_at': '2022-10-10T10:00:00.000000'
        }
        obj = BaseModel(**data)
        self.assertEqual(obj.id, '1234')
        self.assertEqual(obj.created_at.isoformat(timespec='seconds'), '2022-10-10T10:00:00')

    def test_base_model_save(self):
        """Test that BaseModel.save() updates updated_at and stores in storage."""
        last_update = self.storage.all()
        self.base.save()
        key = f"BaseModel.{self.base.id}"
        self.assertIn(key, self.storage.all())

if __name__ == '__main__':
    unittest.main()
