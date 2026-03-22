import pytest
import math

def test_right_angle_triangle_small_floats():
    # Edge case: extremely small floating‑point lengths that form a right triangle.
    a = 1e-10
    b = 1e-10
    c = math.sqrt(2) * a
    assert right_angle_triangle(a, b, c) is True

def test_right_angle_triangle_large_ints_permuted():
    # Very large integer sides that form a 3-4-5 triangle, provided out of order.
    a, b, c = 4000000000, 3000000000, 5000000000
    assert right_angle_triangle(a, b, c) is True

def test_negative_side_returns_false():
    # A triangle cannot have a negative side length; the function should handle this gracefully.
    assert right_angle_triangle(-3, 4, 5) is False