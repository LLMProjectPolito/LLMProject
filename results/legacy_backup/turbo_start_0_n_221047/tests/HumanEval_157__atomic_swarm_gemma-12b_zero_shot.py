import pytest
import math

def test_basic():
    assert right_angle_triangle(3, 4, 5) == True

def test_edge_zero_sides():
    assert right_angle_triangle(0, 0, 0) == False

def test_right_angle_triangle_invalid_type():
    """Test with string input."""
    assert right_angle_triangle("3", 4, 5) == False