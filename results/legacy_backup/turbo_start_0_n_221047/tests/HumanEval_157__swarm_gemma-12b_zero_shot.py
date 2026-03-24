import pytest
import math

def test_zero_length_side():
    assert right_angle_triangle(0, 4, 5) == False