from Point import Point
from typing import Tuple

"""
Rectangle Class
----------
This class represents an individual rectangle in the Euclidean plane.
A rectangle is uniquely defined given a top-left point and a bottom-right point.
Each Rectangle is guaranteed to hold integer coordinates and are parallel to the axes.
A valid rectangle will always be intersected by the y-axis.

A Rectangle contains the following properties:
    - top_left: A Point representing the top-left corner of the rectangle
    - bottom_right: A Point representing the bottom-right corner of the rectangle

It also contains the following functions alongside an initialiser:
    - contains(Point) -> bool: Returns True if the given point is contained within the rectangle, False otherwise.
    - get_points() -> tuple[Point, Point]: Returns the top-left and bottom-right points of the rectangle as a tuple.

Your task is to complete the following functions which are marked by the TODO comment.
You are free to add properties and functions to the class as long as the given signatures remain identical.
"""


class Rectangle:
    # These are the defined properties as described above, feel free to add more if you wish!
    top_left: Point
    bottom_right: Point

    def __init__(self, top_left: Point, bottom_right: Point) -> None:
        """
        The constructor for the Rectangle class.
        :param top_left: A Point representing the top-left corner of the rectangle
        :param bottom_right: A Point representing the bottom-right corner of the rectangle
        :raises ValueError: If the given rectangle is invalid according to the above conditions
        """

        if not (top_left.x < bottom_right.x and top_left.y > bottom_right.y):
            raise ValueError('Invalid rectangle')

        self.top_left = top_left
        self.bottom_right = bottom_right

    def contains(self, point: Point) -> bool:
        """
        Returns True if the given point is contained within the rectangle, False otherwise.
        :param point: The point to check
        :return: True if the given point is contained within the rectangle, False otherwise.
        """

        return self.top_left.x <= point.x <= self.bottom_right.x and self.bottom_right.y <= point.y <= self.top_left.y

    def get_points(self) -> Tuple[Point, Point]:
        """
        Returns the top-left and bottom-right points of the rectangle.
        Do not modify this function.
        :return: A tuple of the top-left and bottom-right points of the rectangle in that order.
        """
        return (self.top_left, self.bottom_right)
