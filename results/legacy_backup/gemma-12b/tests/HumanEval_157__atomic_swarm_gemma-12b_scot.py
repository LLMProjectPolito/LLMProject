import pytest
import math

def test_right_angle_triangle_positive():
    """Test a valid right-angled triangle (3, 4, 5)."""
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_zero_sides():
    """
    Test case for when one or more sides are zero.
    A triangle cannot have a side with length zero, so it should return False.
    """
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 4, 0) == False
    assert right_angle_triangle(0, 0, 5) == False
    assert right_angle_triangle(0, 0, 0) == False

def test_right_angle_triangle_invalid_side_length():
    """
    Test case to check if the function handles invalid side lengths (zero or negative).
    """
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, 0) == False