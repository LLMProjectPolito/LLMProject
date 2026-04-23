
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
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (7, 24, 25),
    (20, 21, 29),
])
def test_valid_right_triangles(a, b, c):
    """Test standard integer Pythagorean triples."""
    assert right_angle_triangle(a, b, c) is True

@pytest.mark.parametrize("a, b, c", [
    (4, 3, 5),  # Permuted order
    (5, 13, 12), # Permuted order
    (13, 5, 12), # Permuted order
    (25, 7, 24), # Permuted order
])
def test_valid_right_triangles_permutations(a, b, c):
    """Test that the order of arguments does not affect the result."""
    assert right_angle_triangle(a, b, c) is True

@pytest.mark.parametrize("a, b, c", [
    (3.0, 4.0, 5.0),
    (5.0, 12.0, 13.0),
    (1.5, 2.0, 2.5),
])
def test_valid_right_triangles_floats(a, b, c):
    """Test with floating point values."""
    assert right_angle_triangle(a, b, c) is True

@pytest.mark.parametrize("a, b, c", [
    (3, 3, 3),    # Equilateral
    (2, 2, 3),    # Isosceles (Acute)
    (5, 5, 8),    # Isosceles (Obtuse)
    (1, 2, 3),    # Degenerate (not a triangle)
    (1, 1, 10),   # Impossible triangle
    (10, 10, 10), # Equilateral
])
def test_invalid_triangles(a, b, c):
    """Test triangles that are not right-angled."""
    assert right_angle_triangle(a, b, c) is False

@pytest.mark.parametrize("a, b, c", [
    (0, 4, 5),    # Zero side
    (-3, 4, 5),   # Negative side
    (0, 0, 0),    # All zeros
    (-3, -4, -5), # All negatives
])
def test_degenerate_and_invalid_inputs(a, b, c):
    """Test edge cases like zero or negative side lengths."""
    assert right_angle_triangle(a, b, c) is False

def test_large_values():
    """Test with large Pythagorean triples to ensure stability."""
    # 20, 21, 29 is small, let's use a larger one: 200, 210, 290
    assert right_angle_triangle(200, 210, 290) is True
    # 88, 105, 137
    assert right_angle_triangle(88, 105, 137) is True