
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
from decimal import Decimal

# Assuming the function is imported from your module
# from your_module import right_angle_triangle

@pytest.mark.parametrize("a, b, c", [
    (3, 4, 5),           # Standard triple
    (5, 12, 13),         # Standard triple
    (8, 15, 17),         # Standard triple
    (5, 3, 4),           # Permutation
    (4, 5, 3),           # Permutation
    (13, 12, 5),         # Permutation
    (1.5, 2.0, 2.5),     # Floats
    (0.6, 0.8, 1.0),     # Floats
    (300000000, 400000000, 500000000), # Large integers
    (Decimal('3'), Decimal('4'), Decimal('5')), # Decimal types
])
def test_right_angle_triangle_success(a, b, c):
    """Tests valid right-angled triangles, including permutations and numeric types."""
    assert right_angle_triangle(a, b, c) is True


@pytest.mark.parametrize("a, b, c", [
    (5, 5, 5),           # Equilateral
    (2, 2, 3),           # Obtuse
    (4, 4, 5),           # Acute
    (1, 1, 10),          # Triangle inequality violation
    (1, 2, 10),          # Triangle inequality violation
    (1, 2, 3),           # Degenerate triangle (a + b = c)
])
def test_right_angle_triangle_failure(a, b, c):
    """Tests triangles that are not right-angled or are degenerate."""
    assert right_angle_triangle(a, b, c) is False


@pytest.mark.parametrize("a, b, c", [
    (0, 0, 0),           # Zero dimensions
    (3, 4, 0),           # Zero dimension
    (-3, 4, 5),          # Negative dimension
    (0, -4, -5),         # Mixed negative/zero
    (float('inf'), 1, 1),# Infinity
    (float('nan'), 1, 1),# NaN
])
def test_right_angle_triangle_invalid_dimensions(a, b, c):
    """Tests non-positive side lengths and special float values."""
    assert right_angle_triangle(a, b, c) is False


def test_right_angle_triangle_precision():
    """
    Tests floating point precision.
    Note: This test assumes the implementation uses a standard tolerance 
    (like math.isclose). If the difference is within the epsilon, 
    this test should be adjusted to expect True.
    """
    # 3^2 + 4^2 = 25. 5.0000000000001^2 is slightly more than 25.
    # We expect False if the function respects high-precision differences.
    assert right_angle_triangle(3, 4, 5.0000000000001) is False


@pytest.mark.parametrize("a, b, c", [
    (None, 4, 5),
    ("3", 4, 5),
    (3, 4, [5]),
    (3, 4, (3+4j)),      # Complex numbers
    (True, 4, 5),        # Boolean (should be treated as 1, but often rejected in strict type checks)
])
def test_right_angle_triangle_type_errors(a, b, c):
    """Tests that non-numeric or strictly invalid types raise a TypeError."""
    # Note: If the function allows bools (as they are ints), 
    # remove True from this parametrization.
    with pytest.raises(TypeError):
        right_angle_triangle(a, b, c)