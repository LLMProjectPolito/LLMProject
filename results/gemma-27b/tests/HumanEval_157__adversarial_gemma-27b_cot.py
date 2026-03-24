
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

def test_valid_right_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True

def test_invalid_right_triangle():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(6, 8, 10) == True # Scaled right triangle
    assert right_angle_triangle(6, 8, 11) == False

def test_zero_length_sides():
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 4, 0) == False

def test_negative_length_sides():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False
    assert right_angle_triangle(-3, -4, -5) == False

def test_float_length_sides():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(3.5, 4.5, 5.5) == False
    assert right_angle_triangle(6.0, 8.0, 10.0) == True
    assert right_angle_triangle(0.3, 0.4, 0.5) == True

def test_large_numbers():
    assert right_angle_triangle(1000, 1000, 1414) == False #approx sqrt(2)
    assert right_angle_triangle(1000, 1000, 1414.21356) == True #approx sqrt(2)

def test_side_order():
    assert right_angle_triangle(4, 3, 5) == True
    assert right_angle_triangle(5, 3, 4) == True
    assert right_angle_triangle(5, 4, 3) == True
    assert right_angle_triangle(12, 5, 13) == True
    assert right_angle_triangle(13, 5, 12) == True
    assert right_angle_triangle(13, 12, 5) == True