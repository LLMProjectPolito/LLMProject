
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

# The function right_angle_triangle is already defined in the environment.
# We are importing it or assuming it is available in the global scope.

@pytest.mark.parametrize("a, b, c, expected", [
    (3, 4, 5, True),   # Standard 3-4-5
    (5, 4, 3, True),   # Permutation
    (4, 5, 3, True),   # Permutation
    (5, 12, 13, True), # Another triple
    (13, 12, 5, True), # Permutation
    (8, 15, 17, True), # Another triple
    (17, 8, 15, True), # Permutation
])
def test_classic_right_triangles(a, b, c, expected):
    """Test known Pythagorean triples in various orders."""
    assert right_angle_triangle(a, b, c) == expected

@pytest.mark.parametrize("a, b, c", [
    (1, 2, 3),         # Degenerate/Non-right
    (2, 2, 2),         # Equilateral
    (3, 3, 5),         # Obtuse
    (3, 3, 4),         # Acute
    (10, 10, 10),      # Equilateral
])
def test_non_right_triangles(a, b, c):
    """Test triangles that are not right-angled."""
    assert right_angle_triangle(a, b, c) is False

def test_floating_point_right_triangle():
    """Test with floating point values (1, 1, sqrt(2))."""
    # 1^2 + 1^2 = (sqrt(2))^2 -> 1 + 1 = 2
    assert right_angle_triangle(1.0, 1.0, math.sqrt(2)) is True
    assert right_angle_triangle(math.sqrt(2), 1.0, 1.0) is True

@pytest.mark.parametrize("a, b, c", [
    (0, 4, 5),         # Zero side
    (-3, 4, 5),        # Negative side
    (0, 0, 0),         # All zero
    (-3, -4, -5),      # All negative
])
def test_invalid_dimensions(a, b, c):
    """Test that invalid side lengths return False."""
    assert right_angle_triangle(a, b, c) is False

def test_large_values():
    """Test with large integers to ensure stability."""
    # 3000^2 + 4000^2 = 5000^2
    assert right_angle_triangle(3000, 4000, 5000) is True
    # Large non-right triangle
    assert right_angle_triangle(10**6, 10**6, 10**6) is False