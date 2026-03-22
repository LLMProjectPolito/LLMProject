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
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True
    assert right_angle_triangle(1, 1, 1) == True

def test_right_angle_triangle_invalid():
    assert right_angle_triangle(1, 2, 5) == False
    assert right_angle_triangle(1, 2, 4) == False
    assert right_angle_triangle(1, 3, 2) == False
    assert right_angle_triangle(2, 1, 3) == False
    assert right_angle_triangle(1, 2, 1) == False
    assert right_angle_triangle(1, 1, 1) == False

def test_right_angle_triangle_zero_sides():
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(1, 1, 2) == False

def test_right_angle_triangle_large_numbers():
    assert right_angle_triangle(1000, 1000, 1000) == True
    assert right_angle_triangle(1000, 1001, 1001) == False