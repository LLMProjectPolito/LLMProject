
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
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Sides must be positive.")
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2

import pytest

def test_right_angle_triangle_basic():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True

def test_right_angle_triangle_not_right():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(1, 1, 1) == False

def test_right_angle_triangle_different_order():
    assert right_angle_triangle(4, 3, 5) == True
    assert right_angle_triangle(13, 12, 5) == True

def test_right_angle_triangle_zero_side():
    with pytest.raises(ValueError):
        right_angle_triangle(0, 4, 5)
    with pytest.raises(ValueError):
        right_angle_triangle(3, 0, 5)
    with pytest.raises(ValueError):
        right_angle_triangle(3, 4, 0)

def test_right_angle_triangle_negative_side():
    with pytest.raises(ValueError):
        right_angle_triangle(-3, 4, 5)
    with pytest.raises(ValueError):
        right_angle_triangle(3, -4, 5)
    with pytest.raises(ValueError):
        right_angle_triangle(3, 4, -5)

def test_right_angle_triangle_equal_sides():
    assert right_angle_triangle(5, 5, 5) == False

def test_right_angle_triangle_large_numbers():
    assert right_angle_triangle(1000, 1000, 1414) == True

def test_right_angle_triangle_float_numbers():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(1.0, 2.0, 3.0) == False

def test_right_angle_triangle_close_to_right():
    assert right_angle_triangle(3.0, 4.0, 5.000000000000001) == True # Test floating point precision

def test_right_angle_triangle_extremely_large_numbers():
    assert right_angle_triangle(1e12, 1e12, 1e12 * 1.41421356) == True