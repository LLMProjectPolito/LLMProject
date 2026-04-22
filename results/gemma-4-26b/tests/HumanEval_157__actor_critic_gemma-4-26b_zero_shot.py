
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
    # Implementation is assumed to be provided; this is the test suite.
    pass

@pytest.mark.parametrize("a, b, c, expected", [
    # --- Standard Right-Angled Triangles (Pythagorean Triples) ---
    (3, 4, 5, True),
    (5, 12, 13, True),
    (8, 15, 17, True),
    (7, 24, 25, True),
    (20, 21, 29, True),

    # --- Shuffled Order (Testing if the function identifies the hypotenuse correctly) ---
    (5, 3, 4, True),
    (4, 5, 3, True),
    (13, 12, 5, True),
    (12, 5, 13, True),

    # --- Floating Point Right-Angled Triangles ---
    # NOTE: The following case mandates a tolerance-based implementation (e.g., math.isclose)
    # because 0.3**2 + 0.4**2 != 0.5**2 due to IEEE 754 floating-point representation.
    (0.3, 0.4, 0.5, True),
    (1.5, 2.0, 2.5, True),

    # --- Non-Right-Angled Triangles ---
    (2, 2, 2, False),    # Equilateral
    (4, 5, 6, False),    # Scalene but not right
    (10, 10, 15, False), # Isosceles but not right

    # --- Degenerate and Invalid Triangles ---
    (1, 2, 3, False),    # Degenerate (1 + 2 = 3, not a triangle)
    (1, 1, 10, False),   # Not a triangle (sum of two sides < third)
    (0, 0, 0, False),    # Zero lengths
    (3, 4, 0, False),    # One zero length
    (-3, 4, 5, False),   # Negative side length
    (-3, -4, -5, False), # All negative side lengths

    # --- Large Scale Testing (Testing potential overflow/precision) ---
    (3000000, 4000000, 5000000, True),
    (3e150, 4e150, 5e150, True),
    # Testing overflow: squaring 1e200 results in 'inf'. 
    # A naive implementation might do 'inf + inf == inf', incorrectly returning True.
    (1e200, 1e200, 1e200, False),

    # --- Micro-Scale Testing (Testing epsilon/tolerance logic) ---
    (3e-10, 4e-10, 5e-10, True),

    # --- Non-finite Float Values ---
    (float('nan'), 4, 5, False),
    (float('inf'), 4, 5, False),
    (4, 5, float('nan'), False),
])
def test_right_angle_triangle(a, b, c, expected):
    """
    Tests various scenarios for the right_angle_triangle function, 
    including valid triples, shuffled inputs, floats, invalid geometry, 
    large scales, micro scales, non-finite values, and overflow handling.
    """
    from __main__ import right_angle_triangle
    assert right_angle_triangle(a, b, c) == expected

def test_precision_edge_case():
    """
    Specifically tests floating point precision for values very close to a right angle,
    ensuring symmetric tolerance logic (both slightly larger and slightly smaller).
    """
    from __main__ import right_angle_triangle
    # A triangle that is almost right-angled but not quite
    # 3^2 + 4^2 = 25. 5.0000001^2 is slightly more than 25.
    assert right_angle_triangle(3, 4, 5.0000001) == False
    # 5.0000001^2 is slightly less than 25.
    assert right_angle_triangle(3, 4, 4.9999999) == False

def test_input_type_validation():
    """
    Tests that the function handles non-numeric inputs gracefully.
    Note: This assumes the implementation is expected to raise a TypeError for bad data.
    """
    from __main__ import right_angle_triangle
    with pytest.raises(TypeError):
        right_angle_triangle(None, 4, 5)
    with pytest.raises(TypeError):
        right_angle_triangle("3", 4, 5)
    with pytest.raises(TypeError):
        right_angle_triangle([3, 4, 5], 4, 5)
    with pytest.raises(TypeError):
        right_angle_triangle(complex(1, 2), 4, 5)
    with pytest.raises(TypeError):
        right_angle_triangle({'a': 1}, 4, 5)