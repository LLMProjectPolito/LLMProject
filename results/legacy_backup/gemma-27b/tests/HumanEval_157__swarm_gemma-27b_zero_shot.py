import pytest

def test_zero_length_side():
    """Test case for when one side has zero length."""
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 4, 0) == False