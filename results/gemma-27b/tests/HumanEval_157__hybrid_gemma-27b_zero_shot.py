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
        assert right_angle_triangle(6, 8, 10) == True
        assert right_angle_triangle(9, 12, 15) == True

    def test_invalid_right_triangle(self):
        assert right_angle_triangle(1, 2, 3) == False
        assert right_angle_triangle(2, 3, 4) == False
        assert right_angle_triangle(4, 5, 6) == False
        assert right_angle_triangle(7, 8, 9) == False
        assert right_angle_triangle(10, 11, 12) == False

    def test_zero_values(self):
        assert right_angle_triangle(0, 0, 0) == True  # Technically a degenerate triangle
        assert right_angle_triangle(0, 3, 5) == False
        assert right_angle_triangle(3, 0, 5) == False
        assert right_angle_triangle(3, 5, 0) == False

    def test_negative_values(self):
        assert right_angle_triangle(-3, 4, 5) == False
        assert right_angle_triangle(3, -4, 5) == False
        assert right_angle_triangle(3, 4, -5) == False
        assert right_angle_triangle(-3, -4, -5) == False

    def test_equal_sides(self):
        assert right_angle_triangle(1, 1, 1) == False
        assert right_angle_triangle(1, 1, 1.41421356237) == True #approx sqrt(2)
        assert right_angle_triangle(1, 1, 2) == False

    def test_large_numbers(self):
        assert right_angle_triangle(1000, 1000, 1414.21356237) == True #approx sqrt(2)*1000
        assert right_angle_triangle(1000, 1000, 1415) == False

    def test_floating_point_numbers(self):
        assert right_angle_triangle(3.0, 4.0, 5.0) == True
        assert right_angle_triangle(3.1, 4.1, 5.1) == False
        assert right_angle_triangle(0.3, 0.4, 0.5) == True
        assert right_angle_triangle(0.6, 0.8, 1.0) == True

    def test_order_of_inputs(self):
        assert right_angle_triangle(4, 3, 5) == True
        assert right_angle_triangle(5, 3, 4) == True
        assert right_angle_triangle(3, 5, 4) == True

    def test_edge_case_close_to_right_triangle(self):
        assert right_angle_triangle(3, 4, 5.000000001) == False
        assert right_angle_triangle(3, 4, 4.999999999) == False

    def test_degenerate_triangle(self):
        assert right_angle_triangle(1, 2, 3) == False
        assert right_angle_triangle(5, 12, 13) == True

    def test_equal_sides_approx(self):
        assert right_angle_triangle(1, 1, 1.41421356237) == True
        assert right_angle_triangle(2, 2, 2.82842712475) == True