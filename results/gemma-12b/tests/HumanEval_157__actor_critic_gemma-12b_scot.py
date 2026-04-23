
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
    return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

def test_valid_right_triangle():
    assert right_angle_triangle(3, 4, 5) == True

def test_valid_right_triangle_float():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True

def test_invalid_triangle():
    assert right_angle_triangle(1, 2, 3) == False

def test_zero_side():
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 4, 0) == False

def test_negative_side():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False

def test_equal_sides():
    assert right_angle_triangle(3, 3, 5) == False
    assert right_angle_triangle(3, 4, 4) == False

def test_all_equal_sides():
    assert right_angle_triangle(3, 3, 3) == False

def test_large_numbers():
    assert right_angle_triangle(1000, 1000, 1414.21356) == True

def test_large_numbers_fail():
    assert right_angle_triangle(1000, 1000, 1400) == False

def test_permutation():
    assert right_angle_triangle(5, 3, 4) == True
    assert right_angle_triangle(4, 5, 3) == True
    assert right_angle_triangle(4, 3, 5) == True

def test_almost_right_triangle():
    assert right_angle_triangle(3.000001, 4.0, 5.0) == True
    assert right_angle_triangle(3.0, 4.000001, 5.0) == True
    assert right_angle_triangle(3.0, 4.0, 5.000001) == True
    assert right_angle_triangle(3.000001, 4.0, 4.999999) == False
    assert right_angle_triangle(2.999999, 4.0, 5.0) == False
    assert right_angle_triangle(3.0, 3.999999, 5.0) == False
    assert right_angle_triangle(3.0, 4.0, 4.999999) == False

def test_invalid_triangle_inequality():
    """
    Tests that the function correctly identifies triangles that violate the triangle inequality
    and are therefore not right triangles.
    """
    assert right_angle_triangle(1, 2, 5) == False

def test_non_right_integer_triangle():
    assert right_angle_triangle(5, 6, 7) == False

def test_tolerance_boundary():
    assert right_angle_triangle(3.0, 4.0, 5.00001) == False
    assert right_angle_triangle(3.0, 4.0, 4.99999) == False

def test_very_small_numbers():
    assert right_angle_triangle(0.0001, 0.0002, 0.0003) == False

def test_near_integer_values():
    assert right_angle_triangle(3.0, 4.0, 4.999999) == False