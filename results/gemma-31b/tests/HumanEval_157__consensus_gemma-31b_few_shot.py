
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
import itertools

@pytest.mark.parametrize("a, b, c, expected", [
    # Standard Pythagorean triples
    (3, 4, 5, True),
    (5, 12, 13, True),
    (8, 15, 17, True),
    (7, 24, 25, True),
    (20, 21, 29, True),
    
    # Permutations of sides to ensure hypotenuse is not hardcoded as 'c'
    (5, 3, 4, True),
    (4, 5, 3, True),
    (13, 5, 12, True),
    (12, 13, 5, True),
    (17, 8, 15, True),
    (15, 17, 8, True),
    
    # Non-right triangles
    (1, 2, 3, False),    # Degenerate/Linear
    (1, 1, 1, False),    # Equilateral
    (2, 2, 3, False),    # Obtuse
    (2, 2, 2, False),    # Equilateral
    (4, 5, 6, False),    # Acute
    (10, 10, 10, False),
    (3, 3, 4, False),    # Isosceles
    (5, 5, 8, False),
    (2, 3, 4, False),    # Scalene non-right
    
    # Edge cases: Zeroes, Negatives, and Invalid Triangles
    (0, 0, 0, False),
    (0, 4, 5, False),
    (-3, -4, -5, False), 
    (1, 1, 10, False),
    
    # Floating point values
    (1.0, 1.0, 2.0**0.5, True),
    (0.3, 0.4, 0.5, True),
    
    # Large numbers
    (300, 400, 500, True),
    (2000, 2100, 2900, True),
    (800, 1500, 1700, True),
    
    # Almost right triangles (precision checks)
    (3, 4, 5.1, False),
    (3, 4, 4.9, False),
])
def test_right_angle_triangle(a, b, c, expected):
    """
    Test the right_angle_triangle function with various side lengths,
    including valid triples, permutations, non-right triangles, and edge cases.
    """
    assert right_angle_triangle(a, b, c) == expected

@pytest.mark.parametrize("a, b, c", [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
])
def test_right_angle_triangle_all_permutations(a, b, c):
    """Test all permutations of known right triangles to ensure robustness."""
    for p in itertools.permutations([a, b, c]):
        assert right_angle_triangle(*p) is True