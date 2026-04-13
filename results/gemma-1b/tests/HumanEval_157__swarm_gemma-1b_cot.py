
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

def right_angle_triangle(a, b, c):
    """
    Checks if a triangle with sides a, b, and c is a right triangle.
    """
    sides = sorted([a, b, c])
    a, b, c = sides[0], sides[1], sides[2]
    return a**2 + b**2 == c**2

def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(0, 0, 0) == True
    assert right_angle_triangle(0, 1, 1) == False
    assert right_angle_triangle(1, 0, 1) == False
    assert right_angle_triangle(1, 1, 0) == True

def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(0, 0, 0) == True
    assert right_angle_triangle(0, 1, 1) == False
    assert right_angle_triangle(1, 0, 1) == False
    assert right_angle_triangle(1, 1, 0) == True

def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(0, 0, 0) == True
    assert right_angle_triangle(0, 1, 1) == False
    assert right_angle_triangle(1, 0, 1) == False
    assert right_angle_triangle(1, 1, 0) == True