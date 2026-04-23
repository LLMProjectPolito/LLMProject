
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
        assert right_angle_triangle(7, 24, 25) == True
        assert right_angle_triangle(1, 1, 1) == True #degenerate case, but still a right triangle

    def test_invalid_triangle(self):
        assert right_angle_triangle(1, 2, 3) == False
        assert right_angle_triangle(4, 6, 7) == False
        assert right_angle_triangle(1, 1, 2) == False
        assert right_angle_triangle(2, 2, 2) == False
        assert right_angle_triangle(10, 10, 10) == False

    def test_edge_cases(self):
        assert right_angle_triangle(0, 0, 0) == False # zero length sides
        assert right_angle_triangle(0, 1, 1) == False # one side is zero
        assert right_angle_triangle(1, 0, 1) == False # one side is zero
        assert right_angle_triangle(1, 1, 0) == False # one side is zero
        assert right_angle_triangle(1, 1, 1) == True #degenerate case, but still a right triangle

    def test_negative_values(self):
        assert right_angle_triangle(-3, 4, 5) == True
        assert right_angle_triangle(3, -4, 5) == True
        assert right_angle_triangle(3, 4, -5) == True
        assert right_angle_triangle(-3, -4, 5) == True
        assert right_angle_triangle(-3, 4, -5) == True
        assert right_angle_triangle(3, -4, -5) == True
        assert right_angle_triangle(-1, -2, -3) == False #negative sides don't form a triangle
        assert right_angle_triangle(-1, 2, 3) == False #negative sides don't form a triangle
        assert right_angle_triangle(1, -2, 3) == False #negative sides don't form a triangle
        assert right_angle_triangle(1, 2, -3) == False #negative sides don't form a triangle

    def test_large_numbers(self):
        assert right_angle_triangle(1000, 2000, 2200) == True
        assert right_angle_triangle(1000, 2000, 2199) == False
        assert right_angle_triangle(1000, 1000, 1000) == True

    def test_triangle_inequality(self):
        assert right_angle_triangle(1, 2, 5) == False
        assert right_angle_triangle(1, 2, 3) == False
        assert right_angle_triangle(1, 1, 2) == False
        assert right_angle_triangle(1, 1, 1) == True
        assert right_angle_triangle(1, 1, 2) == False
        assert right_angle_triangle(2, 2, 2) == False
        assert right_angle_triangle(1, 2, 4) == False
        assert right_angle_triangle(2, 3, 4) == False
        assert right_angle_triangle(3, 4, 5) == True