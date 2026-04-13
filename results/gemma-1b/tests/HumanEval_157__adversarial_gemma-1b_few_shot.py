
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
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return a**2 + b**2 == c**2

def test_right_angle_triangle_positive():
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_negative():
    assert right_angle_triangle(1, 2, 3) == False

def test_right_angle_triangle_zero():
    assert right_angle_triangle(0, 4, 5) == False

def test_right_angle_triangle_invalid_sides():
    assert right_angle_triangle(1, 2, 4) == False

def test_right_angle_triangle_triangle_with_zero():
    assert right_angle_triangle(0, 0, 0) == False