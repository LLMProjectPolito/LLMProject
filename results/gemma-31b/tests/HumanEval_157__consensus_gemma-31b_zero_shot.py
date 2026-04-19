
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
    # Standard Pythagorean triples (True)
    (3, 4, 5, True),
    (5, 12, 13, True),
    (8, 15, 17, True),
    (7, 24, 25, True),
    (20, 21, 29, True),
    
    # Permutations of sides to ensure hypotenuse isn't assumed to be the last argument (True)
    (5, 3, 4, True),
    (4, 5, 3, True),
    (13, 5, 12, True),
    (12, 13, 5, True),
    (13, 12, 5, True),
    (12, 5, 13, True),
    
    # Not right-angled triangles (False)
    (1, 2, 3, False),
    (2, 2, 2, False),
    (10, 10, 10, False),
    (2, 3, 4, False),
    (5, 5, 8, False),
    (6, 8, 11, False),
    (5, 5, 5, False),
    (10, 10, 15, False),
    (3, 3, 3, False),
    (4, 4, 6, False),
    (10, 11, 12, False),
    (1, 1, 10, False),
    
    # Floating point values (True)
    (1.0, 1.0, 2**0.5, True),
    (1.0, 2**0.5, 1.0, True),
    (2**0.5, 1.0, 1.0, True),
    (1.5, 2.0, 2.5, True),
    (0.3, 0.4, 0.5, True),
    
    # Floating point values (False)
    (1.1, 2.2, 3.3, False),
    (3.0, 4.0, 5.0001, False),
    
    # Edge cases: Zero and Negative lengths (False)
    (0, 0, 0, False),
    (0, 4, 5, False),
    (-3, -4, -5, False),
    (-3, 4, 5, False),
    
    # Large numbers (True)
    (3000, 4000, 5000, True),
    (1000, 2400, 2600, True),
])
def test_right_angle_triangle(a, b, c, expected):
    """
    Tests the right_angle_triangle function with various valid, invalid, 
    and edge-case side lengths.
    """
    assert right_angle_triangle(a, b, c) == expected

def test_right_angle_triangle_large_numbers_false():
    """Test with larger integers that are not perfectly right-angled."""
    assert right_angle_triangle(1000000, 1000000, 1414213) == False

def test_right_angle_triangle_near_miss():
    """Testing values very close to a right triangle to ensure precision."""
    assert right_angle_triangle(3, 4, 5.0000001) == False
    assert right_angle_triangle(3, 4, 4.9999999) == False