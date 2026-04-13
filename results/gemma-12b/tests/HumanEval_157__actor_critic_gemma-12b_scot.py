
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
from your_module import right_angle_triangle  # Replace your_module
import math

def test_valid_right_triangle():
    assert right_angle_triangle(3, 4, 5) == True

def test_valid_right_triangle_float():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True

def test_invalid_triangle():
    assert right_angle_triangle(1, 2, 3) == False

def test_zero_sides():
    assert right_angle_triangle(0, 0, 0) == False

def test_negative_sides():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False

def test_isosceles_right_triangle():
    assert right_angle_triangle(5, 5, pytest.approx(7.0710678118654755, rel=1e-6))

def test_large_numbers():
    assert right_angle_triangle(1000, 1000, pytest.approx(1414.2135623730951, rel=1e-6))

def test_equal_sides_not_right():
    assert right_angle_triangle(2, 2, 3) == False

def test_triangle_inequality_greater():
    assert right_angle_triangle(1, 2, 4) == False  # 1 + 2 < 4
    assert right_angle_triangle(1, 1, 3) == False  # 1 + 1 < 3
    assert right_angle_triangle(2, 2, 5) == False  # 2 + 2 < 5

def test_triangle_inequality_valid():
    assert right_angle_triangle(1, 2, 3) == False # 1 + 2 == 3
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True

def test_side_order():
    assert right_angle_triangle(5, 3, 4) == True

def test_small_numbers():
    assert right_angle_triangle(0.001, 0.002, pytest.approx(0.0029154759474226504, rel=1e-6))

def test_non_numeric_input():
    with pytest.raises(TypeError):
        right_angle_triangle("a", 4, 5)
    with pytest.raises(TypeError):
        right_angle_triangle(3, "b", 5)
    with pytest.raises(TypeError):
        right_angle_triangle(3, 4, "c")

def test_isosceles_right_triangle_equal_sides():
    assert right_angle_triangle(1, 1, pytest.approx(math.sqrt(2), rel=1e-6))