
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
    (17, 15, 8, True),
    (13, 5, 12, True),
    (12, 13, 5, True),
    
    # Non-right triangles
    (1, 2, 3, False),  # Degenerate/Linear
    (5, 5, 5, False),  # Equilateral
    (2, 2, 2, False),  # Equilateral
    (10, 10, 10, False), # Equilateral
    (2, 2, 3, False),  # Isosceles obtuse
    (2, 2, 2.5, False), # Isosceles acute
    (10, 11, 12, False), # Scalene
    (3, 4, 6, False),  # Obtuse
    (3, 4, 4, False),  # Acute
    (2, 3, 4, False),  # Obtuse
    (3, 3, 4, False),  # Acute
    
    # Edge cases: Zero or negative lengths
    (0, 0, 0, False),
    (-3, -4, -5, False),
    (3, 4, 0, False),
    (0, 4, 5, False),
    (3, -4, 5, False),
    (-3, 4, 5, False),
    
    # Floating point values
    (1.0, 1.0, 2**0.5, True), 
    (0.3, 0.4, 0.5, True),
    (1.0, 1.0, math.sqrt(2), True),
    (1.0, 1.0, 1.414, False), # Close but not exact
    (1.0, 1.0, 1.4142135623730951, True),
])
def test_right_angle_triangle(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

def test_large_values():
    # Testing with larger integers to ensure no overflow/precision issues
    assert right_angle_triangle(300, 400, 500) is True
    assert right_angle_triangle(3000, 4000, 5000) is True
    assert right_angle_triangle(800, 1500, 1700) is True
    assert right_angle_triangle(1000, 1000, 1000) is False
    assert right_angle_triangle(1000000, 1000000, 2000000) is False

def test_invalid_triangle_inequality():
    # Test cases where sides cannot physically form a triangle
    assert right_angle_triangle(1, 1, 10) is False