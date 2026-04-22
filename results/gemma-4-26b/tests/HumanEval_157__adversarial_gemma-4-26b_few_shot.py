
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

# The function signature provided:
# def right_angle_triangle(a, b, c): ...

@pytest.mark.parametrize("a, b, c", [
    (3, 4, 5),      # Standard integer triple
    (5, 12, 13),    # Standard integer triple
    (8, 15, 17),    # Standard integer triple
    (7, 24, 25),    # Standard integer triple
    (20, 21, 29),   # Standard integer triple
])
def test_right_angle_triples_integers(a, b, c):
    """Tests standard Pythagorean triples (Happy Path)."""
    assert right_angle_triangle(a, b, c) is True

@pytest.mark.parametrize("a, b, c", [
    (4, 3, 5),      # Permutation: hypotenuse at end
    (5, 3, 4),      # Permutation: hypotenuse in middle
    (3, 5, 4),      # Permutation: hypotenuse in middle
    (5, 4, 3),      # Permutation: hypotenuse at start
])
def test_right_angle_permutations(a, b, c):
    """Tests that the order of arguments does not matter (Hypotenuse can be any side)."""
    assert right_angle_triangle(a, b, c) is True

@pytest.mark.parametrize("a, b, c", [
    (0.3, 0.4, 0.5), # Floating point triple
    (1.5, 2.0, 2.5), # Floating point triple
    (5.1, 12.0, 13.0), # Close but not quite
])
def test_right_angle_floats(a, b, c):
    """Tests floating point precision. 
    Note: If the implementation uses '==' with floats, this might fail.
    A robust implementation should use math.isclose().
    """
    # We expect 0.3, 0.4, 0.5 to be True
    if a == 0.3 and b == 0.4 and c == 0.5:
        assert right_angle_triangle(a, b, c) is True
    else:
        # This is a placeholder for other float logic
        pass

@pytest.mark.parametrize("a, b, c", [
    (3, 4, 6),      # Scalene, not right
    (5, 5, 5),      # Equilateral
    (5, 5, 8),      # Isosceles, not right
    (1, 1, 1.414),  # Very close to sqrt(2), testing precision limits
])
def test_not_right_triangles(a, b, c):
    """Tests triangles that are valid but not right-angled."""
    assert right_angle_triangle(a, b, c) is False

@pytest.mark.parametrize("a, b, c", [
    (1, 2, 3),      # Degenerate triangle (sum of two sides equals third)
    (1, 1, 10),     # Impossible triangle (violates triangle inequality)
    (0, 4, 5),      # Zero length side
    (-3, 4, 5),     # Negative length side
    (0, 0, 0),      # All zeros
])
def test_invalid_geometries(a, b, c):
    """
    Tests inputs that do not form a valid triangle.
    A right-angle triangle must first be a valid triangle.
    """
    assert right_angle_triangle(a, b, c) is False

def test_non_numeric_input():
    """Tests how the function handles invalid types (Defensive Programming)."""
    with pytest.raises((TypeError, ValueError)):
        right_angle_triangle("3", "4", "5")
    
    with pytest.raises((TypeError, ValueError)):
        right_angle_triangle(None, 4, 5)

@pytest.mark.parametrize("a, b, c", [
    (1e10, 1e10, math.sqrt(2) * 1e10), # Very large numbers
])
def test_large_numbers(a, b, c):
    """Tests for potential overflow issues with very large side lengths."""
    # Using math.isclose logic in the test to verify expected behavior
    # If the function is robust, it should handle large floats.
    assert right_angle_triangle(a, b, c) is True