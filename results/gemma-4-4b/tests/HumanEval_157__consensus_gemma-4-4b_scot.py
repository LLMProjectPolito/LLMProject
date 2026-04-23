
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
        assert right_angle_triangle(1, 1, (2**0.5)) == True #Test with square root
        assert right_angle_triangle(25, 60, 65) == True

    def test_invalid_triangle(self):
        assert right_angle_triangle(1, 2, 3) == False
        assert right_angle_triangle(7, 8, 9) == False
        assert right_angle_triangle(2, 3, 4) == False
        assert right_angle_triangle(1, 1, 1) == False #Equilateral triangle
        assert right_angle_triangle(1, 5, 7) == False

    def test_zero_length_sides(self):
        assert right_angle_triangle(0, 0, 0) == False
        assert right_angle_triangle(0, 1, 1) == False
        assert right_angle_triangle(1, 0, 1) == False
        assert right_angle_triangle(1, 1, 0) == False

    def test_negative_length_sides(self):
        assert right_angle_triangle(-3, 4, 5) == True #should still work if the squares are positive
        assert right_angle_triangle(3, -4, 5) == True
        assert right_angle_triangle(3, 4, -5) == True
        assert right_angle_triangle(-3, -4, -5) == True
        assert right_angle_triangle(-3, -4, 5) == True

    def test_equal_sides(self):
        assert right_angle_triangle(5, 5, 5) == False
        assert right_angle_triangle(5, 5, 6) == False
        assert right_angle_triangle(5, 6, 5) == False

    def test_large_numbers(self):
        assert right_angle_triangle(1000, 1000, 1414) == True
        assert right_angle_triangle(1000, 1000, 1001) == False

    def test_decimal_numbers(self):
        assert right_angle_triangle(0.5, 0.5, 0.707) == True #approximate sqrt(2)/2
        assert right_angle_triangle(0.1, 0.2, 0.2236) == True #approximate sqrt(0.5)
        assert right_angle_triangle(0.1, 0.2, 0.2237) == False