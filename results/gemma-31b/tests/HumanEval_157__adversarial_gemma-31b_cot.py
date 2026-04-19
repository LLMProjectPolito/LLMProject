
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

def test_standard_pythagorean_triples():
    """Test well-known Pythagorean triples."""
    assert right_angle_triangle(3, 4, 5) is True
    assert right_angle_triangle(5, 12, 13) is True
    assert right_angle_triangle(8, 15, 17) is True
    assert right_angle_triangle(7, 24, 25) is True
    assert right_angle_triangle(20, 21, 29) is True

def test_permutations():
    """Test that the order of arguments does not affect the result."""
    # Hypotenuse at different positions
    assert right_angle_triangle(3, 4, 5) is True
    assert right_angle_triangle(3, 5, 4) is True
    assert right_angle_triangle(5, 3, 4) is True

def test_non_right_triangles():
    """Test triangles that are valid but not right-angled."""
    assert right_angle_triangle(2, 2, 2) is False  # Equilateral
    assert right_angle_triangle(2, 2, 3) is False  # Isosceles
    assert right_angle_triangle(10, 10, 10) is False
    assert right_angle_triangle(4, 5, 6) is False

def test_degenerate_and_invalid_triangles():
    """Test cases where sides do not form a valid triangle or are degenerate."""
    assert right_angle_triangle(1, 2, 3) is False  # Degenerate (1+2=3)
    assert right_angle_triangle(1, 1, 10) is False # Impossible triangle
    assert right_angle_triangle(0, 0, 0) is False  # Zero length
    assert right_angle_triangle(0, 4, 5) is False  # Zero length

def test_negative_values():
    """Test that negative side lengths are handled (should be False)."""
    assert right_angle_triangle(-3, -4, -5) is False
    assert right_angle_triangle(3, 4, -5) is False

def test_floating_point_values():
    """Test with floating point numbers, including sqrt(2)."""
    # 1^2 + 1^2 = (sqrt(2))^2
    assert right_angle_triangle(1.0, 1.0, math.sqrt(2)) is True
    # 0.3^2 + 0.4^2 = 0.5^2
    assert right_angle_triangle(0.3, 0.4, 0.5) is True
    # Non-right float triangle
    assert right_angle_triangle(1.1, 1.1, 1.1) is False

@pytest.mark.parametrize("a, b, c, expected", [
    (3, 4, 5, True),
    (5, 4, 3, True),
    (13, 12, 5, True),
    (1, 1, 1, False),
    (1, 2, 3, False),
    (0, 0, 0, False),
    (10, 20, 30, False),
    (10, 20, 40, False),
])
def test_parametrized_cases(a, b, c, expected):
    """General test suite for various combinations."""
    assert right_angle_triangle(a, b, c) == expected