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

    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2

### Tests (Pytest):
import pytest

def test_right_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True

def test_right_triangle_invalid():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(2, 2, 3) == False

def test_right_triangle_with_negative_sides():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False

def test_right_triangle_with_zero_sides():
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 4, 0) == False

def test_right_triangle_triangle_inequality_fail():
    assert right_angle_triangle(1, 2, 4) == False
    assert right_angle_triangle(1, 2, 5) == False

def test_right_triangle_equal_sides_large_third():
    assert right_angle_triangle(5, 5, 10) == False

def test_right_triangle_with_floating_point_numbers():
    assert right_angle_triangle(0.3, 0.4, 0.5) == True

def test_right_triangle_different_order():
    assert right_angle_triangle(4, 3, 5) == True
    assert right_angle_triangle(5, 3, 4) == True