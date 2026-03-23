import pytest
import math

def test_right_angle_triangle_positive():
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_zero_sides():
    assert right_angle_triangle(0, 0, 0) == False

def test_right_angle_triangle_negative_input():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False