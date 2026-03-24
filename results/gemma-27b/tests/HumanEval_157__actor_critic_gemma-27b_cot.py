
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
import math

def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(5.0, 12.0, 13.0) == True
    assert right_angle_triangle(1.5, 2.0, 2.5) == True

def test_right_angle_triangle_invalid():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(6, 8, 11) == False
    assert right_angle_triangle(6, 8, 10) == False

@pytest.mark.parametrize("a, b, c", [
    (0, 0, 0),
    (0, 4, 5),
    (3, 0, 5),
    (3, 4, 0),
    (0, 0, 5)
])
def test_right_angle_triangle_zero(a, b, c):
    assert right_angle_triangle(a, b, c) == False

@pytest.mark.parametrize("a, b, c", [
    (-3, 4, 5),
    (3, -4, 5),
    (3, 4, -5),
    (-3, -4, -5)
])
def test_right_angle_triangle_negative(a, b, c):
    assert right_angle_triangle(a, b, c) == False

def test_triangle_inequality():
    assert right_angle_triangle(1, 2, 5) == False
    assert right_angle_triangle(1, 5, 2) == False
    assert right_angle_triangle(5, 1, 2) == False
    assert right_angle_triangle(2, 1, 5) == False
    assert right_angle_triangle(2, 5, 1) == False
    assert right_angle_triangle(5, 2, 1) == False

def test_right_angle_triangle_large_numbers():
    assert pytest.approx(right_angle_triangle(1000, 1000, math.sqrt(2000000))) == True

def test_right_angle_triangle_same_sides():
    assert right_angle_triangle(5, 5, 5) == False
    assert right_angle_triangle(10, 10, 10) == False

def test_right_angle_triangle_edge_case():
    assert pytest.approx(right_angle_triangle(1, 1, math.sqrt(2))) == True

@pytest.mark.parametrize("a, b, c", [
    ("3", 4, 5),
    (3, "4", 5),
    (3, 4, "5"),
    ([3], 4, 5),
    (3, [4], 5),
    (3, 4, [5])
])
def test_right_angle_triangle_invalid_input(a, b, c):
    with pytest.raises(TypeError):
        right_angle_triangle(a, b, c)