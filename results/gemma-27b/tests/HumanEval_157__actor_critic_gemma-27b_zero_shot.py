
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
    if not all(isinstance(side, (int, float)) for side in [a, b, c]):
        raise TypeError("Sides must be numeric")
    if any(side <= 0 for side in [a, b, c]):
        raise ValueError("Sides must be positive")

    sides = sorted([a, b, c])
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

def test_zero_sides():
    with pytest.raises(ValueError):
        right_angle_triangle(0, 0, 0)
    with pytest.raises(ValueError):
        right_angle_triangle(0, 3, 5)
    with pytest.raises(ValueError):
        right_angle_triangle(3, 0, 5)
    with pytest.raises(ValueError):
        right_angle_triangle(3, 5, 0)

def test_negative_sides():
    with pytest.raises(ValueError):
        right_angle_triangle(-3, 4, 5)
    with pytest.raises(ValueError):
        right_angle_triangle(3, -4, 5)
    with pytest.raises(ValueError):
        right_angle_triangle(3, 4, -5)
    with pytest.raises(ValueError):
        right_angle_triangle(-3, -4, -5)

def test_isosceles_not_right():
    assert right_angle_triangle(5, 5, 6) == False

def test_sqrt2():
    assert right_angle_triangle(1, 1, math.sqrt(2)) == True

def test_large_numbers():
    assert right_angle_triangle(1000, 1000, 1414.21356237) == True
    assert right_angle_triangle(100, 100, 100) == False

def test_decimal_numbers():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(3.5, 4.5, 5.700877) == True
    assert right_angle_triangle(1.0, 2.0, 3.0) == False

def test_small_numbers():
    assert right_angle_triangle(1e-9, 1e-9, 1.414e-9) == True

def test_large_integers():
    assert right_angle_triangle(10**9, 10**9, 1.41421356237 * 10**9) == True

def test_non_numeric_input():
    with pytest.raises(TypeError):
        right_angle_triangle("3", 4, 5)
    with pytest.raises(TypeError):
        right_angle_triangle(3, "4", 5)
    with pytest.raises(TypeError):
        right_angle_triangle(3, 4, "5")

def test_slightly_off():
    assert right_angle_triangle(3, 4, 5.00001) == False