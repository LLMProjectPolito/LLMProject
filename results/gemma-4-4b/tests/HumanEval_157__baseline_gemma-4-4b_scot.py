
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

import pytest

def test_right_angle_triangle_positive_case():
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_another_positive_case():
    assert right_angle_triangle(5, 12, 13) == True

def test_right_angle_triangle_different_sides():
    assert right_angle_triangle(8, 15, 17) == True

def test_right_angle_triangle_not_right_angle():
    assert right_angle_triangle(1, 2, 3) == False

def test_right_angle_triangle_isosceles_not_right_angle():
    assert right_angle_triangle(5, 5, 6) == False

def test_right_angle_triangle_zero_side():
    assert right_angle_triangle(0, 4, 5) == False

def test_right_angle_triangle_negative_side():
    with pytest.raises(ValueError):
        right_angle_triangle(-3, 4, 5)

def test_right_angle_triangle_zero_and_negative_side():
    with pytest.raises(ValueError):
        right_angle_triangle(0, -4, 5)

def test_right_angle_triangle_all_zero():
    assert right_angle_triangle(0, 0, 0) == False

def test_right_angle_triangle_large_numbers():
    assert right_angle_triangle(1000, 1000, 1414) == True

def test_right_angle_triangle_decimal_numbers():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True

def test_right_angle_triangle_decimal_not_right_angle():
    assert right_angle_triangle(1.0, 2.0, 3.0) == False