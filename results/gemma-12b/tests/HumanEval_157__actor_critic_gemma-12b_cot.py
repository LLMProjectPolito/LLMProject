
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

def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True

def test_right_angle_triangle_invalid():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 3, 4) == False

def test_right_angle_triangle_negative_values():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False

def test_right_angle_triangle_zero_values():
    assert right_angle_triangle(0, 0, 0) == False

def test_right_angle_triangle_equal_sides_not_right():
    assert right_angle_triangle(2, 2, 3) == False
    assert right_angle_triangle(5, 5, 8) == False

def test_right_angle_triangle_float_values():
    rel_tolerance = 1e-5
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(1.0, 2.0, 3.0) == False
    assert right_angle_triangle(0.5, 0.75, 1.0) == True
    assert right_angle_triangle(1.0, 1.0, pytest.approx(1.41421, rel=rel_tolerance)) == True

def test_right_angle_triangle_large_values():
    rel_tolerance = 1e-5
    assert right_angle_triangle(1000, 1000, pytest.approx(1414.21356, rel=rel_tolerance)) == True
    assert right_angle_triangle(1000000, 1000000, pytest.approx(1414213.56, rel=rel_tolerance)) == True
    assert right_angle_triangle(1000, 1000, 1414) == False

def test_right_angle_triangle_invalid_triangle():
    assert right_angle_triangle(1, 2, 5) == False
    assert right_angle_triangle(1, 1, 3) == False
    assert right_angle_triangle(2, 2, 4) == False