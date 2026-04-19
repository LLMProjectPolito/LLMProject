
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
    # To be a right triangle, the square of the longest side must equal 
    # the sum of the squares of the other two sides.
    try:
        sides = sorted([a, b, c])
        # Use math.isclose for floating point comparisons to avoid precision errors
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)
    except TypeError:
        raise TypeError("All side lengths must be numeric.")

@pytest.mark.parametrize("a, b, c, expected", [
    # Standard Pythagorean triples
    (3, 4, 5, True),
    (5, 12, 13, True),
    (8, 15, 17, True),
    (7, 24, 25, True),
    (20, 21, 29, True),
    
    # Permutations of the same triple (ensuring the hypotenuse isn't always the last arg)
    (5, 3, 4, True),
    (4, 5, 3, True),
    (13, 5, 12, True),
    (12, 13, 5, True),
    
    # Non-right triangles (Degenerate, Equilateral, Isosceles, Acute, Obtuse)
    (1, 2, 3, False),    # Degenerate
    (5, 5, 5, False),    # Equilateral
    (6, 6, 8, False),    # Isosceles
    (10, 11, 12, False), # Scalene
    (2, 2, 3, False),    # Obtuse
    (3, 3, 3, False),    # Acute
    (4, 4, 5, False),    # Obtuse
    (10, 10, 10, False),
    
    # Floating point cases (exact and irrational)
    (0.3, 0.4, 0.5, True),
    (1.5, 2.0, 2.5, True),
    (1, 1, math.sqrt(2), True),
    (math.sqrt(3), 1, 2, True),
    (0.1, 0.1, 0.2, False),
    
    # Edge cases: Small and Large numbers
    (0.003, 0.004, 0.005, True),
    (3000, 4000, 5000, True),
    (1000000, 1000000, 1414213, False), # Close to sqrt(2) but not exact
    
    # Mathematical formula edge cases (degenerate/negative)
    (0, 0, 0, True),    # 0^2 + 0^2 = 0^2
    (-3, -4, 5, True),  # (-3)^2 + (-4)^2 = 5^2
    (-3, -4, -5, True), # (-3)^2 + (-4)^2 = (-5)^2
    (0, 4, 5, False),
])
def test_right_angle_triangle_parametrized(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

def test_right_angle_triangle_precision():
    """
    Specifically test for floating point precision issues where 
    standard == might fail but math.isclose should pass.
    """
    # 1^2 + 1^2 = (sqrt(2))^2
    # Using a high-precision float representation of sqrt(2)
    assert right_angle_triangle(1, 1, 1.4142135623730951) is True

def test_right_angle_triangle_type_error():
    """Test that the function raises TypeError when non-numeric types are passed."""
    with pytest.raises(TypeError):
        right_angle_triangle("3", "4", "5")
    with pytest.raises(TypeError):
        right_angle_triangle(None, 4, 5)
    with pytest.raises(TypeError):
        right_angle_triangle([3], 4, 5)