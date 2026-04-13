
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
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2

def test_valid_right_triangle():
    assert right_angle_triangle(3, 4, 5) == True

def test_another_valid_right_triangle():
    assert right_angle_triangle(5, 12, 13) == True

def test_valid_right_triangle_float():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True

def test_invalid_triangle():
    assert right_angle_triangle(1, 2, 3) == False

def test_isosceles_right_triangle():
    assert right_angle_triangle(1, 1, 2**0.5) == True

def test_equilateral_triangle():
    assert right_angle_triangle(5, 5, 5) == False

def test_zero_side():
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 4, 0) == False

def test_negative_side():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False

def test_large_sides():
    assert right_angle_triangle(1000, 1000, 1000 * (2**0.5)) == True

def test_large_numbers():
    assert right_angle_triangle(10000, 10000, 14142.1356237) == True

def test_mixed_types():
    assert right_angle_triangle(3, 4.0, 5) == True
    assert right_angle_triangle(3.0, 4, 5) == True

def test_almost_right_triangle():
    assert right_angle_triangle(3.0000001, 4.0, 5.0) == True
    assert right_angle_triangle(3.0, 4.0000001, 5.0) == True
    assert right_angle_triangle(3.0, 4.0, 5.0000001) == True

def test_equal_sides_not_right():
    assert right_angle_triangle(2, 2, 3) == False