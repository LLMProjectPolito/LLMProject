
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

def test_right_angle_triangle_boundary_min_triple():
    # Smallest integer Pythagorean triple
    assert right_angle_triangle(3, 4, 5) is True
    assert right_angle_triangle(5, 3, 4) is True
    assert right_angle_triangle(4, 5, 3) is True

def test_right_angle_triangle_boundary_isosceles():
    # Boundary case: Isosceles right triangle (1^2 + 1^2 = sqrt(2)^2)
    assert right_angle_triangle(1, 1, 2**0.5) is True

def test_right_angle_triangle_boundary_near_miss():
    # Boundary case: Values extremely close to a right triangle but not exactly
    assert right_angle_triangle(3, 4, 5.0000000001) is False
    assert right_angle_triangle(3, 4, 4.9999999999) is False

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

# Focus: Logic Branches
def test_right_angle_triangle_hypotenuse_last():
    assert right_angle_triangle(3, 4, 5) is True

def test_right_angle_triangle_hypotenuse_first():
    assert right_angle_triangle(5, 3, 4) is True

def test_right_angle_triangle_not_right():
    assert right_angle_triangle(1, 2, 3) is False