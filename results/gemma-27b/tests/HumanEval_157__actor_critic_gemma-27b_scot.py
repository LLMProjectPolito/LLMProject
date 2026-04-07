
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
    a, b, c = sides[0], sides[1], sides[2]

    if a <= 0 or b <= 0 or c <= 0:
        return False

    if a + b <= c:
        return False

    return abs(a**2 + b**2 - c**2) < 1e-6  # Using a small tolerance for floating-point comparisons


def test_valid_right_triangle():
    assert right_angle_triangle(3, 4, 5) == True

def test_not_right_triangle():
    assert right_angle_triangle(1, 2, 3) == False

def test_triangle_inequality_violation():
    assert right_angle_triangle(1, 2, 5) == False

def test_almost_triangle_inequality_violation():
    assert right_angle_triangle(1, 2, 3.0000001) == False

def test_triangle_inequality_slightly_greater():
    assert right_angle_triangle(1, 2, 3.00000001) == True

def test_hypotenuse_not_last():
    assert right_angle_triangle(5, 3, 4) == True

def test_large_numbers_triangle_inequality():
    assert right_angle_triangle(1000, 1000, 1414.213562371) == False

def test_valid_float_right_triangle():
    assert right_angle_triangle(3.5, 4.5, 5.700877) == True

def test_invalid_float_right_triangle():
    assert right_angle_triangle(1.1, 2.2, 3.3) == False

def test_non_positive_side():
    assert right_angle_triangle(-3, 4, 5) == False