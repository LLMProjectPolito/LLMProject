
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

# The function right_angle_triangle(a, b, c) is assumed to be defined in the environment.

@pytest.mark.parametrize("a, b, c", [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (7, 24, 25),
    (20, 21, 29),
])
def test_valid_integer_triangles(a, b, c):
    """Tests standard integer Pythagorean triples."""
    assert right_angle_triangle(a, b, c) is True

@pytest.mark.parametrize("a, b, c", [
    (3, 5, 4),
    (5, 3, 4),
    (4, 3, 5),
    (5, 4, 3),
    (13, 12, 5),
    (12, 13, 5),
])
def test_permutation_robustness(a, b, c):
    """Tests that the function identifies the hypotenuse correctly regardless of input order."""
    assert right_angle_triangle(a, b, c) is True

@pytest.mark.parametrize("a, b, c", [
    (2, 2, 2),    # Equilateral
    (2, 3, 4),    # Scalene non-right
    (10, 10, 15), # Isosceles non-right
    (1, 1, 1.414),# Close to sqrt(2) but not quite
])
def test_invalid_triangles(a, b, c):
    """Tests triangles that are valid shapes but not right-angled."""
    assert right_angle_triangle(a, b, c) is False

@pytest.mark.parametrize("a, b, c", [
    (1, 2, 3),    # Degenerate triangle (sum of two sides equals third)
    (1, 1, 10),   # Impossible triangle (sum of two sides less than third)
    (0, 4, 5),    # Zero side
    (0, 0, 0),    # All zeros
    (-3, 4, 5),   # Negative side
    (-3, -4, -5), # All negative
])
def test_degenerate_and_invalid_geometry(a, b, c):
    """Tests cases that do not form valid geometric triangles."""
    assert right_angle_triangle(a, b, c) is False

def test_floating_point_precision():
    """
    Tests if the function handles floating point precision correctly.
    This is a critical test for Blue Team: if the function uses '==' 
    instead of math.isclose(), this test will likely fail.
    """
    side_a = 1.0
    side_b = 1.0
    side_c = math.sqrt(2)
    # Using pytest.approx logic is usually for the implementation, 
    # but here we test if the function itself is robust.
    assert right_angle_triangle(side_a, side_b, side_c) is True

def test_large_values():
    """Tests the function with very large integer values."""
    a = 3000000
    b = 4000000
    c = 5000000
    assert right_angle_triangle(a, b, c) is True

def test_non_numeric_input():
    """Tests how the function handles non-numeric types (Defensive Testing)."""
    with pytest.raises((TypeError, ValueError)):
        right_angle_triangle("3", "4", "5")
    with pytest.raises((TypeError, ValueError)):
        right_angle_triangle(None, 4, 5)