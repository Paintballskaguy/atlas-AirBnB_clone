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

    @classmethod
    def tearDownClass(cls):
        """Tear down once after all tests in the class."""
        print("Tearing down class resources for TestFileStorage...")
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)

    def setUp(self):
        """Set up before each test method."""
        print("Setting up before a test...")
        self.storage = TestFileStorage.storage
        self.storage.__objects = {}

    def tearDown(self):
        """Tear down after each test method."""
        print("Tearing down after a test...")
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
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.test_file))

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
        self.assertEqual(str(obj.created_at), '2022-10-10T10:00:00.000000')

    def test_base_model_save(self):
        """Test that BaseModel.save() updates updated_at and stores in storage."""
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()

        self.assertNotEqual(obj.updated_at, old_updated_at)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())


if __name__ == '__main__':
    unittest.main()
