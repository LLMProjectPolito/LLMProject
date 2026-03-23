import pytest

def test_zero_length_side():
    """Test case for when one of the sides has a length of zero."""
    assert right_angle_triangle(0, 4, 5) is False
    assert right_angle_triangle(3, 0, 5) is False
    assert right_angle_triangle(3, 4, 0) is False