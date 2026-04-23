
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
    (5, 3, 4),          # Permutation
    (13, 5, 12),        # Permutation
    (4, 5, 3),          # Permutation
    (0.3, 0.4, 0.5),    # Floating point values
])
def test_right_angle_triangle_valid(a, b, c):
    """Tests cases that should return True (valid right-angled triangles)."""
    assert right_angle_triangle(a, b, c) is True

@pytest.mark.parametrize("a, b, c", [
    (1, 2, 3),          # Not a right triangle
    (5, 5, 5),          # Equilateral triangle
    (5, 5, 8),          # Isosceles triangle (not right)
    (10, 10, 15),       # Isosceles triangle (not right)
    (3, 4, 6),          # Close but not right
    (2, 2, 3),          # Small non-right triangle
])
def test_right_angle_triangle_invalid(a, b, c):
    """Tests cases that are triangles but not right-angled."""
    assert right_angle_triangle(a, b, c) is False

@pytest.mark.parametrize("a, b, c", [
    (1, 1, 10),         # Violates triangle inequality (a + b < c)
    (10, 1, 1),         # Violates triangle inequality
    (0, 0, 0),          # Zero lengths
    (-3, 4, 5),         # Negative side length
    (3, 4, -5),         # Negative side length
])
def test_right_angle_triangle_not_a_triangle(a, b, c):
    """Tests cases that do not form a valid triangle at all."""
    assert right_angle_triangle(a, b, c) is False

def test_right_angle_triangle_large_values():
    """Tests with larger integer values to ensure no overflow issues."""
    # 20, 21, 29 is a Pythagorean triple (20^2 + 21^2 = 400 + 441 = 841 = 29^2)
    assert right_angle_triangle(20, 21, 29) is True