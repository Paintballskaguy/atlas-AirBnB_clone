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
from models import storage

def setUpModule():
    print(storage)


class TestBaseModelClass(unittest.TestCase):
    """ class containing testing functions for Base class
    """
    def setUpClass():
        pass

    def test_base_id(self):
        base = BaseModel()
        self.assertIsNotNone(base.id)

    def test_to_dict(self):
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertEqual(base_dict,
                         {'__class__': 'BaseModel',
                          'id': base_dict.get('id'),
                          'created_at': base_dict.get('created_at'),
                          'updated_at': base_dict.get('updated_at') })

    def test_save(self):
        base = BaseModel()
        last_update = base.updated_at
        base.save()
        self.assertNotEqual(last_update, base.updated_at)

    def test__str__(self):
        base = BaseModel()
        self.assertEqual(base.__str__(), str(base))

if __name__== '__main__':
    unittest.main()
