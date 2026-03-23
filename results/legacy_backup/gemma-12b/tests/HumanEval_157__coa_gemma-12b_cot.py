import pytest
import math


# Focus: Boundary Values
import pytest

def test_right_angle_triangle_boundary_zero():
    assert right_angle_triangle(0, 0, 0) == False

def test_right_angle_triangle_boundary_one_zero():
    assert right_angle_triangle(0, 3, 4) == False
    assert right_angle_triangle(3, 0, 4) == False
    assert right_angle_triangle(3, 4, 0) == False

def test_right_angle_triangle_boundary_small_values():
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(1, 1, 2) == False
    assert right_angle_triangle(3, 4, 5) == True

# Focus: Type Scenarios
def test_right_angle_triangle_valid_input():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True

def test_right_angle_triangle_invalid_input():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(13, 12, 5) == False

def test_right_angle_triangle_zero_input():
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(0, 3, 4) == False
    assert right_angle_triangle(3, 0, 4) == False
    assert right_angle_triangle(3, 4, 0) == False

# Focus: Logic Branches
def test_right_angle_triangle_valid_right_triangle():
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_invalid_triangle():
    assert right_angle_triangle(1, 2, 3) == False

def test_right_angle_triangle_zero_length_side():
    assert right_angle_triangle(0, 4, 5) == False