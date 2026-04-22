
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
    (9, 40, 41, True),
    (11, 60, 61, True),
    # Large Pythagorean triples
    (300, 400, 500, True),
    (3000, 4000, 5000, True),
    # Floating point values
    (0.3, 0.4, 0.5, True),
    (1.5, 2.0, 2.5, True),
    (0.6, 0.8, 1.0, True),
    (1.2, 1.6, 2.0, True),
    # Permutations of side lengths (ensuring the function finds the hypotenuse)
    (4, 3, 5, True),
    (5, 3, 4, True),
    (3, 5, 4, True),
    (4, 5, 3, True),
    (5, 4, 3, True),
    (13, 12, 5, True),
    (12, 13, 5, True),
    (25, 24, 7, True),
    (24, 25, 7, True),
    (29, 21, 20, True),
    (41, 9, 40, True),
    (40, 41, 9, True),
    # Non-right-angled triangles
    (1, 2, 3, False),    # Degenerate triangle (line)
    (2, 2, 2, False),    # Equilateral triangle
    (5, 5, 5, False),    # Equilateral triangle
    (10, 10, 10, False), # Equilateral triangle
    (1, 1, 1, False),    # Equilateral triangle
    (3, 4, 6, False),    # Obtuse triangle
    (4, 5, 6, False),    # Acute triangle
    (5, 5, 8, False),    # Isosceles non-right
    (10, 11, 12, False), # Acute triangle
    (1, 1, 1.414, False),# Close to sqrt(2) but not exact
    (2, 3, 4, False),    # Acute triangle
    (10, 10, 14, False), # Isosceles non-right
    # Invalid/Impossible triangles (zero, negative, or triangle inequality violation)
    (0, 0, 0, False),
    (0, 3, 4, False),
    (3, 0, 4, False),
    (3, 4, 0, False),
    (-3, 4, 5, False),
    (3, -4, 5, False),
    (3, 4, -5, False),
    (-3, -4, -5, False),
    (1, 1, 10, False),   # Triangle inequality violation
    (10, 1, 1, False),   # Triangle inequality violation
])
def test_right_angle_triangle(a, b, c, expected):
    """
    Tests various scenarios for the right_angle_triangle function,
    including standard triples, permutations, floats, and invalid inputs.
    """
    assert right_angle_triangle(a, b, c) == expected