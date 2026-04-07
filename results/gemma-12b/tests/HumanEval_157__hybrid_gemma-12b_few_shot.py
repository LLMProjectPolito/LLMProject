
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
from math import sqrt

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
    """
    Pytest class for testing the right_angle_triangle function.
    """

    def test_valid_right_triangle(self):
        """Tests with valid right-angled triangles."""
        assert right_angle_triangle(3, 4, 5) == True
        assert right_angle_triangle(5, 12, 13) == True
        assert right_angle_triangle(8, 15, 17) == True
        assert right_angle_triangle(7, 24, 25) == True
        assert right_angle_triangle(6, 8, 10) == True  # Multiple of 3-4-5
        assert right_angle_triangle(20, 21, 29) == True

    def test_invalid_right_triangle(self):
        """Tests with triangles that are not right-angled."""
        assert right_angle_triangle(1, 2, 3) == False
        assert right_angle_triangle(1, 1, 1) == False
        assert right_angle_triangle(2, 3, 4) == False
        assert right_angle_triangle(10, 11, 12) == False
        assert right_angle_triangle(5, 5, 5) == False

    def test_zero_length_side(self):
        """Tests with a zero-length side (should not be a triangle)."""
        assert right_angle_triangle(0, 0, 0) == False
        assert right_angle_triangle(0, 3, 4) == False
        assert right_angle_triangle(3, 0, 4) == False
        assert right_angle_triangle(3, 4, 0) == False

    def test_negative_length_side(self):
        """Tests with a negative length side (invalid input)."""
        assert right_angle_triangle(-3, 4, 5) == False
        assert right_angle_triangle(3, -4, 5) == False
        assert right_angle_triangle(3, 4, -5) == False
        assert right_angle_triangle(-3, -4, -5) == False

    def test_equal_sides(self):
        """Tests with triangles having two or three equal sides."""
        assert right_angle_triangle(5, 5, 5) == False
        assert right_angle_triangle(5, 5, 7) == False
        assert right_angle_triangle(5, 7, 5) == False
        assert right_angle_triangle(7, 5, 5) == False

    def test_large_numbers(self):
        """Tests with large numbers to check for potential overflow issues."""
        assert right_angle_triangle(1000, 1000, sqrt(2000000)) == True
        assert right_angle_triangle(10000, 10000, sqrt(200000000)) == True
        assert right_angle_triangle(100000, 100000, sqrt(20000000000)) == True

    def test_floating_point_numbers(self):
        """Tests with floating-point numbers (should still work correctly)."""
        assert right_angle_triangle(3.0, 4.0, 5.0) == True
        assert right_angle_triangle(5.0, 12.0, 13.0) == True
        assert right_angle_triangle(1.0, 2.0, 3.0) == False

    def test_mixed_types(self):
        """Tests with mixed types (should raise TypeError)."""
        with pytest.raises(TypeError):
            right_angle_triangle("3", 4, 5)
        with pytest.raises(TypeError):
            right_angle_triangle(3, "4", 5)
        with pytest.raises(TypeError):
            right_angle_triangle(3, 4, "5")