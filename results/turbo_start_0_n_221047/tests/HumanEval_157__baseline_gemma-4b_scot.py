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

### STEP 1: REASONING
# The function `right_angle_triangle` checks if three given side lengths form a right-angled triangle.
# The core logic is based on the Pythagorean theorem: a² + b² = c², where c is the hypotenuse.
# We need to test various scenarios, including valid right triangles, invalid right triangles, and edge cases (e.g., zero or negative side lengths, though the problem description doesn't explicitly state constraints on these).
# We should test with common right triangles (3, 4, 5) and some non-right triangles.

### STEP 2: PLAN
# Test cases:
# 1. Valid right triangle (3, 4, 5)
# 2. Another valid right triangle (5, 12, 13)
# 3. Invalid right triangle (1, 2, 3)
# 4. Invalid right triangle (1, 1, 1)
# 5. Edge case: zero side length
# 6. Edge case: negative side length (should not happen, but good to consider)
# 7. Another valid right triangle (6, 8, 10)

### STEP 3: CODE
def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(6, 8, 10) == True

def test_right_angle_triangle_invalid():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(1, 1, 1) == False

def test_right_angle_triangle_edge_cases():
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 4, 0) == False

def test_right_angle_triangle_negative_sides():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False