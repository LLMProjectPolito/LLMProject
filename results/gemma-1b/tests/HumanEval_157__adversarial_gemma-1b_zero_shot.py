
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
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2

def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(1, 1, 1) == True

def test_right_angle_triangle_degenerate():
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(4, 0, 5) == False
    assert right_angle_triangle(5, 0, 4) == False

def test_right_angle_triangle_large_numbers():
    assert right_angle_triangle(1000, 1000, 1000) == True
    assert right_angle_triangle(1, 1000, 1000) == False
    assert right_angle_triangle(1000, 1, 1000) == False

def test_right_angle_triangle_negative_sides():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False
    assert right_angle_triangle(-3, -4, 5) == False
    assert right_angle_triangle(-3, -4, -5) == False