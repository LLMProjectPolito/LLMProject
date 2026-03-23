import pytest
import math

def test_floating_point_near_right_angle():
    assert right_angle_triangle(3.000001, 4.000001, 5.000002) == True