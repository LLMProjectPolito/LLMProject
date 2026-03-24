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

    # Input Validation: Check for valid triangle inequality and non-negative sides
    if not (a > 0 and b > 0 and c > 0):
        return False
    if not (a + b > c and a + c > b and b + c > a):
        return False

    return a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2


import pytest

def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(6, 8, 10) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(3, 5, 4) == True  # Different order
    assert right_angle_triangle(4, 3, 5) == True  # Different order
    assert right_angle_triangle(5, 4, 3) == True  # Different order
    assert right_angle_triangle(5.0, 12.0, 13.0) == True # Floating point
    assert right_angle_triangle(3.0, 4.0, 5.0) == True # Floating point

def test_right_angle_triangle_invalid():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(2, 2, 3) == False # Two sides equal, not a right triangle

def test_right_angle_triangle_zero_side():
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 4, 0) == False

def test_right_angle_triangle_negative_side():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False

def test_right_angle_triangle_triangle_inequality_fail():
    assert right_angle_triangle(1, 2, 5) == False  # 1 + 2 < 5
    assert right_angle_triangle(1, 5, 2) == False  # 1 + 2 < 5
    assert right_angle_triangle(5, 1, 2) == False  # 1 + 2 < 5