
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


# Focus: Boundary Values
def test_right_angle_triangle_zero_and_minimal_boundaries():
    # Testing the lower boundary of side lengths (zero and smallest integer triple)
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_large_boundaries():
    # Testing large values to ensure no overflow or precision issues
    assert right_angle_triangle(3000000, 4000000, 5000000) == True
    assert right_angle_triangle(3000000, 4000000, 5000001) == False

def test_right_angle_triangle_near_miss_boundaries():
    # Testing values that are very close to satisfying the Pythagorean theorem
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(5, 12, 12.9) == False
    assert right_angle_triangle(5, 12, 13.1) == False

# Focus: Input Permutations
import pytest

def test_right_angle_triangle_permutations():
    # Hypotenuse in different positions
    assert right_angle_triangle(3, 4, 5) is True
    assert right_angle_triangle(3, 5, 4) is True
    assert right_angle_triangle(5, 3, 4) is True

def test_right_angle_triangle_non_right_permutations():
    # Non-right triangle in different positions
    assert right_angle_triangle(1, 2, 3) is False
    assert right_angle_triangle(3, 1, 2) is False
    assert right_angle_triangle(2, 3, 1) is False

# Focus: Type Scenarios
import pytest

def test_right_angle_triangle_floats():
    assert right_angle_triangle(3.0, 4.0, 5.0) is True
    assert right_angle_triangle(1.5, 2.0, 2.5) is True
    assert right_angle_triangle(1.1, 2.2, 3.3) is False

def test_right_angle_triangle_invalid_types():
    with pytest.raises(TypeError):
        right_angle_triangle("3", "4", "5")
    with pytest.raises(TypeError):
        right_angle_triangle(None, 4, 5)
    with pytest.raises(TypeError):
        right_angle_triangle([3], [4], [5])