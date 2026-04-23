
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
    The function also checks if the given sides satisfy the triangle inequality theorem.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    if a <= 0 or b <= 0 or c <= 0:
        return False
    sides = sorted([a, b, c])
    if sides[0] + sides[1] <= sides[2]:
        return False
    return pytest.approx(sides[0]**2 + sides[1]**2) == sides[2]**2

def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True

def test_right_angle_triangle_invalid():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(6, 7, 8) == False

def test_right_angle_triangle_zero():
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(0, 3, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 5, 0) == False

def test_right_angle_triangle_negative():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False
    assert right_angle_triangle(-3, -4, 5) == False
    assert right_angle_triangle(-3, 4, -5) == False
    assert right_angle_triangle(3, -4, -5) == False
    assert right_angle_triangle(-3, -4, -5) == False

def test_right_angle_triangle_equal_sides():
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(1, 1, pytest.approx(1.4142135623730951)) == True

def test_right_angle_triangle_large_numbers():
    assert right_angle_triangle(1000, 1000, pytest.approx(1414.2135623730951)) == True
    assert right_angle_triangle(100, 100, 100) == False

def test_right_angle_triangle_decimal_numbers():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(1.5, 2.0, 2.5) == True
    assert right_angle_triangle(1.0, 2.0, 3.0) == False
    assert right_angle_triangle(3.14, 4.22, 5.0) == True
    assert right_angle_triangle(1.1, 2.2, 2.5) == False

def test_right_angle_triangle_edge_cases():
    assert right_angle_triangle(0.001, 0.002, 0.002000001) == False
    assert right_angle_triangle(0.001, 0.001, pytest.approx(0.00141421356237)) == True

def test_right_angle_triangle_floating_point_precision():
    assert right_angle_triangle(1, 1, 1.4142135623730951) == True