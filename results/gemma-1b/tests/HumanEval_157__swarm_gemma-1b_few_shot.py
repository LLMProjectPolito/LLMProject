import pytest
import math

def right_angle_triangle(a, b, c):
    """
    This function checks if a triangle with sides a, b, and c is a right triangle.
    """
    if a <= 0 or b <= 0 or c <= 0:
        return False
    sides = sorted([a, b, c])
    return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False

def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False

def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False

def test_right_angle_triangle_invalid():
    assert right_angle_triangle(-1, 2, 3) == False
    assert right_angle_triangle(1, -2, 3) == False
    assert right_angle_triangle(1, 2, -3) == False
    assert right_angle_triangle(1, 2, 3.0) == False
    assert right_angle_triangle(1, 2, 0) == False