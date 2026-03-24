
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

def test_near_triangle_inequality():
    assert right_angle_triangle(1, 2, 3.0000001) == False

def test_isosceles_right_triangle():
    assert right_angle_triangle(1, 1, 1.41421356237) == True

def test_valid_float_right_triangle():
    assert right_angle_triangle(3.5, 4.5, 5.700877) == True

def test_invalid_float_right_triangle():
    assert right_angle_triangle(1.1, 2.2, 3.3) == False

def test_tolerance_limit():
    assert right_angle_triangle(3, 4, 5.000001) == False

def test_swapped_sides():
    assert right_angle_triangle(4, 3, 5) == True

def test_two_sides_equal_near_hypotenuse():
    assert right_angle_triangle(1, 1, 1.41421356238) == False