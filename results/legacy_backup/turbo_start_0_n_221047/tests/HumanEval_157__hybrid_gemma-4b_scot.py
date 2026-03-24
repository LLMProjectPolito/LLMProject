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

def test_invalid_right_triangle():
    assert right_angle_triangle(1, 2, 3) == False

def test_another_valid_right_triangle():
    assert right_angle_triangle(5, 12, 13) == True

def test_zero_side():
    assert right_angle_triangle(0, 4, 5) == False

def test_negative_side():
    assert right_angle_triangle(-3, 4, 5) == False

def test_equal_sides():
    assert right_angle_triangle(4, 4, 4) == True

def test_large_numbers():
    assert right_angle_triangle(1000, 1000, 1000) == True

def test_floating_point_numbers():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True