import pytest
import math

def test_right_angle_triangle_zero_length_side():
    """Test case for when one of the sides has a length of zero."""
    assert right_angle_triangle(0, 4, 5) == False

def test_zero_length_side():
    """Test case for a triangle with a zero-length side."""
    assert right_angle_triangle(0, 4, 5) == False