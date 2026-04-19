
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
    (3, 3, 3, False),  # Equilateral
    (2, 2, 3, False),  # Isosceles obtuse
    (3, 4, 6, False),  # Obtuse
    (4, 5, 6, False),  # Acute
    
    # Floating point values
    (1.0, 1.0, 2**0.5, True), # 1^2 + 1^2 = (sqrt 2)^2
    (0.3, 0.4, 0.5, True),
    
    # Edge cases: Zero and Negative values (should not be valid triangles)
    (0, 0, 0, False),
    (-3, -4, -5, False),
    (0, 4, 5, False),
])
def test_right_angle_triangle(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

def test_large_numbers():
    # Testing with larger Pythagorean triple
    assert right_angle_triangle(300, 400, 500) == True
    assert right_angle_triangle(1000, 2400, 2600) == True

def test_precision_near_miss():
    # A triangle that is very close to right-angled but not quite
    # 3^2 + 4^2 = 25; 5.000001^2 = 25.00001...
    assert right_angle_triangle(3, 4, 5.000001) == False