import pytest
from your_module import right_angle_triangle  # Replace your_module

def test_valid_right_triangle():
    assert right_angle_triangle(3, 4, 5) == True

def test_valid_right_triangle_float():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True

def test_valid_right_triangle_isosceles():
    assert right_angle_triangle(5, 5, 7.0710678118654755) == True

def test_invalid_triangle():
    assert right_angle_triangle(1, 2, 3) == False

def test_zero_side():
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 4, 0) == False

def test_negative_side():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False

def test_equilateral_triangle():
    assert right_angle_triangle(5, 5, 5) == False

def test_large_numbers():
    assert right_angle_triangle(20, 21, 29) == True
    assert right_angle_triangle(1000, 1000, 1414.2135623730951) == True

def test_small_numbers():
    assert right_angle_triangle(0.1, 0.2, 0.28284271247461902) == True

def test_permutation_valid():
    assert right_angle_triangle(5, 3, 4) == True
    assert right_angle_triangle(4, 5, 3) == True

def test_triangle_inequality_violation():
    assert right_angle_triangle(1, 2, 5) == False