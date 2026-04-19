
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

def test_right_angle_triangle_unordered_hypotenuse():
    """
    Test that the function correctly identifies a right-angled triangle 
    even when the hypotenuse is not the last argument provided.
    """
    assert right_angle_triangle(5, 3, 4) is True

def test_right_angle_triangle_unordered_floats():
    """
    Tests the function with floating point numbers where the hypotenuse 
    is not the last argument provided.
    2.5^2 + 6.0^2 = 6.25 + 36.0 = 42.25
    6.5^2 = 42.25
    """
    assert right_angle_triangle(2.5, 6.5, 6.0) is True