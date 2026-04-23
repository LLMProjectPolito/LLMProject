
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
    return sides[0]**2 + sides[1]**2 == sides[2]**2

def test_right_angle_triangle_positive(a, b, c):
    assert right_angle_triangle(a, b, c) == True

def test_right_angle_triangle_invalid_triangle(a, b, c):
    assert right_angle_triangle(a, b, c) == False

def test_right_angle_triangle_equal_sides(a, b, c):
    assert right_angle_triangle(a, b, c) == False

def test_right_angle_triangle_one_side_zero(a, b, c):
    assert right_angle_triangle(0, b, c) == False

def test_right_angle_triangle_negative_sides(a, b, c):
    assert right_angle_triangle(-3, 4, 5) == True

def test_right_angle_triangle_mixed_positive_negative(a, b, c):
    assert right_angle_triangle(-3, 4, 5) == True

def test_right_angle_triangle_large_numbers(a, b, c):
    assert right_angle_triangle(1000, 2000, 2200) == True

def test_right_angle_triangle_small_numbers(a, b, c):
    assert right_angle_triangle(1, 1, 1) == False

def test_right_angle_triangle_a_equals_b(a, b, c):
    assert right_angle_triangle(5, 5, 5) == False

def test_right_angle_triangle_a_equals_c(a, b, c):
    assert right_angle_triangle(5, 5, 5) == False

def test_right_angle_triangle_b_equals_c(a, b, c):
    assert right_angle_triangle(5, 5, 5) == False