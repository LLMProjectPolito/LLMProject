
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
    (5, 4, 3, True),
    (4, 5, 3, True),
    (13, 12, 5, True),
    (12, 13, 5, True),
    (13, 5, 12, True),
    
    # Non-right triangles
    (1, 2, 3, False),
    (1, 1, 1, False),
    (2, 2, 3, False),
    (10, 10, 10, False),
    (5, 5, 8, False),
    
    # Edge cases: zeros and negatives
    (0, 0, 0, False),
    (0, 4, 5, False),
    (-3, -4, -5, False),
    
    # Floating point cases
    (0.3, 0.4, 0.5, True),
    (1.5, 2.0, 2.5, True),
])
def test_right_angle_triangle(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected