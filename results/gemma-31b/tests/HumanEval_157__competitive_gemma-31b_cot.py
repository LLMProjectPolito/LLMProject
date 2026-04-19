
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

@pytest.mark.parametrize("a, b, c, expected", [
    (3, 4, 5, True),
    (5, 4, 3, True),
    (4, 5, 3, True),
    (5, 12, 13, True),
    (8, 15, 17, True),
    (7, 24, 25, True),
    (1, 2, 3, False),
    (2, 2, 2, False),
    (1, 1, 1, False),
    (10, 11, 12, False),
    (0.3, 0.4, 0.5, True),
    (0.6, 0.8, 1.0, True),
    (1, 1, 1.4142135623730951, True), # sqrt(2)
    (0, 0, 0, True), # Mathematically 0^2 + 0^2 = 0^2
    (-3, -4, -5, True), # Squares make them positive
])
def test_right_angle_triangle(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

def test_large_numbers():
    # 3000, 4000, 5000
    assert right_angle_triangle(3000, 4000, 5000) is True

def test_non_right_triangle_close_call():
    # 3, 4, 5.1 is not right angled
    assert right_angle_triangle(3, 4, 5.1) is False