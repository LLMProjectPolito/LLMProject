
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

import math
import pytest

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
    # A triangle must have all side lengths greater than zero
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    # Sort sides to identify the hypotenuse (the longest side)
    sides = sorted([a, b, c])
    
    # Use the Pythagorean theorem: a^2 + b^2 = c^2
    # math.isclose is used to handle floating point precision errors
    return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

@pytest.mark.parametrize("a, b, c, expected", [
    # Standard Pythagorean triples
    (3, 4, 5, True),
    (5, 12, 13, True),
    (8, 15, 17, True),
    (7, 24, 25, True),
    (20, 21, 29, True),
    
    # Permutations of side lengths (hypotenuse in different positions)
    (5, 3, 4, True),
    (4, 5, 3, True),
    (13, 12, 5, True),
    (12, 5, 13, True),
    
    # Non-right triangles
    (1, 2, 3, False),  # Degenerate triangle
    (2, 2, 2, False),  # Equilateral
    (2, 2, 3, False),  # Obtuse
    (2, 3, 4, False),  # Obtuse
    (3, 3, 4, False),  # Acute
    (1, 1, 1, False),  # Equilateral
    
    # Edge cases: zero and negative values
    (0, 0, 0, False), 
    (-3, -4, -5, False),
    (0, 4, 5, False),
])
def test_right_angle_triangle_integers(a, b, c, expected):
    """Test right_angle_triangle with various integer inputs."""
    assert right_angle_triangle(a, b, c) == expected

def test_right_angle_triangle_floats():
    """Test right_angle_triangle with floating point numbers."""
    # 1^2 + 1^2 = (sqrt(2))^2
    assert right_angle_triangle(1.0, 1.0, 2**0.5) is True
    assert right_angle_triangle(0.3, 0.4, 0.5) is True
    assert right_angle_triangle(1.1, 2.2, 3.3) is False

def test_right_angle_triangle_large_numbers():
    """Test with larger Pythagorean triples."""
    assert right_angle_triangle(300, 400, 500) is True
    assert right_angle_triangle(1000, 2400, 2600) is True