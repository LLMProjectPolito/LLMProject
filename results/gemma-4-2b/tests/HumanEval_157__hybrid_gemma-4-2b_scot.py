
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
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2

def test_right_angle_triangle_parametrized(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

def test_non_right_triangle_equilateral(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

def test_invalid_triangle(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

def test_zero_length_sides(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

class TestRightAngleTriangle:

    def test_valid_right_triangle_3_4_5(self):
        assert right_angle_triangle(3, 4, 5) == True

    def test_valid_right_triangle_5_12_13(self):
        assert right_angle_triangle(5, 12, 13) == True

    def test_valid_right_triangle_8_15_17(self):
        assert right_angle_triangle(8, 15, 17) == True

    def test_valid_right_triangle_1_1_sqrt_2(self):
        assert right_angle_triangle(1, 1, math.sqrt(2)) == True

    def test_invalid_triangle_1_2_3(self):
        assert right_angle_triangle(1, 2, 3) == False

    def test_invalid_triangle_2_3_4(self):
        assert right_angle_triangle(2, 3, 4) == False

    def test_invalid_triangle_1_2_4(self):
        assert right_angle_triangle(1, 2, 4) == False

    def test_invalid_triangle_1_1_1(self):
        assert right_angle_triangle(1, 1, 1) == False

    def test_negative_side(self):
        assert right_angle_triangle(-3, 4, 5) == False

    def test_zero_side(self):
        assert right_angle_triangle(0, 4, 5) == False

    def test_zero_and_negative_side(self):
        assert right_angle_triangle(0, -3, 5) == False

    def test_float_numbers(self):
        assert right_angle_triangle(3.5, 4.2, 5.0) == True

    def test_int_and_float_numbers(self):
        assert right_angle_triangle(3, 4.2, 5) == True

    def test_large_numbers(self):
      assert right_angle_triangle(1000, 1001, 1002) == True

    def test_triangle_inequality(self):
        assert right_angle_triangle(1, 1, 2) == False