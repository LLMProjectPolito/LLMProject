
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

# --- The Function (Assumed implementation for context) ---
def right_angle_triangle(a, b, c):
    """Checks if sides a, b, and c form a right-angled triangle."""
    # Implementation would go here
    pass

# --- Superior Test Suite ---

@pytest.mark.parametrize("a, b, c", [
    # Standard Pythagorean triples
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (7, 24, 25),
    (20, 21, 29),
    # Permutations (Testing that order doesn't matter)
    (5, 3, 4),
    (13, 5, 12),
    (4, 5, 3),
    # Floating point precision
    (1.0, 1.0, math.sqrt(2)),
    (1.5, 2.0, 2.5),
    # Large numbers
    (3000000, 4000000, 5000000),
])
def test_right_angle_triangle_valid(a, b, c):
    """Tests all valid right-angled triangles, including permutations, floats, and large integers."""
    assert right_angle_triangle(a, b, c) is True


@pytest.mark.parametrize("a, b, c", [
    (1, 1, 1),    # Equilateral
    (2, 2, 3),    # Isosceles (not right)
    (10, 11, 12), # Scalene (not right)
    (5, 5, 5),    # Equilateral
    (1.0, 1.0, 1.5), # Close float but not right
])
def test_right_angle_triangle_not_right_angled(a, b, c):
    """Tests valid triangle shapes that are mathematically not right-angled."""
    assert right_angle_triangle(a, b, c) is False


@pytest.mark.parametrize("a, b, c", [
    (1, 2, 3),    # Degenerate (sum of two sides equals third)
    (1, 1, 10),   # Impossible (sum of two sides less than third)
    (1, 2, 10),   # Impossible
])
def test_right_angle_triangle_invalid_geometry(a, b, c):
    """Tests sides that violate the Triangle Inequality Theorem."""
    assert right_angle_triangle(a, b, c) is False


@pytest.mark.parametrize("a, b, c", [
    (0, 4, 5),    # Zero side
    (-3, 4, 5),   # Negative side
    (3, -4, 5),   # Negative side
    (-3, -4, -5), # All negative
    (0, 0, 0),    # All zeros
])
def test_right_angle_triangle_invalid_dimensions(a, b, c):
    """Tests that non-positive side lengths are rejected."""
    assert right_angle_triangle(a, b, c) is False