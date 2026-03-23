import pytest
import math

def test_right_angle_triangle_basic():
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_zero_side():
    assert right_angle_triangle(0, 4, 5) == False

def test_right_angle_triangle_zero_side():
    assert right_angle_triangle(0, 4, 5) == False