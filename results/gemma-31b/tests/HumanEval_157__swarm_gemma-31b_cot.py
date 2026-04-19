
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

@pytest.mark.parametrize("a, b, c", [
    (2**0.5, 1, 1),  # Irrational hypotenuse, not last argument
    (5, 3, 4),       # Integer hypotenuse, not last argument
    (13, 12, 5),     # Integer hypotenuse, not last argument
])
def test_right_angle_triangle_hypotenuse_position(a, b, c):
    """
    Tests if the function correctly identifies a right triangle regardless of 
    the order of side lengths and whether the values are integers or floats.
    """
    assert right_angle_triangle(a, b, c) is True