#!/usr/bin/python3
""" reference list of assert methods: 
    Common assert methods used in unittest for reference.
"""

import io, os, contextlib, unittest, datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
from models.base_model import datetime


class TestBaseModelClass(unittest.TestCase):
    """Class containing testing functions for BaseModel"""

    @classmethod
    def setUpClass(cls):
        """Set up any state specific to the test case."""
        print("Setting up class resources for TestBaseModelClass...")
        cls.storage = FileStorage()
        cls.base = BaseModel()

    def setUp(self):
        """Set up any state tied to the execution of the test method."""
        print("Setting up for a test...")
        self.storage = FileStorage()
        self.storage.__objects = {}
        """     
    def tearDown(self):
        ##Clean up after each test method runs.
        print("Cleaning up after a test...")
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        
    @classmethod
    def tearDownClass(cls):
        ####Tear down any class-specific resources after all tests.
        print("Tearing down class resources for TestBaseModelClass...")
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)
        """
    def test_base_id(self):
        """Test if id is set on initialization"""
        self.assertIsNotNone(self.base.id)
        self.assertIsInstance(self.base.id, str)

    def test_to_dict(self):
        """Test to_dict method"""
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
        """Test BaseModel initialization from a dictionary."""
        data = {
            'id': '1234',
            'created_at': datetime,
            'updated_at': datetime
            }
        obj = BaseModel(**data)
        self.assertEqual(obj.id, '1234')
        self.assertEqual(obj.created_at.isoformat(timespec='seconds'), '2022-10-10T10:00:00')
        self.assertEqual(obj.updated_at.isoformat(timespec='seconds'), '2022-10-10T10:00:00')

    def test_base_model_save(self):
        """Test that BaseModel.save() updates updated_at and stores in storage."""
        last_update = self.base.updated_at
        self.base.save()
        self.assertNotEqual(last_update, self.base.updated_at)

    def test_base_id(self):
        """Test if id is set on initialization."""
        self.assertIsNotNone(self.base.id)

    def test__str__(self):
        """Test if __str__ returns the expected string format"""
        expected_str = "[BaseModel] ({}) {}".format(self.base.id, self.base.__dict__)
        self.assertEqual(str(self.base), expected_str)

    def test_init_from_kwargs(self):
        """Test initialization from kwargs"""
        date = "2022-10-10T10:00:00"
        data = {'id': '1234', 'created_at': date, 'updated_at': date}
        base = BaseModel(**data)
        self.assertEqual(base.id, '1234')
        self.assertEqual(base.created_at.isoformat(), date)
        self.assertEqual(base.updated_at.isoformat(), date)


if __name__ == '__main__':
    unittest.main()
