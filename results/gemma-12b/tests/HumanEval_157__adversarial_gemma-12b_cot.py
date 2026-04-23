
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
    if not all(isinstance(side, (int, float)) for side in [a, b, c]):
        raise TypeError("Sides must be numbers (int or float)")

    if any(side <= 0 for side in [a, b, c]):
        return False

    if not (a + b > c and a + c > b and b + c > a):
        return False

    sides = sorted([a, b, c])
    return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-6

@pytest.mark.parametrize("a, b, c, expected", [
    (3, 4, 5, True),
    (5, 12, 13, True),
    (1, 2, 3, False),
    (2, 3, 4, False),
    (4, 3, 5, True),  # Unsorted
    (5, 4, 3, True),
    (3, 5, 4, True),
    (0, 4, 5, False),  # Zero length
    (-3, 4, 5, False), # Negative length
    (3, -4, 5, False),
    (3, 4, -5, False),
    (1.0, 2.0, 2.236067977, True), # Float values
    (3.0, 4.0, 5.0, True),
    (1, 1, 1, False),
    (1, 1, 1.41421356, True),
    (2, 2, 2, False),
    (1, 2, 2.5, True),
])
def test_right_angle_triangle(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

def test_type_error():
    with pytest.raises(TypeError):
        right_angle_triangle("a", 4, 5)
    with pytest.raises(TypeError):
        right_angle_triangle(3, "b", 5)
    with pytest.raises(TypeError):
        right_angle_triangle(3, 4, "c")
    with pytest.raises(TypeError):
        right_angle_triangle([1,2], 4, 5)