
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
    a, b, c = sides[0], sides[1], sides[2]

    if a <= 0 or b <= 0 or c <= 0:
        return False

    if a + b <= c:
        return False

    return a**2 + b**2 == c**2

def test_valid_right_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True

def test_not_right_triangle():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(6, 8, 10) == False
    assert right_angle_triangle(1, 1, 1) == False

def test_invalid_input_zero():
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 4, 0) == False

def test_invalid_input_negative():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False

def test_triangle_inequality_violation():
    assert right_angle_triangle(1, 2, 5) == False
    assert right_angle_triangle(1, 5, 2) == False
    assert right_angle_triangle(5, 1, 2) == False

def test_same_sides():
    assert right_angle_triangle(5, 5, 5) == False

def test_isosceles_not_right():
    assert right_angle_triangle(5, 5, 6) == False
    assert right_angle_triangle(5, 6, 5) == False
    assert right_angle_triangle(6, 5, 5) == False

def test_large_numbers():
    assert right_angle_triangle(65, 72, 97) == True
    assert right_angle_triangle(1000, 1000, 1414) == False #approx sqrt(2)