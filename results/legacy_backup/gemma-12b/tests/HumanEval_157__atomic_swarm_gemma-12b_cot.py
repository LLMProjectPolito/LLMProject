import pytest
import math

def test_right_angle_triangle_positive():
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_zero_sides():
    """Test with one or more sides having zero length."""
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(0, 3, 4) == False
    assert right_angle_triangle(3, 0, 4) == False
    assert right_angle_triangle(3, 4, 0) == False

def test_right_angle_triangle_invalid_input():
    """Test with a negative side length."""
    assert right_angle_triangle(-3, 4, 5) == False