import pytest
import math


# Focus: Boundary Values
def is_right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    is_right_angle_triangle(3, 4, 5) == True
    is_right_angle_triangle(1, 2, 3) == False
    """
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2

# Focus: Type Scenarios
def is_right_triangle(a, b, c):
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2

# Focus: Logic Branches
def is_right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    is_right_angle_triangle(3, 4, 5) == True
    is_right_angle_triangle(1, 2, 3) == False
    """
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2