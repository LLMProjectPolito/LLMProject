
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
    Raises ValueError if any side length is negative.
    Returns False if the sides cannot form a valid triangle (including zero lengths).
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive.")
    sides = sorted([a, b, c])
    if sides[0] + sides[1] <= sides[2]:
        return False
    return pytest.approx(sides[0]**2 + sides[1]**2) == sides[2]**2

def test_valid_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True

def test_invalid_triangle():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(6, 7, 8) == False

def test_negative_length_sides():
    with pytest.raises(ValueError):
        right_angle_triangle(-3, 4, 5)
    with pytest.raises(ValueError):
        right_angle_triangle(3, -4, 5)
    with pytest.raises(ValueError):
        right_angle_triangle(3, 4, -5)
    with pytest.raises(ValueError):
        right_angle_triangle(-3, -4, -5)

def test_equal_sides():
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(2, 2, 3) == False

def test_large_numbers():
    assert right_angle_triangle(1000, 1000, pytest.approx(math.sqrt(2) * 1000)) == True
    assert right_angle_triangle(1000, 1001, 1002) == False

def test_decimal_right_triangle():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(3.1, 4.1, 5.1) == False
    assert right_angle_triangle(0.3, 0.4, 0.5) == True

def test_small_right_triangle():
    assert right_angle_triangle(0.001, 0.001, pytest.approx(math.sqrt(2) * 0.001)) == True
    assert right_angle_triangle(0.001, 0.002, 0.0020000001) == False

def test_triangle_inequality_fail():
    assert right_angle_triangle(1, 2, 5) == False

def test_nearly_right_triangle():
    assert right_angle_triangle(1, 1, 1.414214) == True
    assert right_angle_triangle(1, 1, 1.414216) == False