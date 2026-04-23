
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

# Note: The function right_angle_triangle(a, b, c) is assumed to be defined in the environment.

@pytest.mark.parametrize("a, b, c", [
    # Standard integer triples
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (7, 24, 25),
    (20, 21, 29),
    # Unsorted sides (testing hypotenuse identification)
    (5, 3, 4),
    (4, 5, 3),
    (13, 12, 5),
    (13, 5, 12),
    # Floating point triples
    (1.5, 2.0, 2.5),
    (0.3, 0.4, 0.5),
    (2.5, 6.0, 6.5),
])
def test_right_angle_triangles_true(a, b, c):
    """Tests valid Pythagorean triples including unsorted sides and floats."""
    assert right_angle_triangle(a, b, c) is True


@pytest.mark.parametrize("a, b, c", [
    (1, 1, 1),          # Equilateral
    (2, 2, 3),          # Isosceles (Acute)
    (5, 5, 8),          # Isosceles (Obtuse)
    (4, 5, 6),          # Scalene (Acute)
    (1, 1, 1.414),      # Near-miss float (close to sqrt(2))
])
def test_right_angle_triangles_false_valid_geometry(a, b, c):
    """Tests valid triangles that are not right-angled."""
    assert right_angle_triangle(a, b, c) is False


@pytest.mark.parametrize("a, b, c", [
    (0, 4, 5),          # Zero length side
    (-3, 4, 5),         # Negative length side
    (0, 0, 0),          # All zeros
    (-1, -1, -1),       # All negatives
    (1, 2, 3),          # Degenerate (a + b = c)
    (1, 2, 10),         # Impossible (a + b < c)
])
def test_right_angle_triangles_false_invalid_geometry(a, b, c):
    """Tests non-triangles, degenerate triangles, and invalid side lengths."""
    assert right_angle_triangle(a, b, c) is False


def test_right_angle_triangles_precision_edge_case():
    """
    Tests high-precision floating point comparison using irrational numbers.
    Ensures the implementation handles math.sqrt(2) correctly.
    """
    side_a = 1.0
    side_b = 1.0
    side_c = math.sqrt(2)
    assert right_angle_triangle(side_a, side_b, side_c) is True


def test_right_angle_triangles_large_values():
    """Tests very large integers to ensure no overflow and correct logic at scale."""
    # Large valid triple
    assert right_angle_triangle(3000000, 4000000, 5000000) is True
    # Large non-triple (near miss)
    assert right_angle_triangles_false_valid_geometry_logic(3000001, 4000000, 5000000) is False

def test_right_angle_triangles_large_values_robustness():
    """Explicitly testing large values for both True and False outcomes."""
    # Large valid triple
    assert right_angle_triangle(3000000, 4000000, 5000000) is True
    # Large non-triple
    assert right_angle_triangle(3000001, 4000000, 5000000) is False