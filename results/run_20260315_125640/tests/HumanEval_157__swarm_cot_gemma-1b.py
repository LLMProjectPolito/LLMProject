import pytest
import math

def right_angle_triangle(a, b, c):
    assert a + b == c
    assert a + c == b
    assert b + c == a

def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(1, 1, 1) == True
    assert right_angle_triangle(1, 1, 2) == False

def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(1, 1, 1) == True
    assert right_angle_triangle(1, 1, 2) == False

def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(1, 1, 1) == True
    assert right_angle_triangle(1, 1, 2) == False