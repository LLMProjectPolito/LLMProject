import pytest
import math


# Focus: Boundary Values
def test_boundary_zero():
    assert right_angle_triangle(0, 0, 0) == False

def test_boundary_small():
    assert right_angle_triangle(1, 1, 1) == False

def test_boundary_large():
    assert right_angle_triangle(1000, 1000, 1414) == True

# Focus: Type Scenarios
def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_invalid():
    assert right_angle_triangle(1, 2, 3) == False

def test_right_angle_triangle_zero_side():
    assert right_angle_triangle(0, 4, 5) == False

# Focus: Logic Branches
def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_invalid():
    assert right_angle_triangle(1, 2, 3) == False

def test_right_angle_triangle_zero_side():
    assert right_angle_triangle(0, 4, 5) == False