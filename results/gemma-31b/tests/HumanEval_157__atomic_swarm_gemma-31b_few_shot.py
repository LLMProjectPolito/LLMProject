
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

def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True

def test_zero_sides():
    assert right_angle_triangle(0, 0, 0) == False

def test_right_angle_triangle_negative_sides():
    assert right_angle_triangle(-3, -4, -5) == False