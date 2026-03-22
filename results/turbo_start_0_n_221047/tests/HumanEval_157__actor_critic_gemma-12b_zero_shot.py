import pytest
from your_module import right_angle_triangle  # Replace your_module

def test_valid_right_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True
    assert right_angle_triangle(20, 21, 29) == True

def test_triangle_inequality():
    assert right_angle_triangle(3, 4, 6) == False  # Violates triangle inequality
    assert right_angle_triangle(1, 2, 5) == False  # Violates triangle inequality
    assert right_angle_triangle(1, 1, 2) == False  # Violates triangle inequality

def test_zero_sides():
    assert right_angle_triangle(0, 0, 0) == False  # All sides zero
    assert right_angle_triangle(0, 3, 4) == False
    assert right_angle_triangle(3, 0, 4) == False
    assert right_angle_triangle(3, 4, 0) == False
    assert right_angle_triangle(0, 0, 5) == False  # Two sides zero, third non-zero
    assert right_angle_triangle(0, 0, 1) == False

def test_large_numbers():
    assert right_angle_triangle(1000, 1000, pytest.approx(1414.2135623730951)) == True
    assert right_angle_triangle(10000, 10000, pytest.approx(14142.135623730951)) == True
    assert right_angle_triangle(1000, 1000, 1414) == False

def test_floating_point_inputs():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(1.5, 2.0, 2.5) == True
    assert right_angle_triangle(1.0, 2.0, 3.0) == False

def test_negative_inputs():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False
    assert right_angle_triangle(-3, -4, -5) == False

def test_near_miss():
    assert right_angle_triangle(3.0, 4.0, 5.0001) == False
    assert right_angle_triangle(3.0, 4.0, 4.9999) == False

def test_invalid_triangle_properties():
    assert right_angle_triangle(1, 1, 1) == False  # Equilateral triangle
    assert right_angle_triangle(5, 5, 10) == False  # Two sides equal, invalid
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(4, 5, 6) == False
    assert right_angle_triangle(10, 11, 12) == False
    assert right_angle_triangle(2, 3, 4) == False