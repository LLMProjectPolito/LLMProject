
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

def test_valid_right_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True
    assert right_angle_triangle(20, 21, 29) == True

def test_invalid_triangle_inequality():
    # Tests cases where the triangle inequality is not met.
    assert right_angle_triangle(1, 2, 5) == False  # Not a triangle
    assert right_angle_triangle(1, 1, 2) == False  # Invalid triangle (sum of two sides < third side)

def test_non_right_triangles():
    assert right_angle_triangle(4, 5, 6) == False
    assert right_angle_triangle(10, 11, 12) == False
    assert right_angle_triangle(5, 5, 5) == False  # Equilateral triangle
    assert right_angle_triangle(0, 0, 5) == False  # Two sides zero
    assert right_angle_triangle(0, 0, 0) == False  # All sides zero

def test_edge_case_equal_sides_not_right():
    assert right_angle_triangle(5, 5, 7) == False

def test_edge_case_very_small_numbers():
    assert right_angle_triangle(0.001, 0.002, 0.003) == False

def test_large_numbers():
    assert right_angle_triangle(1000, 1000, 1414) == False
    assert right_angle_triangle(1000, 1000, pytest.approx(1414.2135623730951, rel=1e-6)) == True
    assert right_angle_triangle(10000, 10000, 14142) == False

def test_float_inputs():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(1.5, 2.0, 2.5) == True
    assert right_angle_triangle(1.0, 2.0, 3.0) == False

def test_negative_inputs():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False
    assert right_angle_triangle(-3, -4, -5) == False

def test_zero_and_positive():
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 4, 0) == False