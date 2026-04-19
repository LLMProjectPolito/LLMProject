
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
    (17, 8, 15, True),
    (15, 17, 8, True),
    
    # Non-right triangles
    (1, 2, 3, False),    # Degenerate (collinear)
    (3, 3, 3, False),    # Equilateral
    (2, 2, 3, False),    # Isosceles obtuse
    (2, 2, 1, False),    # Isosceles acute
    (10, 10, 10, False), # Equilateral
    (3, 4, 6, False),    # Obtuse
    (4, 5, 6, False),    # Acute
    (3, 3, 4, False),    # Acute
    (2, 3, 4, False),    # Obtuse
    
    # Edge cases: Zero, Negative lengths, and Triangle Inequality
    (0, 0, 0, False),
    (0, 4, 5, False),
    (-3, -4, -5, False),
    (-3, 4, 5, False),
    (1, 1, 10, False),   # Cannot physically form a triangle
    
    # Floating point cases
    (1.0, 1.0, math.sqrt(2), True),
    (0.3, 0.4, 0.5, True),
    (1.0, 1.0, 2.0, False),
    (1.0, 1.0, 1.41, False), # Close but not exactly sqrt(2)
])
def test_right_angle_triangle_parametrized(a, b, c, expected):
    """Tests the right_angle_triangle function with various side lengths."""
    assert right_angle_triangle(a, b, c) == expected

def test_right_angle_triangle_large_numbers():
    """Test with very large numbers to check for overflow or precision."""
    assert right_angle_triangle(300, 400, 500) is True
    assert right_angle_triangle(1000, 2400, 2600) is True
    assert right_angle_triangle(3000, 4000, 5000) is True
    assert right_angle_triangle(3000000, 4000000, 5000000) is True