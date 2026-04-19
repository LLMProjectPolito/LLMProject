
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
    
    # Permutations of sides (hypotenuse in first, middle, and last positions)
    (3, 4, 5, True), # Last
    (3, 5, 4, True), # Middle
    (5, 3, 4, True), # First
    
    # Non-right triangles
    (1, 2, 3, False),  # Degenerate triangle (1+2=3), not right-angled
    (2, 2, 2, False),  # Equilateral
    (3, 4, 6, False),  # Obtuse
    (5, 6, 7, False),  # Acute
    (10, 10, 10, False),
    (1, 1, 1, False),
    
    # Edge cases: very large numbers
    (300, 400, 500, True),
    (3000, 4000, 5000, True),
    
    # Edge cases: floating point
    (0.3, 0.4, 0.5, True), # Simple decimal triple
    (1.0, 1.0, 2**0.5, True), # Irrational hypotenuse
])
def test_right_angle_triangle_valid_inputs(a, b, c, expected):
    """
    Tests the right_angle_triangle function with various valid numeric 
    side lengths, including permutations and floating point values.
    """
    assert right_angle_triangle(a, b, c) == expected

@pytest.mark.parametrize("a, b, c", [
    (0, 0, 0),       # All zeros
    (0, 4, 5),       # One zero
    (-3, -4, 5),     # Negative legs
    (3, 4, -5),      # Negative hypotenuse
    (1, 1, 10),      # Triangle inequality violation
    (float('nan'), 4, 5), # NaN value
    (float('inf'), 4, 5), # Infinity value
])
def test_right_angle_triangle_invalid_geometry(a, b, c):
    """
    Tests that non-physical side lengths, impossible triangles, or 
    special float values return False.
    """
    assert right_angle_triangle(a, b, c) is False

@pytest.mark.parametrize("a, b, c", [
    ("3", 4, 5),     # String input
    (None, 4, 5),    # None input
    ([3], 4, 5),     # List input
])
def test_right_angle_triangle_invalid_types(a, b, c):
    """
    Tests that non-numeric inputs raise a TypeError to ensure robustness.
    """
    with pytest.raises(TypeError):
        right_angle_triangle(a, b, c)