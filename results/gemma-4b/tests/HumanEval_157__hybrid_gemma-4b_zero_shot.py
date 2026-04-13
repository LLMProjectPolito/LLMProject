
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

class TestRightAngleTriangle:
    def test_valid(self):
        assert right_angle_triangle(3, 4, 5) == True
        assert right_angle_triangle(5, 12, 13) == True
        assert right_angle_triangle(8, 15, 17) == True
        assert right_angle_triangle(7, 24, 25) == True
        assert right_angle_triangle(6, 8, 10) == True

    def test_invalid(self):
        assert right_angle_triangle(1, 2, 3) == False
        assert right_angle_triangle(2, 3, 4) == False
        assert right_angle_triangle(4, 5, 6) == False
        assert right_angle_triangle(1, 1, 1) == False
        assert right_angle_triangle(1, 2, 2.5) == False

    def test_zero_sides(self):
        assert right_angle_triangle(0, 4, 5) == False
        assert right_angle_triangle(3, 0, 5) == False
        assert right_angle_triangle(3, 4, 0) == False
        assert right_angle_triangle(0, 0, 0) == False

    def test_negative_sides(self):
        assert right_angle_triangle(-3, 4, 5) == False
        assert right_angle_triangle(3, -4, 5) == False
        assert right_angle_triangle(3, 4, -5) == False
        assert right_angle_triangle(-3, -4, -5) == False

    def test_equal_sides(self):
        assert right_angle_triangle(5, 5, 5) == False
        assert right_angle_triangle(1, 1, 1) == False

    def test_large_numbers(self):
        assert right_angle_triangle(1000, 1000, 1414) == True
        assert right_angle_triangle(1000, 1000, 1415) == False

    def test_decimal_numbers(self):
        assert right_angle_triangle(3.0, 4.0, 5.0) == True
        assert right_angle_triangle(1.5, 2.0, 2.5) == True
        assert right_angle_triangle(1.0, 1.0, 1.41421356237) == False