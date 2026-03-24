
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

STEP 1: REASONING -
The function `right_angle_triangle` checks if three given side lengths form a right-angled triangle. It sorts the sides and then applies the Pythagorean theorem (a^2 + b^2 = c^2) to determine if the triangle is right-angled.  We need to test various scenarios including valid right triangles, invalid right triangles, and edge cases like zero or negative side lengths (although the problem description doesn't explicitly state this, it's good practice to consider).

STEP 2: PLAN -
1.  `test_valid_right_triangle()`: Tests a standard valid right triangle (3, 4, 5).
2.  `test_invalid_right_triangle()`: Tests a triangle that is not a right triangle (1, 2, 3).
3.  `test_another_valid_right_triangle()`: Tests another valid right triangle (5, 12, 13).
4.  `test_zero_side()`: Tests a case where one of the sides is zero.
5.  `test_negative_side()`: Tests a case where one of the sides is negative (should likely raise an error, but the function doesn't handle it, so we'll test the behavior).
6.  `test_equal_sides()`: Tests a case where all sides are equal.

STEP 3: CODE -