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
### We need to test the edge case where all three sides are zero. This will result in a division by zero error if we don't handle it.
### STEP 2: PLAN - List test functions names and scenarios.
### test_zero_sides: Test the case where all three sides are zero.
### STEP 3: CODE - Write the high-quality pytest suite.
###
def test_zero_sides():
    assert right_angle_triangle(0, 0, 0) == True

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
def test_zero_side():
    assert right_angle_triangle(0, 4, 5) == False