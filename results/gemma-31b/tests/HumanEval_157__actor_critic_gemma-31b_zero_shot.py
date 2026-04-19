
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

def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    '''
    # A triangle must have sides greater than 0
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    # Sort sides to easily identify the hypotenuse (longest side)
    sides = sorted([a, b, c])
    # Pythagorean theorem: a^2 + b^2 = c^2
    return sides[0]**2 + sides[1]**2 == sides[2]**2

@pytest.mark.parametrize("a, b, c, expected", [
    # Standard Pythagorean triples
    (3, 4, 5, True),
    (5, 12, 13, True),
    (8, 15, 17, True),
    (7, 24, 25, True),
    (20, 21, 29, True),
    
    # Permutations of sides (hypotenuse in different positions)
    (5, 3, 4, True),
    (4, 5, 3, True),
    (13, 12, 5, True),
    (12, 5, 13, True),
    
    # Non-right triangles
    (1, 2, 3, False),    # Degenerate triangle (1+2=3)
    (2, 2, 2, False),    # Equilateral (Removed redundant 10, 10, 10)
    (2, 2, 3, False),    # Isosceles
    (4, 5, 6, False),    # Scalene non-right
    
    # Edge cases: Zero and Negative values
    (0, 4, 5, False),    # Zero value (Removed redundant 0, 0, 0)
    (-3, -4, -5, False), # Mathematically squares match, but sides cannot be negative
    (-3, 4, 5, False),
    
    # Floating point cases
    (0.3, 0.4, 0.5, True), # Floating-point right triangle
    (1.0, 1.0, 2.0, False),
    (1, 1, math.sqrt(2), True), # Precision edge case to expose '==' logic error
])
def test_right_angle_triangle(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

def test_large_numbers():
    # Testing with larger Pythagorean triple
    assert right_angle_triangle(300, 400, 500) == True
    assert right_angle_triangle(1000, 2400, 2600) == True

def test_invalid_triangle_inequality():
    # Sides that cannot form any triangle (a + b < c)
    assert right_angle_triangle(1, 1, 10) == False