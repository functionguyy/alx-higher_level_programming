#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
from unittest.mock import patch


class InheritanceTestCase(unittest.TestCase):

    def setUp(self):
        self.square = Square(5)

    def test_square_object_is_instance_of_rectangle(self):
        self.assertIsInstance(self.square, Rectangle)


class IdAttrTestCase(unittest.TestCase):

    def test_id_is_not_none(self):
        """Square object id should not be None"""
        a = Square(5)
        self.assertIsNotNone(a.id)

    def test_id_specified(self):
        """Square object id should be the id passed if any"""
        a = Square(9, 15, id=3)
        self.assertEqual(a.id, 3)


class InstanceAttrTestCase(unittest.TestCase):

    def setUp(self):
        self.square = Square(5)

    def test_square_object_has_size_attr(self):
        """Square object should have size attribute"""
        self.assertTrue(hasattr(self.square, "size"), 'no size attribute')


class SizeAttrTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.square = Square(5)

    def test_getter_method(self):
        """obj.size should return value of size"""
        self.assertEqual(self.square.size, 5)

    def test_setter_method(self):
        """obj.size = value should change value of size"""
        self.square.size = 8
        self.assertEqual(self.square.size, 8)

    def test_string_input(self):
        """assigning to size should fail with string input"""
        with self.assertRaises(TypeError):
            Square("hello")

    def test_negative_input(self):
        """assigning to size should fail with negative integer input"""
        with self.assertRaises(ValueError):
            Square(-9)

    def test_float_input(self):
        """assigning to size should fail with float input"""
        with self.assertRaises(TypeError):
            Square(1.1)

    def test_bool_input(self):
        """assigning to size should fail with bool input"""
        with self.assertRaises(TypeError):
            Square(True)

    def test_zero_input(self):
        """assigning to size should fail with zero input"""
        with self.assertRaises(ValueError):
            Square(0)


class XAttrTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.square = Square(5, 4)

    def test_getter_method(self):
        """obj.x should return value of x"""
        self.assertEqual(self.square.x, 4)

    def test_setter_method(self):
        """obj.size = value should change value of x"""
        self.square.x = 6
        self.assertEqual(self.square.x, 6)

    def test_string_input(self):
        """assigning to x should fail with string input"""
        with self.assertRaises(TypeError):
            Square(7, "2")

    def test_negative_input(self):
        """assigning to x should fail with negative number input"""
        with self.assertRaises(ValueError):
            Square(5, -4)


class YAttrTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.square = Square(5, 4, 6)

    def test_getter_method(self):
        """obj.y should return value of y"""
        self.assertEqual(self.square.y, 6)

    def test_setter_method(self):
        """obj.y = value should change value of y"""
        self.square.y = 9
        self.assertEqual(self.square.y, 9)

    def test_string_input(self):
        """assigning to y should fail with string input"""
        with self.assertRaises(TypeError):
            Square(4, 7, "9")

    def test_negative_input(self):
        """assigning to y should fail with negative input"""
        with self.assertRaises(ValueError):
            Square(2, 3, -6)


class StrAttrTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.square = Square(5, 2, 3, 89)

    def test_str_attr_output(self):
        out = "[Square] (89) 2/3 - 5"

        with patch('sys.stdout', new=StringIO()) as output:
            print(self.square)
            print_out = output.getvalue().strip()
            self.assertEqual(print_out, out)


class UpdateAttrTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.square = Square(5)

    def test_update_with_no_args(self):

        a = self.square.id

        self.square.update()

        b = self.square.id

        self.assertEqual(a, b)
        self.assertEqual(self.square.size, 5)
        self.assertEqual(self.square.x, 0)
        self.assertEqual(self.square.y, 0)


if __name__ == "__main__":
    unittest.main()
