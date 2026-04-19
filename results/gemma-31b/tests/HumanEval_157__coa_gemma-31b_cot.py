
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
def test_right_angle_triangle_large_values():
    assert right_angle_triangle(30000, 40000, 50000) is True

def test_right_angle_triangle_small_values():
    assert right_angle_triangle(0.03, 0.04, 0.05) is True

def test_right_angle_triangle_near_boundary():
    assert right_angle_triangle(3, 4, 5.0000001) is False

# Focus: Type Scenarios
import pytest

def test_right_angle_triangle_float_types():
    # Testing with float values to ensure numeric type flexibility
    assert right_angle_triangle(3.0, 4.0, 5.0) is True
    assert right_angle_triangle(1.5, 2.0, 2.5) is True
    assert right_angle_triangle(1.1, 2.2, 3.3) is False

def test_right_angle_triangle_invalid_types():
    # Testing with non-numeric types to ensure appropriate error handling
    with pytest.raises(TypeError):
        right_angle_triangle("3", "4", "5")
    with pytest.raises(TypeError):
        right_angle_triangle(None, 4, 5)
    with pytest.raises(TypeError):
        right_angle_triangle([3], [4], [5])

# Focus: Logic Branches
import pytest

def test_right_angle_triangle_true_branches():
    # Test each side as the potential hypotenuse
    assert right_angle_triangle(3, 4, 5) is True  # c is hypotenuse
    assert right_angle_triangle(3, 5, 4) is True  # b is hypotenuse
    assert right_angle_triangle(5, 3, 4) is True  # a is hypotenuse

def test_right_angle_triangle_false_branch():
    # Test cases that do not satisfy the Pythagorean theorem
    assert right_angle_triangle(1, 2, 3) is False
    assert right_angle_triangle(5, 5, 5) is False