
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

def test_basic_right_triangle():
    assert right_angle_triangle(3, 4, 5) == True

def test_other_right_triangles():
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True

def test_non_right_triangles():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(4, 6, 7) == False
    assert right_angle_triangle(5, 5, 6) == False

def test_isosceles_right_triangle():
    assert right_angle_triangle(5, 5, 5) == True

def test_equilateral_triangle():
    assert right_angle_triangle(3, 3, 3) == True

def test_invalid_input_negative_length():
    assert right_angle_triangle(-3, 4, 5) == False

def test_invalid_input_zero_length():
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(0, 0, 0) == False

def test_all_zeroes():
    assert right_angle_triangle(0, 0, 0) == False

def test_floating_point_numbers():
    assert right_angle_triangle(3.5, 4.2, 5.3) == True

def test_large_numbers():
    assert right_angle_triangle(1000, 2000, 2200) == True

def test_degenerate_triangle_1_1_2():
    assert right_angle_triangle(1, 1, 2) == False

def test_degenerate_triangle_1_2_4():
    assert right_angle_triangle(1, 2, 4) == False

def test_hypotenuse_longest_side_1_1_1():
    assert right_angle_triangle(1, 1, 1) == True

def test_hypotenuse_longest_side_1_2_3():
    assert right_angle_triangle(1, 2, 3) == False

def test_1_1_2_invalid():
    assert right_angle_triangle(1, 1, 2) == False

def test_1_1_0_invalid():
    assert right_angle_triangle(1, 1, 0) == False

def test_1_2_1_invalid():
    assert right_angle_triangle(1, 2, 1) == False

def test_1_0_1_invalid():
    assert right_angle_triangle(1, 0, 1) == False

def test_0_1_1_invalid():
    assert right_angle_triangle(0, 1, 1) == False

def test_0_0_1_invalid():
    assert right_angle_triangle(0, 0, 1) == False

def test_0_1_0_invalid():
    assert right_angle_triangle(0, 1, 0) == False

def test_1_0_0_invalid():
    assert right_angle_triangle(1, 0, 0) == False

def test_0_0_0_invalid():
    assert right_angle_triangle(0, 0, 0) == False