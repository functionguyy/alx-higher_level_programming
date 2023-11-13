#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
from unittest.mock import patch


class InheritanceTestCase(unittest.TestCase):

    def test_square_object_is_instance_of_rectangle(self):
        a = Square(5)
        self.assertIsInstance(a, Rectangle)


class IdAttrTestCase(unittest.TestCase):

    def test_id_is_not_none(self):
        """Square object id should not be None"""
        a = Square(5)
        self.assertIsNotNone(a.id)

    def test_id_specified(self):
        """Square object id should be the id passed if any"""
        a = Square(9, 15, id=3)
        self.assertEqual(a.id, 3)

    def test_negative_id_input(self):
        """assigning to id should fail with negative input"""
        with self.assertRaises(ValueError):
            a = Square(5, id=-2)

class InstanceAttrTestCase(unittest.TestCase):

    def test_square_object_has_size_attr(self):
        """Square object should have size attribute"""
        a = Square(5)
        self.assertTrue(hasattr(a, "size"), 'no size attribute')
class SizeAttrTestCase(unittest.TestCase):

    def test_getter_method(self):
        """obj.size should return value of size"""
        a = Square(5)
        self.assertEqual(a.size, 5)

    def test_setter_method(self):
        """obj.size = value should change value of size"""
        a = Square(5)
        a.size = 8
        self.assertEqual(a.size, 8)

    def test_string_input(self):
        """assigning to size should fail with string input"""
        with self.assertRaises(TypeError):
            a = Square("hello")

    def test_negative_input(self):
        """assigning to size should fail with negative integer input"""
        with self.assertRaises(ValueError):
            a = Square(-9)

    def test_float_input(self):
        """assigning to size should fail with float input"""
        with self.assertRaises(TypeError):
            a = Square(1.1)

    def test_bool_input(self):
        """assigning to size should fail with bool input"""
        with self.assertRaises(TypeError):
            a = Square(True)

    def test_zero_input(self):
        """assigning to size should fail with zero input"""
        with self.assertRaises(ValueError):
            a = Square(0)


class XAttrTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.square = Square(5)

    def test_string_input(self):
        """assigning to x should fail with string input"""
        with self.assertRaises(TypeError):
            self.square.x = "test"

    def test_negative_input(self):
        """assigning to x should fail with string input"""
        with self.assertRaises(ValueError):
            self.square.x = -5


class YAttrTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.square = Square(5)

    def test_string_input(self):
        """assigning to y should fail with string input"""
        with self.assertRaises(TypeError):
            self.square.y = "new"

    def test_negative_input(self):
        """assigning to y should fail with negative input"""
        with self.assertRaises(ValueError):
            self.square.y = -3


class StrAttrTestCase(unittest.TestCase):

    def test_str_attr_output(self):
        s = Square(5, 2, 3, 89)
        out = "[Square] (89) 2/3 - 5"

        with patch('sys.stdout', new=StringIO()) as output:
            print(s)
            print_out = output.getvalue().strip()
            self.assertEqual(print_out, out)


if __name__ == "__main__":
    unittest.main()
