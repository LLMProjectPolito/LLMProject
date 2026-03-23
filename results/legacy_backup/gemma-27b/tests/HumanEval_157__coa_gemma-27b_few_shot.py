import pytest
import math


# Focus: Boundary Values
def test_right_angle_triangle_zero_sides():
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 4, 0) == False

def test_right_angle_triangle_small_values():
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(1, 1, 2) == False

def test_right_angle_triangle_large_values():
    assert right_angle_triangle(1000, 1000, 1414) == True
    assert right_angle_triangle(1000, 1000, 1415) == False

# Focus: Equivalence Partitioning
def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True

def test_right_angle_triangle_invalid():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(2, 2, 3) == False

def test_right_angle_triangle_zero():
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(0, 4, 5) == False

# Focus: Invalid Input Handling
def test_invalid_input_non_positive():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 4, 0) == False

def test_invalid_input_non_numeric():
    assert right_angle_triangle("3", 4, 5) == False
    assert right_angle_triangle(3, "4", 5) == False
    assert right_angle_triangle(3, 4, "5") == False
    assert right_angle_triangle(None, 4, 5) == False
    assert right_angle_triangle(3, None, 5) == False
    assert right_angle_triangle(3, 4, None) == False

def test_invalid_input_triangle_inequality():
    assert right_angle_triangle(1, 2, 5) == False
    assert right_angle_triangle(5, 1, 2) == False
    assert right_angle_triangle(2, 5, 1) == False