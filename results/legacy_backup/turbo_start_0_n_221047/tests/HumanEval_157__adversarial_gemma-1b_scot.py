import pytest

def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    """
    sides = sorted([a, b, c])
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False

def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(4, 3, 5) == True
    assert right_angle_triangle(7, 9, 11) == True

def test_right_angle_triangle_invalid():
    assert right_angle_triangle(1, 2, 5) == False
    assert right_angle_triangle(1, 2, 4) == False
    assert right_angle_triangle(1, 2, 1) == False
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(1, 2, 10) == False

def test_right_angle_triangle_degenerate():
    assert right_angle_triangle(1, 1, 1) == True
    assert right_angle_triangle(1, 1, 2) == False
    assert right_angle_triangle(1, 1, 0) == False

def test_right_angle_triangle_large_numbers():
    assert right_angle_triangle(1000, 1000, 1000) == True
    assert right_angle_triangle(1000, 1001, 1001) == True
    assert right_angle_triangle(1000, 1002, 1002) == False