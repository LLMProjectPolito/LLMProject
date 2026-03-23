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
    return sides[0]**2 + sides[1]**2 == sides[2]**2

def test_right_angle():
    assert right_angle_triangle(3, 4, 5) == True

def test_not_right_angle():
    assert right_angle_triangle(1, 2, 3) == False

def test_equal_sides():
    assert right_angle_triangle(5, 5, 6) == True

def test_equal_sides_2():
    assert right_angle_triangle(5, 12, 13) == True

def test_equal_sides_3():
    assert right_angle_triangle(7, 24, 25) == True