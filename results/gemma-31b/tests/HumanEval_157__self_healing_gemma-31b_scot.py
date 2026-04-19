
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

import math
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
    # A triangle must have positive side lengths
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    # Sort the sides to identify the hypotenuse (the longest side)
    sides = sorted([a, b, c])
    
    # Use the Pythagorean theorem: a^2 + b^2 = c^2
    # math.isclose is used to handle floating point precision issues
    return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

@pytest.mark.parametrize("a, b, c, expected", [
    # Standard Pythagorean triples
    (3, 4, 5, True),
    (5, 12, 13, True),
    (8, 15, 17, True),
    (7, 24, 25, True),
    (20, 21, 29, True),
    
    # Permutations of sides to ensure hypotenuse isn't assumed to be the last argument
    (5, 3, 4, True),
    (5, 4, 3, True),
    (4, 3, 5, True),
    (4, 5, 3, True),
    (3, 5, 4, True),
    
    # Non-right triangles
    (1, 2, 3, False),
    (2, 2, 2, False),
    (10, 11, 12, False),
    (5, 5, 5, False),
    (6, 7, 8, False),
    
    # Edge cases: Degenerate triangles or invalid lengths
    (0, 0, 0, False),
    (1, 1, 2, False),
    
    # Floating point values
    (1.0, 1.0, 2**0.5, True),
    (0.3, 0.4, 0.5, True),
    (1.1, 1.1, 1.5, False),
])
def test_right_angle_triangle(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected