import pytest
import math


# Focus: Boundary Values
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
### Boundary values are crucial because small changes in side lengths can drastically change the result.
### We need to test cases with very small and very large side lengths, as well as cases where the triangle inequality is not satisfied.

### STEP 2: PLAN - List test functions names and scenarios.
### test_right_angle_triangle_valid
### test_right_angle_triangle_invalid
### test_right_angle_triangle_zero
### test_right_angle_triangle_large

### STEP 3: CODE - Write the high-quality pytest suite.
def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True

def test_right_angle_triangle_invalid():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(2, 2, 3) == False

def test_right_angle_triangle_zero():
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(1, 0, 1) == False
    assert right_angle_triangle(0, 1, 1) == False

def test_right_angle_triangle_large():
    assert right_angle_triangle(1000, 1000, 1414) == True
    assert right_angle_triangle(1000, 1000, 1415) == False

# Focus: Type Scenarios
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
### The test functions should cover various scenarios, focusing solely on the 'Type Scenarios' dimension,
### ensuring the function behaves correctly with different input types and combinations.

### STEP 2: PLAN - List test functions names and scenarios.
### Test functions:
### - test_valid_right_triangle: Tests a valid right-angled triangle (3, 4, 5).
### - test_invalid_right_triangle: Tests a triangle that is not a right-angled triangle (1, 2, 3).
### - test_equal_sides: Tests a triangle with equal sides (4, 4, 4).

### STEP 3: CODE - Write the high-quality pytest suite.
###
### TEST FUNCTIONS
###
def test_valid_right_triangle():
    assert right_angle_triangle(3, 4, 5) == True

def test_invalid_right_triangle():
    assert right_angle_triangle(1, 2, 3) == False

def test_equal_sides():
    assert right_angle_triangle(4, 4, 4) == False

# Focus: Logic Branches
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

def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_invalid_1():
    assert right_angle_triangle(1, 2, 3) == False

def test_right_angle_triangle_invalid_2():
    assert right_angle_triangle(5, 12, 13) == True

def test_right_angle_triangle_invalid_3():
    assert right_angle_triangle(7, 24, 25) == True