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

def test_right_angle_triangle_positive():
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_negative():
    assert right_angle_triangle(1, 2, 3) == False

def test_right_angle_triangle_zero():
    assert right_angle_triangle(0, 0, 0) == True

def test_right_angle_triangle_one():
    assert right_angle_triangle(1, 1, 1) == True

def test_right_angle_triangle_two():
    assert right_angle_triangle(2, 2, 2) == True

def test_right_angle_triangle_three():
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_four():
    assert right_angle_triangle(4, 5, 6) == True

def test_right_angle_triangle_five():
    assert right_angle_triangle(5, 6, 7) == True

def test_right_angle_triangle_six():
    assert right_angle_triangle(6, 7, 8) == True

def test_right_angle_triangle_seven():
    assert right_angle_triangle(7, 8, 9) == True

def test_right_angle_triangle_eight():
    assert right_angle_triangle(8, 9, 10) == True

def test_right_angle_triangle_nine():
    assert right_angle_triangle(9, 10, 11) == True

def test_right_angle_triangle_ten():
    assert right_angle_triangle(10, 11, 12) == True

def test_right_angle_triangle_negative_sides():
    assert right_angle_triangle(-1, 2, 3) == False

def test_right_angle_triangle_zero_side():
    assert right_angle_triangle(0, 2, 3) == False

def test_right_angle_triangle_one_side_zero():
    assert right_angle_triangle(1, 0, 3) == False

def test_right_angle_triangle_two_side_zero():
    assert right_angle_triangle(2, 0, 3) == False

def test_right_angle_triangle_three_side_zero():
    assert right_angle_triangle(3, 0, 2) == False