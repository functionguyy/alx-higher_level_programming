#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from unittest.mock import patch


class InheritanceTestCase(unittest.TestCase):

    def test_rectangle_object_is_instance_of_base(self):
        b = Rectangle(1, 2)
        self.assertIsInstance(b, Base)


class InstanceAttrTestCase(unittest.TestCase):

    def test_rectangle_object_has_width_attr(self):
        """Rectangle object should have width attribute"""
        a = Rectangle(2, 6)
        self.assertTrue(hasattr(a, "width"), 'no width attribute')

    def test_rectangle_object_has_height_attr(self):
        """Rectangle object should have height attribute"""
        b = Rectangle(5, 10)
        self.assertTrue(hasattr(b, "height"), 'no height attribute')

    def test_rectangle_object_has_id_attr(self):
        """Rectangle object should have id attribute"""
        b = Rectangle(5, 5)
        self.assertTrue(hasattr(b, "id"), 'no id attribute')

    def test_rectangle_object_has_x_attr(self):
        """Rectangle object should have x attribute"""
        c = Rectangle(8, 10)
        self.assertTrue(hasattr(c, "x"), 'no x attribute')

    def test_rectangle_object_has_y_attr(self):
        """Rectangle object should have x attribute"""
        c = Rectangle(8, 10)
        self.assertTrue(hasattr(c, "y"), 'no y attribute')

    def test_rectangle_object_has_area_attr(self):
        """Rectangle object should have area attribute"""
        c = Rectangle(8, 10)
        self.assertTrue(hasattr(c, "area"), 'no area attribute')

    def test_rectangle_object_has_display_attr(self):
        """Rectangle object should have display attribute"""
        c = Rectangle(8, 10)
        self.assertTrue(hasattr(c, "display"), 'no display attribute')


class IdAttrTestCase(unittest.TestCase):

    def test_id_is_not_none(self):
        """Rectangle object id should not be None"""
        a = Rectangle(8, 10)
        self.assertIsNotNone(a.id)

    def test_id_specified(self):
        """Rectangle object id should be the id passed if any"""
        a = Rectangle(9, 15, id=3)
        self.assertEqual(a.id, 3)


class WidthAttrTestCase(unittest.TestCase):

    def test_getter_method(self):
        """obj.width should return value of width"""
        d = Rectangle(3, 8)
        self.assertEqual(d.width, 3)

    def test_setter_method(self):
        """obj.width = value should change value of width"""
        d = Rectangle(4, 7)
        d.width = 2
        self.assertEqual(d.width, 2)

    def test_string_input(self):
        """assigning to width should fail with string input"""
        a = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            a.width = "hello"

    def test_negative_input(self):
        """assigning to width should fail with negative input"""
        a = Rectangle(8, 5)
        with self.assertRaises(ValueError):
            a.width = -1

    # test float input
    def test_float_input(self):
        """assigning to width should fail with float input"""
        d = Rectangle(1, 8)
        with self.assertRaises(TypeError):
            d.width = 1.0

    # test list input
    def test_list_input(self):
        """assigning to width should fail with list input"""
        d = Rectangle(3, 6)
        with self.assertRaises(TypeError):
            d.width = [2, 4, 5]

    # test bool input
    def test_list_input(self):
        """assigning to width should fail with list input"""
        d = Rectangle(3, 6)
        with self.assertRaises(TypeError):
            d.width = True


class HeightAttrTestCase(unittest.TestCase):

    def test_getter_method(self):
        """obj.height should return value of height"""
        a = Rectangle(3, 9)
        self.assertEqual(a.height, 9)

    def test_setter_method(self):
        """obj.height = value shold change value of height"""
        a = Rectangle(3, 10)
        a.height = 5
        self.assertEqual(a.height, 5)

    def test_string_input(self):
        """assigning to height should fail with string input"""
        a = Rectangle(8, 20)
        with self.assertRaises(TypeError):
            a.height = "boy"

    def test_negative_input(self):
        """assigning to height should fail with negative input"""
        a = Rectangle(2, 6)
        with self.assertRaises(ValueError):
            a.height = -9

    def test_zero_input(self):
        """assigning to height should fail with zero input"""
        a = Rectangle(4, 8)
        with self.assertRaises(ValueError):
            a.height = 0


class XAttrTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.rectangle = Rectangle(3, 8)

    def test_getter_method(self):
        """obj.x should return value of x"""
        # d = Rectangle(3, 8)
        self.assertEqual(self.rectangle.x, 0)

    def test_setter_method(self):
        """obj.x = value should change value of x"""
        # d = Rectangle(4, 7)
        self.rectangle.x = 2
        self.assertEqual(self.rectangle.x, 2)

    def test_string_input(self):
        """assigning to x should fail with string input"""
        # d = Rectangle
        with self.assertRaises(TypeError):
            self.rectangle.x = "test"

    def test_negative_input(self):
        """assigning to x should fail with negative input"""
        with self.assertRaises(ValueError):
            self.rectangle.x = -5


class YAttrTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.rectangle = Rectangle(4, 7)

    def test_getter_method(self):
        """obj.y should return value of y"""
        # d = Rectangle(3, 8)
        self.assertEqual(self.rectangle.y, 0)

    def test_setter_method(self):
        """obj.y = value should change value of y"""
        # d = Rectangle(4, 7)
        self.rectangle.y = 10
        self.assertEqual(self.rectangle.y, 10)

    def test_string_input(self):
        """assigning to y should fail with string  input"""
        with self.assertRaises(TypeError):
            self.rectangle.y = "new"

    def test_negative_input(self):
        """assigning to y should fail with negative input"""
        with self.assertRaises(ValueError):
            self.rectangle.y = -3


class AreaAttrTestCase(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(4, 10)

    def test_output(self):
        """obj.area() should return a value equal to obj.width * obj.height"""
        self.assertEqual(self.rectangle.area(), 4 * 10)


class DisplayAttrTestCase(unittest.TestCase):

    def test_display_rectangle(self):

        r = Rectangle(4, 6)
        out = ("####\n" +
               "####\n" +
               "####\n" +
               "####\n" +
               "####\n" +
               "####\n")

        with patch('sys.stdout', new=StringIO()) as output:
            r.display()
            printed_output = output.getvalue()
            self.assertEqual(printed_output, out)

    def test_display_rectangle_height_one(self):

        r = Rectangle(4, 1)
        out = ("####\n")

        with patch('sys.stdout', new=StringIO()) as output:
            r.display()
            printed_out = output.getvalue()
            self.assertEqual(printed_out, out)

    def test_display_aligned_rectangle(self):
        r = Rectangle(2, 3, 2, 2)
        out = ("\n"     +
               "\n"     +
               "  ##\n" +
               "  ##\n" +
               "  ##\n")

        with patch('sys.stdout', new=StringIO()) as output:
            r.display()
            printed_out = output.getvalue()
            self.assertEqual(printed_out, out)


class StrAttrTestCase(unittest.TestCase):
    def test_str_attr_output(self):
        r = Rectangle(4, 6, 2, 1, 12)
        out = "[Rectangle] (12) 2/1 - 4/6"

        with patch('sys.stdout', new=StringIO()) as output:
            print(r)
            print_out = output.getvalue().strip()
            self.assertEqual(print_out, out)


if __name__ == "__main__":
    unittest.main()
