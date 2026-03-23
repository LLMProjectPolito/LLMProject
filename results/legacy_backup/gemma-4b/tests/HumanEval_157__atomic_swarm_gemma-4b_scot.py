import pytest
import math

def test_basic():
    assert right_angle_triangle(3, 4, 5) == True

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
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `right_angle_triangle` checks if three given side lengths form a right-angled triangle.
### The core logic is based on the Pythagorean theorem: a² + b² = c², where c is the hypotenuse.
### We need to sort the sides to easily identify the potential hypotenuse.
### An edge case is when all sides are zero. In this case, it should return False.
### Another edge case is when one side is zero. In this case, it should return False.

### STEP 2: PLAN - List test functions names and scenarios.
### test_zero_sides: Test with all sides equal to zero.
### test_one_zero_side: Test with one side equal to zero.
### test_valid_right_triangle: Test with a valid right-angled triangle.
### test_invalid_right_triangle: Test with a triangle that is not a right-angled triangle.

### STEP 3: CODE - Write the high-quality pytest suite.
def test_zero_sides():
    assert right_angle_triangle(0, 0, 0) == False

def test_one_zero_side():
    assert right_angle_triangle(0, 4, 3) == False
    assert right_angle_triangle(4, 0, 3) == False
    assert right_angle_triangle(4, 3, 0) == False

def test_valid_right_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True

def test_invalid_right_triangle():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(2, 3, 4) == False

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
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2

### SCoT Steps:
### STEP 1: REASONING - The function `right_angle_triangle` checks if three sides form a right-angled triangle. We need to test cases where the inputs are invalid (e.g., negative values, zero values, or values that violate the triangle inequality).  Specifically, we'll test a case where a side length is zero.
### STEP 2: PLAN - Test function name: `test_zero_side`. Scenario: Input `a = 0`.
### STEP 3: CODE -