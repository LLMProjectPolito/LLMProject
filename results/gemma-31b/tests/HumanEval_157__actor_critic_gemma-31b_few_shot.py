
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

def test_right_angle_basic():
    """Test standard Pythagorean triples."""
    assert right_angle_triangle(3, 4, 5) is True
    assert right_angle_triangle(5, 12, 13) is True
    assert right_angle_triangle(8, 15, 17) is True

def test_right_angle_permutations():
    """Test that the order of arguments does not matter (hypotenuse can be any position)."""
    assert right_angle_triangle(5, 3, 4) is True  # Hypotenuse first
    assert right_angle_triangle(3, 5, 4) is True  # Hypotenuse second
    assert right_angle_triangle(4, 3, 5) is True  # Hypotenuse third

def test_right_angle_false():
    """Test triangles that are not right-angled, including impossible triangles."""
    assert right_angle_triangle(1, 2, 3) is False   # Degenerate/Linear
    assert right_angle_triangle(2, 2, 2) is False   # Equilateral
    assert right_angle_triangle(10, 11, 12) is False # Acute/Obtuse
    # Triangle Inequality: Sides cannot form any triangle
    assert right_angle_triangle(1, 1, 10) is False 

def test_right_angle_floats():
    """Test with floating point numbers and irrational values to ensure precision handling."""
    # Standard float precision
    assert right_angle_triangle(0.3, 0.4, 0.5) is True
    
    # Irrational numbers: 1^2 + 1^2 = (sqrt(2))^2
    # This ensures the implementation uses math.isclose() rather than strict ==
    assert right_angle_triangle(1, 1, math.sqrt(2)) is True
    assert right_angle_triangle(1.0, 1.0, 2.0) is False

def test_right_angle_invalid_sides():
    """Test edge cases with zero, negative, and mixed invalid side lengths."""
    assert right_angle_triangle(0, 0, 0) is False
    assert right_angle_triangle(-3, -4, -5) is False
    assert right_angle_triangle(3, 4, -5) is False
    # Mixed invalid: one side is zero, others are positive
    assert right_angle_triangle(0, 4, 5) is False

def test_right_angle_type_safety():
    """Test that non-numeric inputs raise a TypeError."""
    with pytest.raises(TypeError):
        right_angle_triangle("3", 4, 5)
    with pytest.raises(TypeError):
        right_angle_triangle(None, 4, 5)
    with pytest.raises(TypeError):
        right_angle_triangle([3], 4, 5)