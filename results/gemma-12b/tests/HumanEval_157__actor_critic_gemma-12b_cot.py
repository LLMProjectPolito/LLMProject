
def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''

import pytest

def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    sides = sorted([a, b, c])
    if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
        return False
    if sides[0] + sides[1] <= sides[2]:
        return False
    return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-6

def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True

def test_right_angle_triangle_invalid():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(4, 4, 5) == False

def test_right_angle_triangle_edge_cases():
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(1, 0, 1) == False
    assert right_angle_triangle(0, 1, 1) == False
    assert right_angle_triangle(1, 1, 0) == False
    assert right_angle_triangle(0, 0, 1) == False
    assert right_angle_triangle(0, 1, 0) == False
    assert right_angle_triangle(1, 0, 0) == False

def test_right_angle_triangle_float_values():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(1.0, 2.0, 3.0) == False
    assert right_angle_triangle(0.5, 0.75, 1.0) == True

def test_right_angle_triangle_large_values():
    assert right_angle_triangle(1000, 1000, 1414.21356) == True
    assert right_angle_triangle(1000, 1001, 1002) == False

def test_right_angle_triangle_same_values():
    assert right_angle_triangle(5, 5, 5) == False
    assert right_angle_triangle(5, 5, 5*1.41421356) == True

def test_triangle_inequality():
    assert right_angle_triangle(1, 2, 5) == False
    assert right_angle_triangle(1, 1, 2) == False

def test_negative_values():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False

def test_isosceles_non_right():
    assert right_angle_triangle(5, 5, 6) == False

def test_right_angle_triangle_integer_large_values():
    assert right_angle_triangle(1000, 1000, 1414) == False
    assert right_angle_triangle(3, 4, 5) == True

def test_invalid_input_types():
    assert right_angle_triangle("a", 4, 5) == False
    assert right_angle_triangle(3, "b", 5) == False
    assert right_angle_triangle(3, 4, "c") == False
    assert right_angle_triangle([1,2], 4, 5) == False
    assert right_angle_triangle(3, [1,2], 5) == False
    assert right_angle_triangle(3, 4, [1,2]) == False