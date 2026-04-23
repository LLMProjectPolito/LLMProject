
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

def test_valid_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True
    assert right_angle_triangle(4, 3, 5) == True  # Different order

def test_invalid_triangle():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(6, 7, 8) == False
    assert right_angle_triangle(1, 1, 1.5) == False
    assert right_angle_triangle(2, 2, 2.1) == False

def test_zero_sides():
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 4, 0) == False
    assert right_angle_triangle(0, 0, 5) == False  # Two zeros

def test_negative_sides():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False
    assert right_angle_triangle(-3, -4, -5) == False

def test_float_sides():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(5.0, 12.0, 13.0) == True
    assert right_angle_triangle(1.5, 2.0, 2.5) == True
    assert right_angle_triangle(1.0, 2.0, 3.0) == False
    assert pytest.approx(right_angle_triangle(3.000001, 4.0, 5.0)) == False

def test_same_sides():
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(2, 2, 2) == False

def test_large_numbers():
    assert right_angle_triangle(1000, 1000, 1414) == False
    assert right_angle_triangle(1000, 1000, 1415) == False
    assert pytest.approx(right_angle_triangle(1000, 1000, 1414.21356)) == True
    assert right_angle_triangle(3000, 4000, 5000) == True
    assert right_angle_triangle(6000, 8000, 10000) == True

def test_invalid_input_types():
    with pytest.raises(TypeError):
        right_angle_triangle("3", 4, 5)
    with pytest.raises(TypeError):
        right_angle_triangle(3, "4", 5)
    with pytest.raises(TypeError):
        right_angle_triangle(3, 4, "5")
    with pytest.raises(TypeError):
        right_angle_triangle([3], 4, 5)