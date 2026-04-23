
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

import math
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

    # Input Validation: Check for valid side lengths
    if not all(isinstance(side, (int, float)) for side in [a, b, c]):
        raise TypeError("Side lengths must be numbers (int or float)")

    if any(side <= 0 for side in [a, b, c]):
        raise ValueError("Side lengths must be positive")

    # Triangle Inequality Theorem
    if not (a + b > c and a + c > b and b + c > a):
        return False  # Not a valid triangle

    sides = sorted([a, b, c])
    return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)


def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(6, 8, 10) == True

def test_right_angle_triangle_invalid():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(1, 1, 3) == False
    assert right_angle_triangle(2, 2, 4) == False

def test_right_angle_triangle_isosceles():
    assert math.isclose(right_angle_triangle(1, 1, math.sqrt(2)), True)

def test_right_angle_triangle_equilateral():
    assert right_angle_triangle(1, 1, 1) == False

def test_right_angle_triangle_zero_side():
    with pytest.raises(ValueError):
        right_angle_triangle(0, 1, 2)

def test_right_angle_triangle_negative_side():
    with pytest.raises(ValueError):
        right_angle_triangle(-1, 2, 3)

def test_right_angle_triangle_large_numbers():
    assert math.isclose(right_angle_triangle(20, 21, 29), True)
    assert math.isclose(right_angle_triangle(1000, 1000, 1414.21356), True)

def test_right_angle_triangle_type_error():
    with pytest.raises(TypeError):
        right_angle_triangle("a", 2, 3)
    with pytest.raises(TypeError):
        right_angle_triangle(1, "b", 3)
    with pytest.raises(TypeError):
        right_angle_triangle(1, 2, "c")

def test_right_angle_triangle_violates_triangle_inequality():
    assert right_angle_triangle(1, 2, 5) == False

def test_right_angle_triangle_equal_sides_not_right():
    assert right_angle_triangle(2, 2, 2) == False

def test_right_angle_triangle_near_zero_values():
    assert math.isclose(right_angle_triangle(0.001, 0.001, math.sqrt(0.002)), True)