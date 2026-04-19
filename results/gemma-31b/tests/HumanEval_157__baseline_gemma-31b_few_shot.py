
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
    (3, 4, 5, True),    # Standard 3-4-5 triple
    (5, 12, 13, True),  # Standard 5-12-13 triple
    (8, 15, 17, True),  # Standard 8-15-17 triple
    (5, 3, 4, True),    # Hypotenuse in middle
    (5, 4, 3, True),    # Hypotenuse first
    (1, 2, 3, False),   # Not a right triangle
    (2, 2, 2, False),   # Equilateral triangle
    (1, 1, 2, False),   # Degenerate triangle
    (0, 0, 0, False),   # Zero lengths
])
def test_right_angle_triangle_basic(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

def test_right_angle_triangle_floats():
    # Testing with floating point values (1, 1, sqrt(2))
    # Note: Depending on implementation, floating point precision might be an issue
    assert right_angle_triangle(1.0, 1.0, 2**0.5) == True

def test_right_angle_triangle_large_numbers():
    # Testing with larger Pythagorean triples
    assert right_angle_triangle(20, 21, 29) == True
    assert right_angle_triangle(100, 200, 300) == False

def test_right_angle_triangle_negative_values():
    # Geometrically impossible, but checking mathematical property a^2 + b^2 = c^2
    # If the function only accepts positive lengths, this should be False
    # If it just checks the formula, it might be True. 
    # Usually, a triangle cannot have negative sides.
    assert right_angle_triangle(-3, -4, -5) == True # (-3)^2 + (-4)^2 = (-5)^2