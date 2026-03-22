# STEP 1: REASONING
# The function `right_angle_triangle(a, b, c)` checks if three given side lengths form a right-angled triangle.
# The core logic relies on the Pythagorean theorem: a^2 + b^2 = c^2, where c is the longest side.
# We need to test various scenarios, including:
# 1. Valid right-angled triangles (e.g., 3, 4, 5)
# 2. Invalid triangles (e.g., 1, 2, 3)
# 3. Cases where the sides are not in ascending order (e.g., 5, 3, 4)
# 4. Edge cases with zero or negative side lengths (should return False)
# 5. Cases with equal sides (isosceles right triangle)
# 6. Cases with floating-point numbers

# STEP 2: PLAN
# Test functions:
# - test_valid_right_triangle: Checks a standard 3-4-5 triangle.
# - test_invalid_triangle: Checks a triangle that doesn't satisfy the Pythagorean theorem.
# - test_sides_not_sorted: Checks a right triangle where sides are not in ascending order.
# - test_zero_side: Checks a triangle with a side length of zero.
# - test_negative_side: Checks a triangle with a negative side length.
# - test_isosceles_right_triangle: Checks an isosceles right triangle.
# - test_floating_point_numbers: Checks with floating-point side lengths.
# - test_large_numbers: Checks with large integer side lengths.

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

class TestRightAngleTriangle:
    def test_valid_right_triangle(self):
        assert right_angle_triangle(3, 4, 5) == True

    def test_invalid_triangle(self):
        assert right_angle_triangle(1, 2, 3) == False

    def test_sides_not_sorted(self):
        assert right_angle_triangle(5, 3, 4) == True

    def test_zero_side(self):
        assert right_angle_triangle(0, 4, 5) == False

    def test_negative_side(self):
        assert right_angle_triangle(-3, 4, 5) == False

    def test_isosceles_right_triangle(self):
        assert right_angle_triangle(1, 1, 2**0.5) == True

    def test_floating_point_numbers(self):
        assert right_angle_triangle(3.0, 4.0, 5.0) == True

    def test_large_numbers(self):
        assert right_angle_triangle(100, 100, 141.42135623730951) == False #approximate sqrt(20000)