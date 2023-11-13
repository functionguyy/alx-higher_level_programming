#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.square import Square


class InheritanceTestCase(unittest.TestCase):

    def test_square_object_is_instance_of_rectangle(self):
        a = Square(5)
        self.assertIsInstance(a, Rectangle)


if __name__ == "__main__":
    unittest.main()
