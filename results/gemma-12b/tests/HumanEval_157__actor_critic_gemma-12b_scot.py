
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
from your_module import right_angle_triangle  # Replace your_module

def test_valid_right_triangle():
    assert right_angle_triangle(3, 4, 5) == True

def test_valid_right_triangle_float():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True

def test_invalid_right_triangle():
    assert right_angle_triangle(1, 2, 3) == False

def test_negative_side():
    with pytest.raises(ValueError):
        right_angle_triangle(-3, 4, 5)

def test_invalid_input_type():
    with pytest.raises(TypeError):
        right_angle_triangle("3", 4, 5)
    with pytest.raises(TypeError):
        right_angle_triangle([3, 4, 5], 4, 5)
    with pytest.raises(TypeError):
        right_angle_triangle({"a": 3, "b": 4}, 4, 5)
    with pytest.raises(TypeError):
        right_angle_triangle(None, 4, 5)

def test_hypotenuse_as_a():
    with pytest.raises(ValueError):
        right_angle_triangle(5, 4, 3)

def test_hypotenuse_as_b():
    with pytest.raises(ValueError):
        right_angle_triangle(4, 5, 3)

def test_zero_hypotenuse():
    assert right_angle_triangle(0, 4, 5) == False

def test_two_sides_zero():
    assert right_angle_triangle(0, 0, 5) == False

def test_triangle_inequality():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 4, 3) == True
    assert right_angle_triangle(4, 5, 3) == True
    assert right_angle_triangle(1, 2, 5) == False
    assert right_angle_triangle(5, 2, 1) == False
    assert right_angle_triangle(2, 5, 1) == False

def test_very_small_numbers():
    assert pytest.approx(right_angle_triangle(0.001, 0.002, 0.003)) == False
    assert pytest.approx(right_angle_triangle(0.001, 0.002, 0.002999999999999)) == True

def test_mixed_input_types():
    with pytest.raises(TypeError):
        right_angle_triangle(3, "4.0", 5)

def test_isosceles_right_triangle():
    assert right_angle_triangle(1.41421356, 1.41421356, 2.0) == True

def test_large_numbers():
    assert right_angle_triangle(600, 800, 1000) == True

def test_equal_sides():
    assert right_angle_triangle(5, 5, 5) == False