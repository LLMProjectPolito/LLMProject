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
    assert right_angle_triangle(0, 0, 0) == False

import pytest

def test_invalid_side_length():
    """
    Test case to ensure that negative side lengths are handled correctly.
    A triangle cannot have negative side lengths, so this should return False.
    """
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False