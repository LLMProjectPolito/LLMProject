
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

    # Permutations (Hypotenuse not necessarily the last argument)
    (4, 3, 5, True),
    (5, 3, 4, True),
    (13, 5, 12, True),
    (12, 13, 5, True),
    (29, 20, 21, True),
    (41, 9, 40, True),

    # Floating point Pythagorean triples
    (1.5, 2.0, 2.5, True),
    (0.3, 0.4, 0.5, True),
    (1.2, 1.6, 2.0, True),
    (1.0, 1.0, 2.0**0.5, True),

    # Large values
    (3000, 4000, 5000, True),
    (30000, 40000, 50000, True),
    (600, 800, 1000, True),

    # Non-right-angled triangles (Valid triangles)
    (1, 1, 1, False),
    (2, 3, 4, False),
    (10, 10, 10, False),
    (5, 5, 8, False),
    (2, 2, 2, False),
    (3, 4, 6, False),
    (5, 5, 5, False),
    (10, 10, 15, False),
    (3, 4, 4, False),
    (1, 1, 1.4, False),
    (1.1, 1.1, 1.5556349186, False),

    # Degenerate triangles and invalid side lengths
    (1, 2, 3, False),   # a + b = c (not a triangle)
    (1, 1, 10, False),  # a + b < c (not a triangle)
    (0, 0, 0, False),   # Zero length
    (3, 4, 0, False),   # Zero length
    (0, 5, 5, False),   # Zero length
    (-3, 4, 5, False),  # Negative length
    (3, -4, 5, False),  # Negative length
    (3, 4, -5, False),  # Negative length
    (0, 4, 5, False),   # Zero length
])
def test_right_angle_triangle(a, b, c, expected):
    """
    Tests the right_angle_triangle function with various combinations of
    valid triples, permutations, non-right triangles, and edge cases.
    """
    assert right_angle_triangle(a, b, c) == expected