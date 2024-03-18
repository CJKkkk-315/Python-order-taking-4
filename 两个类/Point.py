from typing import Tuple

"""
Point Class
----------
This class represents an individual point in the Euclidean plane.
Each Point is guaranteed to hold integer coordinates.
A Point contains the following properties:
    - x: The integer coordinate along the x-axis of the Point
    - y: The integer coordinate along the y-axis of the Point
It also contains other relevant getter functions for the above properties.
You are free to add properties and functions to the class as long as the given signatures remain identical.

--->THIS CLASS DOES NOT NEED ANY MODIFICATION AND CAN BE USED AS IS.<---
"""


class Point:
    # These are the defined properties as described above, feel free to add more if you wish!
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        """
        The constructor for the Point class.
        :param x: The integer coordinate along the x-axis of the Point
        :param y: The integer coordinate along the y-axis of the Point
        """
        self.x = x
        self.y = y

    def get_coordinates(self) -> Tuple[int, int]:
        """
        Gets the coordinates of the Point.
        :return: A tuple of the coordinates of the Point in the form (x, y)
        """
        return (self.x, self.y)
