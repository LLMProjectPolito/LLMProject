
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
from math import isclose

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
    if not all(isinstance(side, (int, float)) for side in [a, b, c]):
        raise TypeError("Sides must be numbers (int or float)")

    if any(side <= 0 for side in [a, b, c]):
        return False

    if not (a + b > c and a + c > b and b + c > a):
        return False

    sides = sorted([a, b, c])
    return isclose(sides[0]**2 + sides[1]**2, sides[2]**2)


class TestRightAngleTriangle:
    def test_valid_right_triangle_int(self):
        assert right_angle_triangle(3, 4, 5) == True

    def test_valid_right_triangle_float(self):
        assert right_angle_triangle(3.0, 4.0, 5.0) == True

    def test_non_right_triangle_int(self):
        assert right_angle_triangle(1, 2, 3) == False

    def test_non_right_triangle_float(self):
        assert right_angle_triangle(1.0, 2.0, 3.0) == False

    def test_unsorted_sides(self):
        assert right_angle_triangle(4, 3, 5) == True

    def test_zero_side(self):
        assert right_angle_triangle(0, 4, 5) == False
        assert right_angle_triangle(3, 0, 5) == False
        assert right_angle_triangle(3, 4, 0) == False

    def test_negative_side(self):
        assert right_angle_triangle(-3, 4, 5) == False
        assert right_angle_triangle(3, -4, 5) == False
        assert right_angle_triangle(3, 4, -5) == False

    def test_mixed_types(self):
        assert right_angle_triangle(3, 4.0, 5) == True

    def test_large_numbers(self):
        assert right_angle_triangle(600, 800, 1000) == True

    def test_floating_point_precision(self):
        assert right_angle_triangle(0.3, 0.4, 0.5) == True

    def test_type_error(self):
        with pytest.raises(TypeError):
            right_angle_triangle("a", 4, 5)
        with pytest.raises(TypeError):
            right_angle_triangle(3, "b", 5)
        with pytest.raises(TypeError):
            right_angle_triangle(3, 4, "c")
        with pytest.raises(TypeError):
            right_angle_triangle([1,2], 4, 5)