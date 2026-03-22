import pytest
from your_module import right_angle_triangle  # Replace your_module

def test_valid_right_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True
    assert right_angle_triangle(20, 21, 29) == True

def test_invalid_right_triangle():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(4, 5, 6) == False
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(10, 11, 12) == False

def test_zero_length_side():
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 4, 0) == False
    assert right_angle_triangle(0, 0, 0) == False

def test_negative_length_side():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False
    assert right_angle_triangle(-3, -4, -5) == False

def test_equal_sides():
    assert right_angle_triangle(5, 5, 5) == False
    assert right_angle_triangle(10, 10, 10) == False

def test_large_numbers():
    assert right_angle_triangle(1000, 1000, 1414) == False #approximate
    assert right_angle_triangle(1000, 1000, 1414.2135623730951) == True #approximate
    assert right_angle_triangle(1000000, 1000000, 1414213.562373095) == True #approximate

def test_float_inputs():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(1.0, 2.0, 3.0) == False
    assert right_angle_triangle(0.5, 1.2, 1.3) == True
    assert right_angle_triangle(0.5, 1.2, 1.4) == False