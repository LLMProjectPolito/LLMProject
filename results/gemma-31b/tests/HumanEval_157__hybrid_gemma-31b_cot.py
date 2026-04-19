
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
    # Standard Pythagorean triples (Integers)
    (3, 4, 5, True),
    (5, 12, 13, True),
    (8, 15, 17, True),
    (7, 24, 25, True),
    (20, 21, 29, True),
    (9, 40, 41, True),
    
    # Permutations of sides to ensure the hypotenuse can be any parameter
    (3, 5, 4, True),
    (4, 3, 5, True),
    (4, 5, 3, True),
    (5, 3, 4, True),
    (5, 4, 3, True),
    (13, 5, 12, True),
    (12, 13, 5, True),
    
    # Non-right triangles (Acute)
    (3, 3, 3, False), # Equilateral
    (5, 5, 5, False),
    (6, 6, 7, False),
    (5, 6, 7, False),
    (2, 2, 2, False),
    
    # Non-right triangles (Obtuse)
    (2, 2, 3, False),
    (3, 4, 6, False),
    (10, 10, 15, False),
    
    # Degenerate triangles (sum of two sides equals the third - not a triangle)
    (1, 2, 3, False),
    (5, 10, 15, False),
    
    # Floating point values
    (1.0, 1.0, math.sqrt(2), True),
    (1.5, 2.0, 2.5, True),
    (0.3, 0.4, 0.5, True),
    (0.5, 1.2, 1.3, True),
    (1.1, 1.1, 1.5, False),
    
    # Edge cases: Zero or Negative lengths (cannot form a physical triangle)
    (0, 0, 0, False),
    (0, 4, 5, False),
    (0, 5, 5, False),
    (-3, 4, 5, False),
    (-3, -4, -5, False),
    (3, -4, 5, False),
    
    # Large numbers
    (300, 400, 500, True),
    (1000, 2400, 2600, True),
    (3000, 4000, 5000, True),
    (1000000, 1000000, 1414213, False), # Close but not exact
    (1000000, 1000000, 2000000, False),
])
def test_right_angle_triangle_comprehensive(a, b, c, expected):
    """
    Test a comprehensive set of cases including triples, permutations,
    non-right triangles, floating point precision, and invalid side lengths.
    """
    assert right_angle_triangle(a, b, c) == expected

def test_right_angle_triangle_type_consistency():
    """
    Ensure the function handles mixed types (int and float) correctly.
    """
    assert right_angle_triangle(3, 4.0, 5) is True
    assert right_angle_triangle(3.0, 4, 5.0) is True

def test_right_angle_triangle_precision_extremes():
    """
    Test with very small values and near-misses to check for precision handling.
    """
    # Very small positive values: 0.003^2 + 0.004^2 = 0.005^2
    assert right_angle_triangle(0.003, 0.004, 0.005) is True
    
    # Near-misses: values very close to a right triangle but not exactly
    assert right_angle_triangle(3, 4, 5.000001) is False
    assert right_angle_triangle(3, 4, 4.999999) is False