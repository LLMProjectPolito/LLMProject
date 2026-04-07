
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
    if a <= 0 or b <= 0 or c <= 0:
        return False

    sides = [a, b, c]
    max_side = max(sides)
    other_sides = [side for side in sides if side != max_side]

    return other_sides[0]**2 + other_sides[1]**2 == max_side**2

### Tests (Pytest):

def test_valid_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True

def test_invalid_triangle():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(2, 2, 3) == False

def test_negative_or_zero_input():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 4, 0) == False

def test_triangle_inequality_fail():
    assert right_angle_triangle(1, 2, 4) == False
    assert right_angle_triangle(1, 2, 5) == False

def test_floating_point_precision():
    assert right_angle_triangle(1, 1, 1.41421356237) == True

def test_large_numbers():
    assert right_angle_triangle(1000, 1000, 1414.21356237) == True
    assert right_angle_triangle(1000000, 1000000, 1414213.56237) == True