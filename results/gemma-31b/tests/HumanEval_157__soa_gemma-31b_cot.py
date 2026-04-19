
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
    
    # Non-right triangles (Acute)
    (2, 2, 2, False),
    (4, 4, 5, False),
    (6, 6, 6, False),
    
    # Non-right triangles (Obtuse)
    (1, 2, 3, False), # Degenerate/Obtuse
    (2, 3, 4, False),
    (10, 10, 15, False),
    
    # Edge cases: Very small values
    (0.3, 0.4, 0.5, True),
    (0.003, 0.004, 0.005, True),
    
    # Edge cases: Invalid triangle sides (should be False)
    (0, 0, 0, False),
    (-3, -4, -5, False),
    (1, 1, 10, False),
])
def test_right_angle_triangle(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

def test_floating_point_precision():
    # Testing with sqrt(2) case: 1^2 + 1^2 = (sqrt(2))^2
    # Note: This depends on the function's implementation of float comparison
    import math
    assert right_angle_triangle(1, 1, math.sqrt(2)) is True