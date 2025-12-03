"""
Module for geometric calculations.
"""


import math


def area_of_rectangle(length, breadth):
    """
    Calculate the area of a rectangle.

    Args:
        length (float or int): The length of the rectangle.
        breadth (float or int): The breadth of the rectangle.

    Returns:
        float or int: The area of the rectangle.
    """
    return length * breadth


def area_of_circle(radius):
    """
    Calculate the area of a circle.

    Args:
        radius (float or int): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return math.pi * radius**2
