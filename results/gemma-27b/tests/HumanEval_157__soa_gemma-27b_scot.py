import pytest

# STEP 1: REASONING
# The function `right_angle_triangle(a, b, c)` checks if three given side lengths can form a right-angled triangle.
# It uses the Pythagorean theorem: a^2 + b^2 = c^2, where c is the hypotenuse (longest side).
# Constraints:
#   - Input: Three positive numbers representing side lengths.
#   - Output: Boolean (True if right-angled, False otherwise).
#   - Edge cases:
#     - Invalid input (non-positive side lengths).
#     - Cases where the input sides do not form a valid triangle (triangle inequality).
#     - Cases where the hypotenuse is not correctly identified.

# STEP 2: PLAN
# Test functions:
#   - test_valid_right_triangle: Tests a known right-angled triangle (e.g., 3, 4, 5).
#   - test_not_right_triangle: Tests a triangle that is not right-angled (e.g., 1, 2, 3).
#   - test_invalid_input_zero: Tests with zero as a side length.
#   - test_invalid_input_negative: Tests with negative side lengths.
#   - test_triangle_inequality_violation: Tests cases where the triangle inequality is violated.
#   - test_hypotenuse_not_largest: Tests cases where the largest side is not the hypotenuse.
#   - test_equal_sides_right_triangle: Tests an isosceles right triangle (e.g., 1, 1, sqrt(2)).
#   - test_large_numbers: Tests with large numbers to check for potential overflow issues.
#   - test_float_numbers: Tests with float numbers.

# STEP 3: CODE
def test_valid_right_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True

def test_not_right_triangle():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(7, 8, 9) == False

def test_invalid_input_zero():
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 4, 0) == False

def test_invalid_input_negative():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False

def test_triangle_inequality_violation():
    assert right_angle_triangle(1, 2, 5) == False
    assert right_angle_triangle(5, 1, 2) == False
    assert right_angle_triangle(2, 5, 1) == False

def test_hypotenuse_not_largest():
    assert right_angle_triangle(5, 4, 3) == True  # Correct order
    assert right_angle_triangle(4, 5, 3) == True  # Correct order
    assert right_angle_triangle(4, 3, 5) == True  # Correct order

def test_equal_sides_right_triangle():
    import math
    assert right_angle_triangle(1, 1, math.sqrt(2)) == True
    assert right_angle_triangle(math.sqrt(2), 1, 1) == True

def test_large_numbers():
    assert right_angle_triangle(1000, 1000, 1414) == False #approx sqrt(2) * 1000
    assert right_angle_triangle(65, 72, 97) == True

def test_float_numbers():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(1.5, 2.0, 2.5) == True
    assert right_angle_triangle(1.0, 2.0, 3.0) == False