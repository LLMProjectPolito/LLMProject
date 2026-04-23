
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

class TestRightAngleTriangle:

    def test_positive_right_triangle(self):
        assert right_angle_triangle(3, 4, 5) == True
        assert right_angle_triangle(5, 12, 13) == True
        assert right_angle_triangle(8, 15, 17) == True
        assert right_angle_triangle(7, 24, 25) == True
        assert right_angle_triangle(20, 21, 29) == True

    def test_positive_not_right_triangle(self):
        assert right_angle_triangle(1, 2, 3) == False
        assert right_angle_triangle(4, 5, 6) == False
        assert right_angle_triangle(10, 10, 10) == False
        assert right_angle_triangle(5, 10, 15) == False
        assert right_angle_triangle(1, 1, 1) == False

    def test_zero_length_sides(self):
        assert right_angle_triangle(0, 0, 0) == False
        assert right_angle_triangle(0, 1, 1) == False
        assert right_angle_triangle(1, 0, 1) == False
        assert right_angle_triangle(1, 1, 0) == False
        assert right_angle_triangle(0, 0, 1) == False

    def test_negative_length_sides(self):
        with pytest.raises(ValueError):
            right_angle_triangle(-3, 4, 5)
        with pytest.raises(ValueError):
            right_angle_triangle(3, -4, 5)
        with pytest.raises(ValueError):
            right_angle_triangle(3, 4, -5)
        with pytest.raises(ValueError):
            right_angle_triangle(-3, -4, 5)
        with pytest.raises(ValueError):
            right_angle_triangle(3, -4, -5)
        with pytest.raises(ValueError):
            right_angle_triangle(-3, 4, -5)
        with pytest.raises(ValueError):
            right_angle_triangle(-3, -4, -5)

    def test_equal_sides(self):
        assert right_angle_triangle(5, 5, 5) == False
        assert right_angle_triangle(1, 1, 1) == False
        assert right_angle_triangle(2, 2, 2) == False

    def test_edge_cases(self):
        assert right_angle_triangle(1, 1, 1.41421356) == True # Approximating sqrt(2)
        assert right_angle_triangle(1000, 1000, 1414.21356) == True # larger numbers
        assert right_angle_triangle(1.0, 1.0, 1.41421356) == True # small numbers
        assert right_angle_triangle(0.1, 0.1, 0.141421356) == True # very small numbers

    def test_invalid_input_types(self):
        with pytest.raises(TypeError):
            right_angle_triangle("3", 4, 5)
        with pytest.raises(TypeError):
            right_angle_triangle(3, "4", 5)
        with pytest.raises(TypeError):
            right_angle_triangle(3, 4, "5")
        with pytest.raises(TypeError):
            right_angle_triangle(3.5, 4, 5)
        with pytest.raises(TypeError):
            right_angle_triangle(3, 4.5, 5)
        with pytest.raises(TypeError):
            right_angle_triangle(3, 4, 5.5)