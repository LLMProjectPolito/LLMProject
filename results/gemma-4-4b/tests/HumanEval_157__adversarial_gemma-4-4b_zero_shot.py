
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

    def test_valid_right_triangle(self):
        assert right_angle_triangle(3, 4, 5) == True
        assert right_angle_triangle(5, 12, 13) == True
        assert right_angle_triangle(8, 15, 17) == True
        assert right_angle_triangle(1, 1, (1**2 + 1**2)**0.5) == True # Test with square root

    def test_invalid_triangle(self):
        assert right_angle_triangle(1, 2, 3) == False
        assert right_angle_triangle(7, 8, 9) == False
        assert right_angle_triangle(2, 3, 4) == False
        assert right_angle_triangle(1, 1, 1) == False # Equilateral triangle

    def test_zero_length_sides(self):
        assert right_angle_triangle(0, 0, 0) == False
        assert right_angle_triangle(0, 1, 1) == False
        assert right_angle_triangle(1, 0, 1) == False
        assert right_angle_triangle(1, 1, 0) == False

    def test_negative_length_sides(self):
        assert right_angle_triangle(-3, 4, 5) == True # Should still work with absolute values
        assert right_angle_triangle(3, -4, 5) == True
        assert right_angle_triangle(3, 4, -5) == True
        assert right_angle_triangle(-3, -4, -5) == True

    def test_same_length_sides(self):
        assert right_angle_triangle(5, 5, 5) == False
        assert right_angle_triangle(5, 5, 6) == False
        assert right_angle_triangle(6, 5, 5) == False

    def test_large_numbers(self):
        assert right_angle_triangle(1000, 1000, 1414) == True
        assert right_angle_triangle(10000, 10000, 14142) == True

    def test_float_sides(self):
        assert right_angle_triangle(3.0, 4.0, 5.0) == True
        assert right_angle_triangle(3.5, 4.5, 5.5) == True
        assert right_angle_triangle(1.0, 1.0, (1.0**2 + 1.0**2)**0.5) == True
        assert right_angle_triangle(1.1, 1.2, (1.1**2 + 1.2**2)**0.5) == True