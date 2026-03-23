import pytest
import math


# Focus: Boundary Values
def test_boundary_zero_sides():
    """Test with one or more sides as zero."""
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(0, 3, 4) == False
    assert right_angle_triangle(3, 0, 4) == False
    assert right_angle_triangle(3, 4, 0) == False

def test_boundary_equal_sides():
    """Test with equal sides, including right-angled triangle cases."""
    assert right_angle_triangle(3, 3, 3) == False
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True

def test_boundary_large_sides():
    """Test with large side lengths to check for potential overflow issues."""
    assert right_angle_triangle(1000, 1000, 1414.21356) == True #approximate
    assert right_angle_triangle(1000, 1001, 1002) == False

# Focus: Type Scenarios
def test_right_angle_triangle_valid_input():
    """Test with valid integer inputs forming a right triangle."""
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_invalid_input():
    """Test with integer inputs not forming a right triangle."""
    assert right_angle_triangle(1, 2, 3) == False

def test_right_angle_triangle_zero_input():
    """Test with zero as input, which should return False."""
    assert right_angle_triangle(0, 0, 0) == False

# Focus: Logic Branches
def test_right_angle_triangle_valid_right_angle():
    """Test case where a^2 + b^2 == c^2"""
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_valid_right_angle_different_order():
    """Test case where a^2 + b^2 == c^2, but sides are in a different order"""
    assert right_angle_triangle(4, 3, 5) == True

def test_right_angle_triangle_not_right_angle():
    """Test case where a^2 + b^2 != c^2"""
    assert right_angle_triangle(1, 2, 3) == False