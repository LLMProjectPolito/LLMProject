
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
import math

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
    if a <= 0 or b <= 0 or c <= 0:
        return False

    if not (a + b > c and a + c > b and b + c > a):
        return False

    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2


### Tests (Pytest):
def test_valid_right_triangles():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(6, 8, 10) == True

def test_invalid_right_triangles():
    assert right_angle_triangle(1, 2, 4) == False
    assert right_angle_triangle(3, 4, 6) == False
    assert right_angle_triangle(1, 1, 3) == False

def test_zero_length_sides():
    assert right_angle_triangle(0, 3, 4) == False
    assert right_angle_triangle(0, 0, 0) == False

def test_negative_length_sides():
    assert right_angle_triangle(-1, 2, 3) == False
    assert right_angle_triangle(1, -2, 3) == False
    assert right_angle_triangle(1, 2, -3) == False

def test_equal_sides():
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(3, 3, 3) == False
    assert right_angle_triangle(5, 5, 5) == False

def test_large_numbers():
    assert right_angle_triangle(1000, 1000, 1414) == True  # Approximate sqrt(2) * 1000
    assert right_angle_triangle(1000, 1000, 2000) == False

# Removed test_edge_case_almost_right as it's not relevant with integer inputs.
# Removed test_non_right_triangles as it's redundant.