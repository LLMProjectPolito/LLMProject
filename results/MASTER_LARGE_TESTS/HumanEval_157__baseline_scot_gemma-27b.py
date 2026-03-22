# STEP 1: REASONING
# The function `right_angle_triangle(a, b, c)` determines if three side lengths form a right-angled triangle.
# We need to test various scenarios:
# 1. Valid right-angled triangles (e.g., 3, 4, 5; 5, 12, 13).
# 2. Invalid right-angled triangles (e.g., 1, 2, 3; 1, 1, 1).
# 3. Cases where the input sides are not positive numbers.
# 4. Cases where the sides violate the triangle inequality theorem (sum of two sides must be greater than the third side).
# 5. Cases with zero values.
# 6. Cases with floating-point numbers.

# STEP 2: PLAN
# 1. test_valid_right_triangle: Tests valid right-angled triangles.
# 2. test_invalid_right_triangle: Tests invalid right-angled triangles.
# 3. test_negative_sides: Tests cases with negative side lengths.
# 4. test_zero_sides: Tests cases with zero side lengths.
# 5. test_triangle_inequality: Tests cases violating the triangle inequality theorem.
# 6. test_floating_point_sides: Tests cases with floating-point side lengths.
# 7. test_sides_in_different_order: Tests valid right triangles with sides in different order.

# STEP 3: CODE
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

def test_valid_right_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True

def test_invalid_right_triangle():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(2, 3, 4) == False

def test_negative_sides():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False
    assert right_angle_triangle(-3, -4, -5) == False

def test_zero_sides():
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 4, 0) == False
    assert right_angle_triangle(0, 0, 0) == False

def test_triangle_inequality():
    assert right_angle_triangle(1, 2, 5) == False
    assert right_angle_triangle(1, 5, 2) == False
    assert right_angle_triangle(5, 1, 2) == False

def test_floating_point_sides():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(5.0, 12.0, 13.0) == True
    assert right_angle_triangle(3.1, 4.1, 5.1) == False

def test_sides_in_different_order():
    assert right_angle_triangle(4, 3, 5) == True
    assert right_angle_triangle(5, 3, 4) == True
    assert right_angle_triangle(12, 5, 13) == True