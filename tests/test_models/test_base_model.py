#!/usr/bin/python3
""" reference list of assert methods: 
    Common assert methods used in unittest for reference.
"""

import io, os, contextlib, unittest, datetime
from models.base_model import BaseModel
import models


class TestBaseModelClass(unittest.TestCase):
    """Class containing testing functions for BaseModel"""

    @classmethod
    def setUpClass(cls):
        """Set up any state specific to the test case."""
        print("Setting up class resources for TestBaseModelClass...")
        cls.test_file = "file.json"

    @classmethod
    def tearDownClass(cls):
        """Tear down any class-specific resources after all tests."""
        print("Tearing down class resources for TestBaseModelClass...")
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)

    def setUp(self):
        """Set up any state tied to the execution of the test method."""
        print("Setting up for a test...")
        self.base = BaseModel()

    def tearDown(self):
        """Clean up after each test method runs."""
        print("Cleaning up after a test...")
        del self.base

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

        created_at = datetime.datetime.fromisoformat(base_dict['created_at'])
        updated_at = datetime.datetime.fromisoformat(base_dict['updated_at'])
        self.assertIsInstance(created_at, datetime.datetime)
        self.assertIsInstance(updated_at, datetime.datetime)

    def test_base_model_init(self):
        """Test BaseModel initialization from a dictionary."""
        data = {
            'id': '1234',
            'created_at': '2022-10-10T10:00:00.000000',
            'updated_at': '2022-10-10T10:00:00.000000'
            }
        obj = BaseModel(**data)
        self.assertEqual(obj.id, '1234')
        expected_date = datetime.datetime(2022, 10, 10, 10, 0, 0, 0)
        self.assertEqual(obj.created_at, expected_date)
        self.assertEqual(obj.updated_at, expected_date)

    def test_base_model_save(self):
        """Test that BaseModel.save() updates updated_at and stores in storage."""
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(old_updated_at, obj.updated_at)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, models.storage.all())


    def test__str__(self):
        """Test if __str__ returns the expected string format"""
        expected_str = "[BaseModel] ({}) {}".format(self.base.id, self.base.__dict__)
        self.assertEqual(str(self.base), expected_str)

    def test_init_from_kwargs(self):
        """Test initialization from kwargs"""
        date = datetime.datetime.now().isoformat()
        data = {'id': '1234', 'created_at': date, 'updated_at': date}
        base = BaseModel(**data)
        self.assertEqual(base.id, '1234')
        self.assertEqual(base.created_at.isoformat(), date)
        self.assertEqual(base.updated_at.isoformat(), date)


if __name__ == '__main__':
    unittest.main()
