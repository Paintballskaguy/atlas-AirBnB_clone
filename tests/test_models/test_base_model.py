#!/usr/bin/python3
""" reference list of assert methods: 

    assertEqual(a, b)           a == b
    assertNotEqual(a, b)        a != b
    assertTrue(x)               bool(x) is True
    assertFalse(x)              bool(x) is False
    assertIs(a, b)              a is b
    assertIsNot(a, b)           a is not b
    assertIsNone(x)             a is None
    assertIsNotNone(x)          a is not None
    assertIn(a, b)              a in b
    assertNotIn(a, b)           a not in b
    assertIsInstance(a, b)      isinstance(a, b)
    assertNotIsInstance(a, b)   not isinstance(a, b)

    assertAlmostEqual(a, b)     round(a-b, 7) == 0
    assertNotAlmostEqual(a, b)  round(a-b, 7) != 0
    assertGreater(a, b)         a > b
    assertGreaterEqual(a, b)    a >= b
    assertLess(a, b)            a < b
    assertLessEqual(a, b)       a <= b
    assertRegex(s, r)           r.search(s)
    assertNotRegex(s, r)        not r.search(s)
    assertCountEqual(a, b)      a and b have the same number of each
                                element (regardless of order)

    assertRaises(exc, fun, *args, **kwds)
    assertRaisesRegex(exc, r, fun, *args, **kwds)
    assertWarns(warn, fun, *args, **kwds)
    assertWarnsRegex(warn, r, fun, *args, **kwds)
    assertLogs(logger, level)
"""


import io, os, contextlib, unittest, datetime
from models.base_model import BaseModel
# from models import storage

def setUpModule():
    test_obj = BaseModel()
    date = test_obj.created_at
    date_as_str = date.isoformat()
    print(type(date))
    print(type(date_as_str))
    print(test_obj.created_at)


class TestBaseModelClass(unittest.TestCase):
    """Class containing testing functions for BaseModel"""

    @classmethod
    def setUpClass(cls):
        """Set up any state specific to the test case."""
        cls.base = BaseModel()

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

        # Check if datetime fields are in ISO format
        created_at = datetime.datetime.fromisoformat(base_dict['created_at'])
        updated_at = datetime.datetime.fromisoformat(base_dict['updated_at'])
        self.assertIsInstance(created_at, datetime.datetime)
        self.assertIsInstance(updated_at, datetime.datetime)

    def test_save(self):
        """Test if save method updates the updated_at field"""
        last_update = self.base.updated_at
        self.base.save()
        self.assertNotEqual(last_update, self.base.updated_at)
        self.assertTrue(self.base.updated_at > last_update)

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