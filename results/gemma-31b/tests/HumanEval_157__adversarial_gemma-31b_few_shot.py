
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

def test_right_angle_basic():
    """ Test standard Pythagorean triples """
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True

def test_right_angle_permutations():
    """ 
    Test that the function identifies the hypotenuse regardless of 
    the order of arguments (a, b, c).
    """
    assert right_angle_triangle(5, 3, 4) == True  # Hypotenuse first
    assert right_angle_triangle(3, 5, 4) == True  # Hypotenuse second
    assert right_angle_triangle(4, 3, 5) == True  # Hypotenuse third

def test_right_angle_false_cases():
    """ Test triangles that are valid but not right-angled """
    assert right_angle_triangle(2, 2, 2) == False  # Equilateral
    assert right_angle_triangle(2, 3, 4) == False  # Scalene
    assert right_angle_triangle(1, 1, 1) == False  # Small equilateral

def test_right_angle_degenerate_and_invalid():
    """ 
    Test edge cases where sides do not form a valid triangle 
    or are mathematically impossible.
    """
    assert right_angle_triangle(0, 0, 0) == False  # Zero length
    assert right_angle_triangle(1, 2, 3) == False  # Degenerate (flat line)
    assert right_angle_triangle(-3, 4, 5) == False # Negative length
    assert right_angle_triangle(0, 4, 5) == False  # One zero side

def test_right_angle_floats():
    """ Test with floating point numbers """
    # 1^2 + 1^2 = (sqrt(2))^2
    import math
    assert right_angle_triangle(1.0, 1.0, math.sqrt(2)) == True

@pytest.mark.parametrize("a, b, c, expected", [
    (3, 4, 5, True),
    (5, 12, 13, True),
    (1, 1, 1, False),
    (0, 0, 0, False),
    (10, 10, 10 * (2**0.5), True), # 45-45-90 triangle
])
def test_right_angle_parametrized(a, b, c, expected):
    """ Comprehensive check using parametrization """
    assert right_angle_triangle(a, b, c) == expected