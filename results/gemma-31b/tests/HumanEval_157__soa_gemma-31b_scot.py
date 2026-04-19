
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
    (1, 2, 3, False),  # Degenerate/Linear
    (2, 2, 2, False),  # Equilateral
    (2, 3, 4, False),  # Obtuse
    (3, 3, 4, False),  # Acute
    (10, 10, 10, False),
    
    # Large numbers
    (300, 400, 500, True),
    (3000, 4000, 5000, True),
    
    # Floating point cases (if the function supports them)
    (1.0, 1.0, 2**0.5, True), # Note: This depends on float precision in the implementation
    (0.3, 0.4, 0.5, True),
])
def test_right_angle_triangle(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

def test_zero_and_negative_sides():
    # Geometrically, sides must be positive. 
    # These should return False as they cannot form a valid right triangle.
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(-3, -4, -5) == False
    assert right_angle_triangle(3, 4, -5) == False