
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

    if a + b <= c or a + c <= b or b + c <= a:
        return False

    sides = [a, b, c]
    max_side = max(sides)
    other_sides = [side for side in sides if side != max_side]

    return abs(other_sides[0]**2 + other_sides[1]**2 - max_side**2) < 1e-6

### Tests (Pytest):

def test_valid_right_triangles():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True

def test_invalid_triangles():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(2, 2, 3) == False

def test_invalid_input():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(0, 0, 0) == False

def test_triangle_inequality_fail():
    assert right_angle_triangle(1, 2, 5) == False
    assert right_angle_triangle(1, 5, 2) == False
    assert right_angle_triangle(5, 1, 2) == False

def test_isosceles_right_triangle():
    assert right_angle_triangle(1, 1, 1.41421356) == True