
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
import pytest

def test_right_angle_triangle_small_boundaries():
    # Testing with very small floating point values
    assert right_angle_triangle(0.3, 0.4, 0.5) is True
    assert right_angle_triangle(0.003, 0.004, 0.005) is True

def test_right_angle_triangle_large_boundaries():
    # Testing with very large values to check for overflow or precision issues
    assert right_angle_triangle(3000000, 4000000, 5000000) is True
    assert right_angle_triangle(3e10, 4e10, 5e10) is True

def test_right_angle_triangle_precision_boundary():
    # Testing values that are almost, but not quite, a right triangle
    assert right_angle_triangle(3, 4, 5.0000000001) is False
    assert right_angle_triangle(3, 4, 4.9999999999) is False

# Focus: Type Scenarios
import pytest

def test_right_angle_triangle_float_types():
    # Testing with float values instead of integers
    assert right_angle_triangle(3.0, 4.0, 5.0) is True
    assert right_angle_triangle(1.5, 2.0, 2.5) is True
    assert right_angle_triangle(1.1, 2.2, 3.3) is False

def test_right_angle_triangle_invalid_types():
    # Testing with non-numeric types to ensure TypeError is raised
    with pytest.raises(TypeError):
        right_angle_triangle("3", "4", "5")
    with pytest.raises(TypeError):
        right_angle_triangle(None, 4, 5)
    with pytest.raises(TypeError):
        right_angle_triangle([3], [4], [5])

# Focus: Logic Branches
import pytest

def test_right_angle_triangle_true_cases():
    # Tests all possible hypotenuse positions (a^2+b^2=c^2, a^2+c^2=b^2, b^2+c^2=a^2)
    assert right_angle_triangle(3, 4, 5) is True
    assert right_angle_triangle(3, 5, 4) is True
    assert right_angle_triangle(5, 3, 4) is True

def test_right_angle_triangle_false_cases():
    # Tests cases that do not satisfy the Pythagorean theorem
    assert right_angle_triangle(1, 2, 3) is False
    assert right_angle_triangle(5, 5, 5) is False
    assert right_angle_triangle(2, 3, 4) is False