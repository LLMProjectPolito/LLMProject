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

    return isclose(a**2 + b**2, c**2) or isclose(a**2 + c**2, b**2) or isclose(b**2 + c**2, a**2)


class TestRightAngleTriangle:
    def test_valid_right_triangle(self):
        assert right_angle_triangle(3, 4, 5) == True
        assert right_angle_triangle(5, 12, 13) == True
        assert right_angle_triangle(8, 15, 17) == True
        assert right_angle_triangle(6, 8, 10) == True

    def test_invalid_right_triangle(self):
        assert right_angle_triangle(1, 2, 3) == False
        assert right_angle_triangle(2, 3, 4) == False
        assert right_angle_triangle(5, 5, 5) == False

    def test_float_right_triangle(self):
        assert right_angle_triangle(3.0, 4.0, 5.0) == True
        assert right_angle_triangle(5.0, 12.0, 13.0) == True
        assert right_angle_triangle(0.3, 0.4, 0.5) == True

    def test_mixed_type_right_triangle(self):
        assert right_angle_triangle(3, 4.0, 5) == True
        assert right_angle_triangle(3.0, 4, 5) == True

    def test_zero_length_side(self):
        assert right_angle_triangle(0, 4, 5) == False
        assert right_angle_triangle(3, 0, 5) == False
        assert right_angle_triangle(3, 4, 0) == False

    def test_negative_length_side(self):
        assert right_angle_triangle(-3, 4, 5) == False
        assert right_angle_triangle(3, -4, 5) == False
        assert right_angle_triangle(3, 4, -5) == False

    def test_invalid_triangle_inequality(self):
        assert right_angle_triangle(1, 2, 5) == False
        assert right_angle_triangle(1, 5, 2) == False
        assert right_angle_triangle(5, 1, 2) == False

    def test_type_error(self):
        with pytest.raises(TypeError):
            right_angle_triangle("a", 4, 5)
        with pytest.raises(TypeError):
            right_angle_triangle(3, "b", 5)
        with pytest.raises(TypeError):
            right_angle_triangle(3, 4, "c")
        with pytest.raises(TypeError):
            right_angle_triangle([1,2,3], 4, 5)