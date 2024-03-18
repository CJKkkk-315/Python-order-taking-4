from Rectangle import Rectangle
from Point import Point
from Union import Union
from typing import List, Tuple
from itertools import chain

import unittest

"""
Test cases for the Union class.
"""


def assert_equal(got, expected, msg):
    """
    Simple assert helper
    """
    assert expected == got, "[{}] Expected: {}, got: {}".format(msg, expected, got)


def extract_points(rectangles: List[Rectangle]) -> List[Tuple[int, int]]:
    """
    Given a list of rectangles, convert it into a list of tuples representing the corners of the rectangles
    """
    return [
        pt.get_coordinates()
        for pt in chain.from_iterable(rect.get_points() for rect in rectangles)
    ]


class SampleUnionTestCases(unittest.TestCase):
    """
    Testing functionality of the Union class
    """

    def test_union_construction(self) -> None:
        """
        This is the provided test case from the assignment specs
        """
        # These are the rectangles we want to union
        rect1 = Rectangle(Point(-5, 5), Point(4, 1))
        rect2 = Rectangle(Point(-2, 3), Point(3, -4))
        rect3 = Rectangle(Point(-4, 2), Point(6, -2))

        union = Union([rect1, rect2, rect3])

        # Test that the union is constructed correctly
        actual = extract_points(union.get_union())
        expected = [
            (-5, 5),
            (4, 2),
            (-5, 2),
            (6, 1),
            (-4, 1),
            (6, -2),
            (-2, -2),
            (3, -4),
        ]
        assert_equal(actual, expected, "Union Construction")

        # Test some points and whether they're in the union
        assert_equal(union.contains(Point(0, 0)), True, "Union Contains Point")
        assert_equal(union.contains(Point(5, 5)), False, "Union Contains Point")
        assert_equal(union.contains(Point(-5, 5)), True, "Union Contains Point")
        assert_equal(union.contains(Point(4, 1)), True, "Union Contains Point")
        assert_equal(union.contains(Point(4, 0)), True, "Union Contains Point")
        assert_equal(union.contains(Point(4, -1)), True, "Union Contains Point")
        assert_equal(union.contains(Point(4, -2)), True, "Union Contains Point")
