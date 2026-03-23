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

def test_right_angle_triangle_boundary_zero():
    """Test with zero values for sides."""
    assert right_angle_triangle(0, 0, 0) == True
    assert right_angle_triangle(0, 3, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 5, 0) == False

def test_right_angle_triangle_boundary_one():
    """Test with one as a side length."""
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(1, 1, 2) == False
    assert right_angle_triangle(1, 2, 2) == False
    assert right_angle_triangle(1, 0, 1) == False

def test_right_angle_triangle_boundary_large_values():
    """Test with large values to check for potential overflow issues."""
    assert right_angle_triangle(1000, 1000, 1414) == False
    assert right_angle_triangle(1000, 1000, 1414.2135623730951) == False
    assert right_angle_triangle(3000, 4000, 5000) == True

# Focus: Equivalence Partitioning
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

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function determines if a triangle is right-angled based on side lengths.
# Equivalence partitioning focuses on valid and invalid triangle side combinations.
# Valid combinations satisfy the Pythagorean theorem. Invalid combinations do not.
# We need to consider cases where the sides *can* form a triangle (triangle inequality)
# and cases where they cannot.

# STEP 2: PLAN - List test functions names and scenarios.
# 1. test_right_triangle_valid: Tests valid right-angled triangles (e.g., 3, 4, 5).
# 2. test_right_triangle_invalid_not_right: Tests invalid triangles that don't satisfy the Pythagorean theorem.
# 3. test_right_triangle_invalid_triangle_inequality: Tests invalid triangles that violate the triangle inequality.

# STEP 3: CODE - Write the high-quality pytest suite.

def test_right_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True

def test_right_triangle_invalid_not_right():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(6, 8, 10) == False # Not a right triangle, but valid triangle
    assert right_angle_triangle(1, 1, 1) == False

def test_right_triangle_invalid_triangle_inequality():
    assert right_angle_triangle(1, 2, 5) == False
    assert right_angle_triangle(1, 1, 3) == False
    assert right_angle_triangle(5, 1, 2) == False

# Focus: Invalid Input Handling
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

def test_invalid_input_negative_sides():
    """Test with negative side lengths."""
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False
    assert right_angle_triangle(-3, -4, -5) == False

def test_invalid_input_zero_sides():
    """Test with zero side lengths."""
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 4, 0) == False
    assert right_angle_triangle(0, 0, 0) == False

def test_invalid_input_non_numeric():
    """Test with non-numeric input."""
    with pytest.raises(TypeError):
        right_angle_triangle("3", 4, 5)
    with pytest.raises(TypeError):
        right_angle_triangle(3, "4", 5)
    with pytest.raises(TypeError):
        right_angle_triangle(3, 4, "5")