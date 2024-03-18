from typing import List
from Point import Point
from Rectangle import Rectangle

"""
Union Class
----------
This class represents a union of a sequence of rectangles in the Euclidean plane.
A union is defined as the total segment of area covered by two polygons.

A Union contains the following functions alongside an initialiser:
    - get_union() -> list[Rectangle]: Returns a list of Rectangles representing the union.
    - contains(Point) -> bool: Returns True if the given point is contained within the union, False otherwise.

It also contains the following class function:
    - merge_unions(Union, Union) -> List[Rectangles]: Returns the rectangles which make up the union of two Unions.
    
Your task is to complete the following functions which are marked by the TODO comment.
You are free to add properties and functions to the class as long as the given signatures remain identical.
"""


class Union:
    rectangles: List[Rectangle]

    @classmethod
    def merge_unions(cls, union1: "Union", union2: "Union") -> "Union":
        """
        Returns the Union of two Union objects.
        This should run in O(|union1| + |union2|) time
        :param union1: The first Union
        :param union2: The second Union
        :return: The list of rectangles making up the Union of the two Unions
        """
        return union1.rectangles + union2.rectangles
        # TODO: Add your code here!

    def __init__(self, rectangles: List[Rectangle]) -> None:
        print([[i.get_points()[0].get_coordinates(),i.get_points()[1].get_coordinates()] for i in rectangles])
        """
        The constructor for the Union class.
        Given a sequence of rectangles, use a divide and conquer algorithm to find the union.
        You should not edit this function.
        :param rectangles: The rectangles used to construct the union of the polygon
        """

        # This is the provided divide and conquer algorithm for finding the intersection of a sequence of rectangles.

        # We have 2 base cases here for if there are no rectangles or the union is just one rectangle
        if not len(rectangles) or len(rectangles) == 1:
            self.rectangles = rectangles
            return

        # Then merge the union of the the first half and second half of the rectangles (divide + merge step)
        self.rectangles = Union.merge_unions(
            Union(rectangles[: len(rectangles) // 2]),
            Union(rectangles[len(rectangles) // 2 :]),
        )

    def contains(self, point: Point) -> bool:
        """
        Returns True if the given point is contained within the Union, False otherwise.
        For standard students, this should be O(n) time.
        For advanced students, this should be O(logn) time.
        :param point: The point to check
        :return: True if the given point is contained within the Union, False otherwise.
        """
        for rect in self.rectangles:
            if rect.contains(point):
                return True
        return False

    def get_union(self) -> List[Rectangle]:
        """
        Returns a list of Points representing the coordinates of the union.
        Rectangles should be returned in a sorted order from top to bottom.
        :return: The Rectangles from top to bottom that make up the intersection.
        """
        return self.rectangles
        # TODO: Add your code here!
