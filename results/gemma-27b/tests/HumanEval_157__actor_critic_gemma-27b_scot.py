
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


@pytest.mark.parametrize("a, b, c", [
    (0, 4, 5),
    (3, -4, 5),
    (5, 0, 0),
    (-1, -2, 3)
])
def test_invalid_input(a, b, c):
    assert right_angle_triangle(a, b, c) == False

@pytest.mark.parametrize("a, b, c", [
    (1, 2, 5),
    (1, 2, 3.0000001)
])
def test_triangle_inequality(a, b, c):
    assert right_angle_triangle(a, b, c) == False

@pytest.mark.parametrize("a, b, c", [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (1000, 1000, 1414.21356237),
    (3.5, 4.5, 5.700877),
    (0.3, 0.4, 0.5),
    (0.000001, 0.000001, 0.00000141421356237)
])
def test_valid_right_triangle(a, b, c):
    assert right_angle_triangle(a, b, c) == True

@pytest.mark.parametrize("a, b, c", [
    (1, 2, 3),
    (1.1, 2.2, 3.3)
])
def test_invalid_right_triangle(a, b, c):
    assert right_angle_triangle(a, b, c) == False

def test_equilateral_triangle():
    assert right_angle_triangle(5, 5, 5) == False

def test_near_zero_sides():
    # Using a small tolerance (1e-6) for floating-point comparisons due to potential
    # representation errors with very small numbers.
    assert right_angle_triangle(0.000001, 0.000001, 0.00000141421356237) == True