#!/usr/bin/python3
import unittest
from models.base import Base


class IdAttributeTestCase(unittest.TestCase):

    def test_id_is_assigned(self):
        """argument passed should be the assigned id"""
        a = Base(2)
        self.assertEqual(2, a.id)

    def test_auto_id_is_assigned(self):
        """id should be auto-generated for instance without specified id"""
        b = Base()
        self.assertEqual(b.id, 1)


if __name__ == "__main__":
    unittest.main()
