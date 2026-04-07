
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

def test_triangle_constraints():
    assert right_angle_triangle(1, 1, 3) == False  # Sum less than third side
    assert right_angle_triangle(1, 2, 1) == False  # Triangle inequality violation
    assert right_angle_triangle(1, 1, 2) == False  # Triangle inequality violation
    assert right_angle_triangle(0, 0, 0) == False  # All sides zero
    assert right_angle_triangle(0, 4, 5) == False  # One side zero
    assert right_angle_triangle(3, 0, 5) == False  # One side zero
    assert right_angle_triangle(3, 4, 0) == False  # One side zero
    assert right_angle_triangle(0, 0, 5) == False # Two sides zero

def test_equilateral_triangle():
    assert right_angle_triangle(1, 1, 1) == False

def test_large_numbers():
    assert right_angle_triangle(1000, 1000, pytest.approx(1414.2135623730951, rel=1e-6)) == True
    assert right_angle_triangle(1000, 1000, 1414) == False
    assert right_angle_triangle(10000, 10000, pytest.approx(14142.135623730951, rel=1e-6)) == True

def test_float_inputs():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(1.5, 2.0, 2.5) == True
    assert right_angle_triangle(1.0, 2.0, 3.0) == False

def test_negative_inputs():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False
    assert right_angle_triangle(-3, -4, -5) == False

def test_type_handling():
    assert right_angle_triangle("3", "4", "5") == False
    assert right_angle_triangle(3, 4, "5") == False
    assert right_angle_triangle(3, "4", 5) == False
    assert right_angle_triangle("3", 4, 5) == False

def test_argument_order():
    assert right_angle_triangle(4, 3, 5) == True
    assert right_angle_triangle(5, 4, 3) == False
    assert right_angle_triangle(3, 5, 4) == False
    assert right_angle_triangle(5, 3, 4) == False
    assert right_angle_triangle(4, 5, 3) == False