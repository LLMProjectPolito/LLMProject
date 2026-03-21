import pytest
from your_module import right_angle_triangle  # Replace your_module

def test_right_angle_triangle_basic():
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_non_right():
    assert right_angle_triangle(1, 2, 3) == False

def test_right_angle_triangle_zero_side():
    assert right_angle_triangle(0, 4, 5) == False

def test_right_angle_triangle_negative_side():
    assert right_angle_triangle(-3, 4, 5) == False

def test_right_angle_triangle_equal_sides():
    assert right_angle_triangle(5, 5, 5) == True

def test_right_angle_triangle_small_sides():
    assert right_angle_triangle(1, 1, 1) == False

def test_right_angle_triangle_large_sides():
    assert right_angle_triangle(100, 100, 141.42) == False

def test_right_angle_triangle_close_to_right():
    assert right_angle_triangle(3, 4, 5.0001) == True

def test_right_angle_triangle_isosceles():
    assert right_angle_triangle(5, 5, 5) == True

def test_right_angle_triangle_another_right():
    assert right_angle_triangle(6, 8, 10) == True