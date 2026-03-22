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

STEP 1: REASONING - The function `right_angle_triangle` checks if three given side lengths form a right-angled triangle using the Pythagorean theorem.  It sorts the sides to ensure the longest side is always in the last position.  Edge cases include zero or negative side lengths, and cases where the triangle inequality is not satisfied (i.e., the sum of any two sides is less than the third side).  The function should return `True` only if the Pythagorean theorem holds and the triangle inequality is satisfied.

STEP 2: PLAN -
1.  `test_valid_right_triangle()`: Tests a standard valid right-angled triangle (3, 4, 5).
2.  `test_invalid_right_triangle()`: Tests a triangle that is not a right-angled triangle (1, 2, 3).
3.  `test_zero_side()`: Tests a case where one of the sides is zero.
4.  `test_negative_side()`: Tests a case where one of the sides is negative.
5.  `test_triangle_inequality()`: Tests a case where the triangle inequality is not satisfied (e.g., 1, 2, 5).
6.  `test_equal_sides()`: Tests a case where all sides are equal (e.g., 5, 5, 5). This should return False.
7.  `test_large_numbers()`: Tests with large numbers to check for potential overflow issues.

STEP 3: CODE -