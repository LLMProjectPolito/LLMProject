
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
    (1, 2, 3, False), # Degenerate triangle
    (2, 2, 2, False), # Equilateral
    (2, 2, 3, False), # Isosceles
    (4, 4, 4, False),
    (10, 10, 10, False),
    (5, 5, 8, False),
    
    # Floating point values
    (1, 1, 2**0.5, True),
    (1.5, 2.0, 2.5, True),
    (1.1, 1.1, 1.5, False),
    
    # Edge cases: Zero and Negative values
    (0, 0, 0, False),
    (0, 4, 5, False),
    (-3, -4, -5, False),
    (-3, 4, 5, False),
])
def test_right_angle_triangle(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected