
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
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    sides = sorted([a, b, c])
    return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-6

def test_near_zero_sides():
    assert right_angle_triangle(1e-8, 1e-8, 1.41421356237e-8) == True

def test_zero_length_side():
    assert right_angle_triangle(0, 4, 5) == False

def test_floating_point_precision():
    assert right_angle_triangle(0.3, 0.4, 0.5) == True
    assert right_angle_triangle(3.0000001, 4.0, 5.0) == True
    assert right_angle_triangle(0.6, 0.8, 1.0) == True