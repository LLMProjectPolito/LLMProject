
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
        assert right_angle_triangle(6, 8, 10) == True
        assert right_angle_triangle(1, 1, 1.4142135623730951) == True
        assert right_angle_triangle(2.5, 3.5, 4.0) == True
        assert right_angle_triangle(1.0, 2.0, 2.2360679775) == True
        assert right_angle_triangle(0.5, 0.5, 0.7071067811865476) == True
        assert right_angle_triangle(1000, 2000, 2236.0679775) == True
        assert right_angle_triangle(1000, 1000, 1414.2135623730951) == False

    def test_invalid_triangle(self):
        assert right_angle_triangle(1, 2, 3) == False
        assert right_angle_triangle(4, 6, 7) == False
        assert right_angle_triangle(1, 2, 4) == False
        assert right_angle_triangle(5, 5, 5) == False
        assert right_angle_triangle(0, 1, 1) == False
        assert right_angle_triangle(1000, 1000, 1414.2135623730951) == False

    def test_zero_length_sides(self):
        assert right_angle_triangle(0, 0, 0) == False
        assert right_angle_triangle(0, 1, 1) == False
        assert right_angle_triangle(1, 0, 1) == False
        assert right_angle_triangle(1, 1, 0) == False
        assert right_angle_triangle(0, 0, 0) == False
        assert right_angle_triangle(0, 1, 1) == False
        assert right_angle_triangle(1, 0, 1) == False
        assert right_angle_triangle(1, 1, 0) == False

    def test_negative_side_lengths(self):
        assert right_angle_triangle(-3, 4, 5) == False
        assert right_angle_triangle(3, -4, 5) == False
        assert right_angle_triangle(3, 4, -5) == False
        assert right_angle_triangle(-3, -4, -5) == False

    def test_float_side_lengths(self):
        assert right_angle_triangle(2.5, 3.5, 4.0) == True
        assert right_angle_triangle(1.0, 2.0, 2.2360679775) == True
        assert right_angle_triangle(0.5, 0.5, 0.7071067811865476) == True
        assert right_angle_triangle(2.5, 3.5, 4.0) == True
        assert right_angle_triangle(1.0, 2.0, 2.2360679775) == True
        assert right_angle_triangle(0.5, 0.5, 0.7071067811865476) == True

    def test_large_numbers(self):
        assert right_angle_triangle(1000, 2000, 2236.0679775) == True
        assert right_angle_triangle(1000, 1000, 1414.2135623730951) == False