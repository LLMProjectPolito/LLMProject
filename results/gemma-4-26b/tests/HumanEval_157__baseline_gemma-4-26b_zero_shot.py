
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

@pytest.mark.parametrize("a, b, c", [
    (3, 4, 5),          # Standard triple
    (5, 12, 13),        # Standard triple
    (8, 15, 17),        # Standard triple
    (7, 24, 25),        # Standard triple
    (20, 21, 29),       # Standard triple
    (5, 4, 3),          # Permutation: hypotenuse first
    (13, 5, 12),        # Permutation: hypotenuse middle
    (4, 5, 3),          # Permutation: hypotenuse last
    (1.5, 2.0, 2.5),    # Floating point triple
    (0.3, 0.4, 0.5),    # Floating point triple
])
def test_right_angle_triangle_true(a, b, c):
    """Tests cases that should return True (valid right-angled triangles)."""
    assert right_angle_triangle(a, b, c) is True

@pytest.mark.parametrize("a, b, c", [
    (1, 2, 3),          # Example from docstring (not a triangle)
    (2, 3, 4),          # Valid triangle, not right-angled
    (5, 5, 5),          # Equilateral triangle
    (10, 11, 12),       # Scalene triangle, not right-angled
    (3, 4, 6),          # Triangle, not right-angled
    (1, 1, 1.414),      # Close to sqrt(2) but not exact
])
def test_right_angle_triangle_false(a, b, c):
    """Tests cases that should return False (valid triangles that are not right-angled)."""
    assert right_angle_triangle(a, b, c) is False

@pytest.mark.parametrize("a, b, c", [
    (0, 0, 0),          # All zeros
    (-3, 4, 5),         # Negative side
    (3, -4, 5),         # Negative side
    (0, 3, 4),          # Zero side
    (1, 1, 10),         # Impossible triangle (sum of two sides <= third)
    (-1, -1, -1),       # All negatives
])
def test_right_angle_triangle_invalid_inputs(a, b, c):
    """Tests edge cases including zero, negative, and impossible side lengths."""
    assert right_angle_triangle(a, b, c) is False