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
    return sides[0]**2 + sides[1]**2 == sides[2]**2

def test_basic_right_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True

def test_non_right_triangle():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(2, 3, 4) == False

def test_zero_length_sides():
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 4, 0) == False
    assert right_angle_triangle(0, 0, 0) == False

def test_negative_length_sides():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False
    assert right_angle_triangle(-3, -4, -5) == False

def test_floating_point_numbers():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(5.0, 12.0, 13.0) == True
    assert right_angle_triangle(3.1, 4.1, 5.1) == False
    assert right_angle_triangle(0.3, 0.4, 0.5) == True

def test_order_of_sides():
    assert right_angle_triangle(4, 3, 5) == True
    assert right_angle_triangle(5, 3, 4) == True
    assert right_angle_triangle(5, 4, 3) == True

def test_edge_cases_large_numbers():
    assert right_angle_triangle(1000, 1000, 1414) == False # close to sqrt(2)
    assert right_angle_triangle(1000, 1000, 1414.21356) == True

def test_equality():
    assert right_angle_triangle(1, 1, 1.41421356) == True
    assert right_angle_triangle(5, 5, 7.0710678) == True
    assert right_angle_triangle(2, 2, 3) == False