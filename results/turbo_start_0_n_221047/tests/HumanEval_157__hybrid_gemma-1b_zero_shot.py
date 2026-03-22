import pytest
from your_module import right_angle_triangle  # Replace your_module

def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_invalid():
    assert right_angle_triangle(1, 2, 3) == False

def test_right_angle_triangle_degenerate():
    assert right_angle_triangle(1, 1, 1) == False

def test_right_angle_triangle_zero_sides():
    assert right_angle_triangle(0, 1, 1) == False

def test_right_angle_triangle_large_numbers():
    assert right_angle_triangle(1000, 2000, 3000) == True

def test_right_angle_triangle_small_numbers():
    assert right_angle_triangle(1, 1, 1) == False