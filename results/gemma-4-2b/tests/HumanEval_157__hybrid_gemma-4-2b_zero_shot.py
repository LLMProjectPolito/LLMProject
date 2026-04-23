
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

@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (3, 4, 5, True),
        (5, 12, 13, True),
        (8, 15, 17, True),
        (6, 8, 10, True),
        (7, 24, 25, True),
        (1, 1, 1, False),
        (1, 2, 3, False),
        (2, 2, 2, False),
        (0, 0, 0, False),
        (1, 0, 1, False),
        (0, 1, 1, False),
        (1, 1, 0, False),
        (10, 0, 10, False),
        (0, 10, 10, False),
        (10, 10, 0, False),
        (2, 3, 4, False),
        (5, 5, 5, False),
        (1, 2, 4, False),
        (4, 1, 2, False),
        (2, 4, 1, False),
        (0.5, 0.5, 0.5, False),
        (0.5, 0.5, 1, False),
        (1, 0.5, 0.5, False),
        (0.5, 1, 0.5, False),
        (1, 1, 1.0000000001, False) # Test for floating point precision
    ],
)
def test_right_angle_triangle(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (3, 4, 5, True),
        (5, 12, 13, True),
        (8, 15, 17, True),
        (6, 8, 10, True),
        (7, 24, 25, True),
        (1, 1, 1, False),
        (1, 2, 3, False),
        (2, 2, 2, False),
        (0, 0, 0, False),
        (1, 0, 1, False),
        (0, 1, 1, False),
        (1, 1, 0, False),
        (10, 0, 10, False),
        (0, 10, 10, False),
        (10, 10, 0, False),
        (2, 3, 4, False),
        (5, 5, 5, False),
        (1, 2, 4, False),
        (4, 1, 2, False),
        (2, 4, 1, False),
        (0.5, 0.5, 0.5, False),
        (0.5, 0.5, 1, False),
        (1, 0.5, 0.5, False),
        (0.5, 1, 0.5, False),
        (1, 1, 1.0000000001, False) # Test for floating point precision
    ],
)
def test_right_angle_triangle_negative(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (3, 4, 5, True),
        (5, 12, 13, True),
        (8, 15, 17, True),
        (6, 8, 10, True),
        (7, 24, 25, True),
        (1, 1, 1, False),
        (1, 2, 3, False),
        (2, 2, 2, False),
        (0, 0, 0, False),
        (1, 0, 1, False),
        (0, 1, 1, False),
        (1, 1, 0, False),
        (10, 0, 10, False),
        (0, 10, 10, False),
        (10, 10, 0, False),
        (2, 3, 4, False),
        (5, 5, 5, False),
        (1, 2, 4, False),
        (4, 1, 2, False),
        (2, 4, 1, False),
        (0.5, 0.5, 0.5, False),
        (0.5, 0.5, 1, False),
        (1, 0.5, 0.5, False),
        (0.5, 1, 0.5, False),
        (1, 1, 1.0000000001, False) # Test for floating point precision
    ],
)
def test_right_angle_triangle_zero(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected