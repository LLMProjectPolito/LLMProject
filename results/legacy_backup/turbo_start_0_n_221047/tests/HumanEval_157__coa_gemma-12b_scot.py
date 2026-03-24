import pytest
import math


# Focus: Boundary Values
def test_boundary_zero_sides():
    """Test with one or more sides equal to zero."""
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(0, 3, 4) == False
    assert right_angle_triangle(3, 0, 4) == False
    assert right_angle_triangle(3, 4, 0) == False

def test_boundary_equal_sides():
    """Test with sides that are equal, but don't form a right triangle."""
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(2, 2, 2) == False

def test_boundary_almost_right_triangle():
    """Test values very close to forming a right triangle."""
    assert right_angle_triangle(3.0, 4.0, 5.000000000000001) == True
    assert right_angle_triangle(3.000000000000001, 4.0, 5.0) == True
    assert right_angle_triangle(3.0, 4.000000000000001, 5.0) == True

# Focus: Type Scenarios
def test_right_angle_triangle_valid_input():
    """Test with valid integer inputs forming a right triangle."""
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_invalid_input():
    """Test with integer inputs not forming a right triangle."""
    assert right_angle_triangle(1, 2, 3) == False

def test_right_angle_triangle_zero_input():
    """Test with zero as input, should return False."""
    assert right_angle_triangle(0, 0, 0) == False

# Focus: Logic Branches
def test_right_angle_triangle_valid_right_angle():
    """Test case where a^2 + b^2 == c^2"""
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_valid_right_angle_different_order():
    """Test case where a^2 + b^2 == c^2, but sides are in different order"""
    assert right_angle_triangle(4, 3, 5) == True

def test_right_angle_triangle_not_right_angle():
    """Test case where a^2 + b^2 != c^2"""
    assert right_angle_triangle(1, 2, 3) == False