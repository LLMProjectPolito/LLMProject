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
    a, b, c = sides[0], sides[1], sides[2]

    if a <= 0 or b <= 0 or c <= 0:
        return False

    if a + b <= c:
        return False

    return abs(a**2 + b**2 - c**2) < 1e-6  # Using a small tolerance for floating-point comparisons


def test_valid_right_triangle():
    assert right_angle_triangle(3, 4, 5) == True

def test_valid_right_triangle_different_order():
    assert right_angle_triangle(4, 3, 5) == True

def test_not_right_triangle():
    assert right_angle_triangle(1, 2, 3) == False

def test_invalid_input_zero_side():
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 4, 0) == False

def test_invalid_input_negative_side():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False

def test_invalid_input_triangle_inequality():
    assert right_angle_triangle(1, 2, 5) == False
    assert right_angle_triangle(1, 5, 2) == False
    assert right_angle_triangle(5, 1, 2) == False

def test_isosceles_right_triangle():
    assert right_angle_triangle(1, 1, math.sqrt(2)) == True

def test_large_numbers():
    assert right_angle_triangle(65, 72, 97) == True