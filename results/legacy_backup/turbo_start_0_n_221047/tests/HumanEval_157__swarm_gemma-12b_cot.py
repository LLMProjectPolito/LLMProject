import pytest
import math

def test_zero_length_side():
    """Test case for a triangle with a zero-length side."""
    assert right_angle_triangle(0, 4, 5) == False