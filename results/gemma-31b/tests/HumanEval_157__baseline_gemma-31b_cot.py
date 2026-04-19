
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
    (12, 35, 37, True),
    
    # Permutations of sides (hypotenuse in different positions)
    (3, 5, 4, True),
    (5, 3, 4, True),
    (4, 3, 5, True),
    (4, 5, 3, True),
    (5, 4, 3, True),
    (13, 5, 12, True),
    (12, 13, 5, True),
    
    # Non-right triangles
    (1, 2, 3, False),  # Degenerate triangle (1+2=3), not right-angled
    (2, 2, 2, False),  # Equilateral
    (2, 2, 3, False),  # Isosceles
    (10, 11, 12, False),
    (5, 5, 5, False),
    (6, 7, 8, False),
    
    # Edge cases: Large numbers
    (300, 400, 500, True),
    (3000, 4000, 5000, True),
    
    # Edge cases: Invalid triangle dimensions (should be False)
    (0, 0, 0, False),
    (-3, 4, 5, False),
    (0, 4, 5, False),
    
    # Floating point cases (if supported)
    (1.0, 1.0, 2.0, False),
    (1.0, 1.0, 1.4142135623730951, True), # sqrt(2)
])
def test_right_angle_triangle(a, b, c, expected):
    """
    Tests the right_angle_triangle function with various inputs including
    valid right triangles, non-right triangles, permutations, and edge cases.
    """
    assert right_angle_triangle(a, b, c) == expected

def test_right_angle_triangle_types():
    """
    Verify that the function handles different numeric types correctly.
    """
    # Integer inputs
    assert right_angle_triangle(3, 4, 5) is True
    # Float inputs
    assert right_angle_triangle(3.0, 4.0, 5.0) is True
    # Mixed inputs
    assert right_angle_triangle(3, 4.0, 5) is True