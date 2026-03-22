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
        assert right_angle_triangle(7, 24, 25) == True
        assert right_angle_triangle(20, 21, 29) == True

    def test_invalid_right_triangle(self):
        assert right_angle_triangle(1, 2, 3) == False
        assert right_angle_triangle(4, 5, 6) == False
        assert right_angle_triangle(1, 1, 1) == False
        assert right_angle_triangle(2, 3, 4) == False
        assert right_angle_triangle(10, 11, 12) == False

    def test_zero_length_side(self):
        assert right_angle_triangle(0, 4, 5) == False
        assert right_angle_triangle(3, 0, 5) == False
        assert right_angle_triangle(3, 4, 0) == False
        assert right_angle_triangle(0, 0, 0) == False

    def test_negative_length_side(self):
        assert right_angle_triangle(-3, 4, 5) == False
        assert right_angle_triangle(3, -4, 5) == False
        assert right_angle_triangle(3, 4, -5) == False
        assert right_angle_triangle(-3, -4, -5) == False

    def test_equal_sides_not_right(self):
        assert right_angle_triangle(2, 2, 3) == False
        assert right_angle_triangle(5, 5, 6) == False

    def test_large_numbers(self):
        assert right_angle_triangle(1000, 1000, 1414) == False #approx sqrt(2)
        assert right_angle_triangle(1000, 1000, 1414.2135623730951) == True
        assert right_angle_triangle(3000, 4000, 5000) == True

    def test_float_inputs(self):
        assert right_angle_triangle(3.0, 4.0, 5.0) == True
        assert right_angle_triangle(1.0, 2.0, 3.0) == False
        assert right_angle_triangle(0.5, 1.2, 1.3) == True