from Rectangle import Rectangle
from Point import Point
import unittest

"""
Test cases for the Rectangle class.
"""


def assert_equal(got, expected, msg):
    """
    Simple assert helper
    """
    assert expected == got, "[{}] Expected: {}, got: {}".format(msg, expected, got)


class SampleRectangleTestCases(unittest.TestCase):
    """
    Testing functionality of the Rectangle class
    """

    def test_rectangle_construction(self) -> None:
        """
        This makes a rectangle and check it contains a point
        """
        rect = Rectangle(Point(-5, 1), Point(1, -4))

        assert_equal(rect.contains(Point(-2, 0)), True, "Rectangle Contains")
        assert_equal(rect.contains(Point(2, 0)), False, "Rectangle Contains")
