
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

    # Input Validation: Check for valid triangle inequality and non-negative side lengths
    if not (a > 0 and b > 0 and c > 0):
        return False
    if not (a + b > c and a + c > b and b + c > a):
        return False

    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (3, 4, 5, True),  # Valid right-angled triangle
        (5, 12, 13, True), # Another valid right-angled triangle
        (8, 15, 17, True), # Another valid right-angled triangle
        (1, 2, 3, False), # Invalid triangle
        (1, 1, 3, False), # Invalid triangle
        (3, 3, 3, False), # Equilateral triangle (not right-angled)
        (0, 4, 5, False), # Zero side length
        (3, -4, 5, False), # Negative side length
        (5, 4, 3, True),  # Longest side not 'c' after sorting
        (4, 5, 3, True),  # Longest side not 'c' after sorting
        (3, 5, 4, True),  # Longest side not 'c' after sorting
        (1, 1, math.sqrt(2), pytest.approx(True)), #Isosceles right triangle (floating point)
        (5, 5, 5, False), # Equilateral triangle - not a right triangle
        (1000000, 1000000, math.sqrt(2000000000), pytest.approx(True)), # Large numbers
    ]
)
def test_right_angle_triangle(a, b, c, expected):
    """Tests for the right_angle_triangle function."""
    assert right_angle_triangle(a, b, c) == expected