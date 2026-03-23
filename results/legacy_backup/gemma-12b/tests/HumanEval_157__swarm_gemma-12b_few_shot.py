import pytest
import math

def test_right_angle_triangle_almost_equal():
    assert right_angle_triangle(3.0, 4.0, 5.0000000000000001) == True

def test_right_angle_triangle_almost_equal_2():
    assert right_angle_triangle(3.0, 4.0, 5.0000000001) == True