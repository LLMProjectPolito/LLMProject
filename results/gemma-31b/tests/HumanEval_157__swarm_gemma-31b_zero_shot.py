
def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''

import pytest
import math

def test_right_angle_triangle_unordered():
    # Tests if the function correctly identifies a right-angled triangle 
    # when the hypotenuse is not the last argument.
    assert right_angle_triangle(5, 3, 4) is True

def test_right_angle_triangle_negative_sides():
    # A right-angled triangle cannot have negative side lengths, 
    # even if they satisfy the Pythagorean theorem (-3^2 + -4^2 = -5^2).
    assert right_angle_triangle(-3, -4, -5) is False