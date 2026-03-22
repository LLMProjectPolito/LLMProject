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

def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True

def test_right_angle_triangle_invalid():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(6, 8, 10) == True # Test for multiples
    assert right_angle_triangle(1, 1, 1) == False

def test_right_angle_triangle_zero():
    assert right_angle_triangle(0, 0, 0) == True # Edge case: all zeros
    assert right_angle_triangle(0, 3, 5) == False # Edge case: one zero
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 5, 0) == False

def test_right_angle_triangle_negative():
    assert right_angle_triangle(-3, 4, 5) == False # Negative side
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False
    assert right_angle_triangle(-3, -4, -5) == False # All negative

def test_right_angle_triangle_order():
    assert right_angle_triangle(4, 3, 5) == True # Different order
    assert right_angle_triangle(5, 3, 4) == True
    assert right_angle_triangle(5, 4, 3) == True
    assert right_angle_triangle(13, 5, 12) == True