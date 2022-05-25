import unittest
from classes import Circle


class TestCircle(unittest.TestCase):

    def test_check_radio(self):

        self.assertRaises(Exception, Circle, -1)
        self.assertRaises(Exception, Circle, 0)
        circle = Circle(1)
        triggered = False
        try:
            circle.radio = 0
        except Exception as e:
            triggered = True
        self.assertTrue(triggered)
        self.assertEqual(1, circle.radio)
        triggered = False
        try:
            circle.radio = -1
        except Exception as e:
            triggered = True
        self.assertTrue(triggered)
        self.assertEqual(1, circle.radio)

    def test_print(self):
        circle = Circle(3)
        print(circle)

    def test_multiply(self):
        circle = Circle(1)
        new_circle = circle.multiply(3)
        self.assertEqual(3, new_circle.radio)
        self.assertRaises(Exception, circle.multiply, 0)
        self.assertRaises(Exception, circle.multiply, -2)

    def test_area_perimeter(self):
        circle = Circle(1.5)
        self.assertEqual("7.07", "%.2f" % circle.get_area())
        self.assertEqual("9.42", "%.2f" % circle.get_perimeter())
