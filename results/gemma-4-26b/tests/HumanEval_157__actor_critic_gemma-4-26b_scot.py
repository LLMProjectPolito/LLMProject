
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

# The function 'right_angle_triangle' is assumed to be available in the namespace.

@pytest.mark.parametrize("a, b, c", [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (7, 24, 25),
    (20, 21, 29),
    (1.5, 2.0, 2.5),
    (0.3, 0.4, 0.5),
])
def test_valid_triangles(a, b, c):
    """Test standard integer and floating point Pythagorean triples."""
    assert right_angle_triangle(a, b, c) is True

@pytest.mark.parametrize("a, b, c", [
    (3, 4, 5),
    (3, 5, 4),
    (5, 3, 4),
    (5, 4, 3),
    (4, 3, 5),
    (4, 5, 3),
])
def test_permutations(a, b, c):
    """Test that the order of sides does not matter (hypotenuse can be any side)."""
    assert right_angle_triangle(a, b, c) is True

@pytest.mark.parametrize("a, b, c", [
    (1, 2, 3),    # Degenerate (a + b = c)
    (5, 5, 10),   # Degenerate
    (2, 2, 2),    # Equilateral
    (3, 4, 6),    # Obtuse
    (4, 5, 6),    # Acute
    (10, 10, 15), # Isosceles non-right
])
def test_invalid_triangles(a, b, c):
    """Test triangles that are mathematically not right-angled."""
    assert right_angle_triangle(a, b, c) is False

@pytest.mark.parametrize("a, b, c", [
    (0, 4, 5),      # Zero length side
    (-3, 4, 5),     # Negative length side
    (0, 0, 0),      # All zeros
    (float('nan'), 4, 5),
    (float('inf'), 4, 5),
    (3, float('nan'), 5),
    (3, 4, float('inf')),
])
def test_invalid_numeric_values(a, b, c):
    """Test edge cases like zero, negative numbers, and non-finite floats."""
    assert right_angle_triangle(a, b, c) is False

@pytest.mark.parametrize("a, b, c", [
    (3, 4, 5.0000001), # Clearly not a triple
    (3.0000001, 4, 5), 
    (3, 4.0000001, 5),
])
def test_near_misses(a, b, c):
    """Verify that values significantly different from a triple return False."""
    assert right_angle_triangle(a, b, c) is False

@pytest.mark.parametrize("a, b, c", [
    (3, 4, 5.000000000000001), # Within standard float epsilon
    (3.000000000000001, 4, 5),
])
def test_near_hits(a, b, c):
    """Verify that values within floating-point epsilon are accepted as True."""
    assert right_angle_triangle(a, b, c) is True

def test_large_floats():
    """Test with very large floating-point numbers."""
    # Large valid triple
    a, b, c = 3e15, 4e15, 5e15
    assert right_angle_triangle(a, b, c) is True
    
    # Large invalid triple (mathematically distinct)
    assert right_angle_triangle(1e16, 1e16, 1.5e16) is False

def test_underflow_floats():
    """Test with extremely small positive numbers to check for underflow handling."""
    # Small valid triple
    a, b, c = 3e-20, 4e-20, 5e-20
    assert right_angle_triangle(a, b, c) is True
    
    # Small invalid triple
    assert right_angle_triangle(1e-20, 1e-20, 1e-20) is False

@pytest.mark.parametrize("a, b, c", [
    (None, 4, 5),
    ("3", 4, 5),
    (3, [4], 5),
    (3, 4, {"5"}),
    (complex(3, 0), 4, 5),  # Complex numbers should be rejected
    (3, complex(4, 0), 5),
    (3, 4, complex(5, 0)),
])
def test_type_safety(a, b, c):
    """Ensure non-numeric and complex types raise a TypeError or return False."""
    # Depending on implementation, complex might return False or raise TypeError.
    # Given the prompt, we assume strict numeric handling.
    with pytest.raises((TypeError, ValueError)):
        right_angle_triangle(a, b, c)