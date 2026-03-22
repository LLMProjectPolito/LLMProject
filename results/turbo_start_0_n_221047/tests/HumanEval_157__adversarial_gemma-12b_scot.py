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

    def test_valid_right_triangle_different_order(self):
        assert right_angle_triangle(5, 3, 4) == True

    def test_valid_right_triangle_larger_numbers(self):
        assert right_angle_triangle(5, 12, 13) == True

    def test_invalid_triangle(self):
        assert right_angle_triangle(1, 2, 3) == False

    def test_invalid_triangle_different_order(self):
        assert right_angle_triangle(3, 1, 2) == False

    def test_zero_side(self):
        assert right_angle_triangle(0, 4, 5) == False

    def test_negative_side(self):
        assert right_angle_triangle(-3, 4, 5) == False

    def test_float_right_triangle(self):
        assert right_angle_triangle(3.0, 4.0, 5.0) == True

    def test_float_invalid_triangle(self):
        assert right_angle_triangle(1.0, 2.0, 3.0) == False

    def test_equal_sides_not_right(self):
        assert right_angle_triangle(2, 2, 2) == False