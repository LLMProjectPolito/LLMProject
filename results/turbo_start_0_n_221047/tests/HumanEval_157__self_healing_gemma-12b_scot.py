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

    def test_invalid_triangle(self):
        assert right_angle_triangle(1, 2, 3) == False

    def test_zero_length_sides(self):
        assert right_angle_triangle(0, 0, 0) == False

    def test_negative_length_sides(self):
        assert right_angle_triangle(-1, -2, -3) == False

    def test_isosceles_right_triangle(self):
        assert right_angle_triangle(1, 1, pytest.approx(2**0.5)) == True

    def test_floating_point_numbers(self):
        assert right_angle_triangle(3.0, 4.0, 5.0) == True

    def test_large_numbers(self):
        assert right_angle_triangle(1000, 1000, pytest.approx(1000 * (2**0.5))) == True

    def test_different_order(self):
        assert right_angle_triangle(5, 3, 4) == True
        assert right_angle_triangle(4, 5, 3) == True
        assert right_angle_triangle(4, 3, 5) == True

    def test_not_a_triangle(self):
        assert right_angle_triangle(1, 2, 5) == False