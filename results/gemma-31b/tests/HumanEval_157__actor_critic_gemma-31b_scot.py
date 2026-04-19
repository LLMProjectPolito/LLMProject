
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

@pytest.mark.parametrize("a, b, c", [
    (3, 4, 5),    # Classic 3-4-5
    (5, 12, 13),  # Classic 5-12-13
    (8, 15, 17),  # Classic 8-15-17
    (7, 24, 25),  # Classic 7-24-25
    (4, 3, 5),    # Permutation check (integrated)
    (5, 4, 3),    # Permutation check (integrated)
])
def test_valid_right_triangles(a, b, c):
    """Test standard integer Pythagorean triples and their permutations."""
    assert right_angle_triangle(a, b, c) is True

@pytest.mark.parametrize("a, b, c", [
    (3, 3, 3),    # Equilateral (Acute)
    (2, 2, 3),    # Obtuse
    (1, 2, 3),    # Degenerate (Not a triangle)
    (10, 10, 15), # Isosceles (Not right)
])
def test_non_right_triangles(a, b, c):
    """Test triangles that are not right-angled."""
    assert right_angle_triangle(a, b, c) is False

@pytest.mark.parametrize("a, b, c", [
    (0, 0, 0),    # Zero length
    (-3, 4, 5),   # Negative length (should be False, not True)
    (0, 4, 5),    # One zero length
    (-3, -4, -5), # All negative
])
def test_invalid_geometry(a, b, c):
    """Test that zero or negative side lengths are not considered right triangles."""
    assert right_angle_triangle(a, b, c) is False

@pytest.mark.parametrize("a, b, c", [
    (1.0, 1.0, math.sqrt(2)), # Irrational hypotenuse
    (1.5, 2.0, 2.5),          # Exact float representation
    (0.3, 0.4, 0.5),          # Small floats
])
def test_floating_point_precision(a, b, c):
    """
    Test with floating point numbers. 
    This ensures the implementation uses math.isclose() rather than ==.
    """
    assert right_angle_triangle(a, b, c) is True

@pytest.mark.parametrize("a, b, c", [
    ("3", 4, 5),    # String input
    (None, 4, 5),   # None input
    ([3], 4, 5),    # List input
])
def test_non_numeric_inputs(a, b, c):
    """Test that non-numeric inputs raise a TypeError."""
    with pytest.raises(TypeError):
        right_angle_triangle(a, b, c)

@pytest.mark.parametrize("a, b, c", [
    (math.inf, 4, 5), # Infinity
    (math.nan, 4, 5), # Not a Number
])
def test_special_float_values(a, b, c):
    """Test that inf and nan do not result in a True return."""
    assert right_angle_triangle(a, b, c) is False

def test_large_numbers():
    """Test with very large integers to ensure no overflow issues."""
    a = 3000000
    b = 4000000
    c = 5000000
    assert right_angle_triangle(a, b, c) is True