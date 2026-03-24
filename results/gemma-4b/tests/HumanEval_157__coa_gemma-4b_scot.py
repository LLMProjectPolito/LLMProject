
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

def test_right_angle_triangle_valid_right_triangle():
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_valid_right_triangle_2():
    assert right_angle_triangle(5, 12, 13) == True

def test_right_angle_triangle_invalid_right_triangle():
    assert right_angle_triangle(1, 2, 3) == False

# Focus: Type Scenarios
import pytest

def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_invalid_1():
    assert right_angle_triangle(1, 2, 3) == False

def test_right_angle_triangle_invalid_2():
    assert right_angle_triangle(5, 12, 13) == True

# Focus: Logic Branches
import pytest

def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True

def test_right_angle_triangle_invalid():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(1, 1, 1) == False