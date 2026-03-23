import pytest
import math


# Focus: Boundary Values
def test_right_angle_triangle_true():
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_false():
    assert right_angle_triangle(1, 2, 3) == False

def test_right_angle_triangle_zero():
    assert right_angle_triangle(0, 0, 0) == False

# Focus: Type Scenarios
def test_right_angle_triangle_true():
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_false():
    assert right_angle_triangle(1, 2, 3) == False

# Focus: Logic Branches
def test_right_angle_triangle_true():
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_false():
    assert right_angle_triangle(1, 2, 3) == False