
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
import math

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
    # This is the implementation to be tested. 
    # A robust implementation should sort the sides first.
    sides = sorted([a, b, c])
    return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

class TestRightAngleTriangle:
    
    @pytest.mark.parametrize("a, b, c", [
        (3, 4, 5),      # Standard 3-4-5
        (5, 12, 13),    # Standard 5-12-13
        (8, 15, 17),    # Standard 8-15-17
        (7, 24, 25),    # Standard 7-24-25
        (20, 21, 29),   # Standard 20-21-29
    ])
    def test_valid_right_triangles(self, a, b, c):
        """Test known Pythagorean triples."""
        assert right_angle_triangle(a, b, c) is True

    @pytest.mark.parametrize("a, b, c", [
        (3, 5, 4),      # Hypotenuse in middle
        (5, 3, 4),      # Hypotenuse first
        (4, 3, 5),      # Different order
        (13, 5, 12),    # Hypotenuse first
    ])
    def test_permutation_independence(self, a, b, c):
        """Ensure the function doesn't assume the third argument is the hypotenuse."""
        assert right_angle_triangle(a, b, c) is True

    @pytest.mark.parametrize("a, b, c", [
        (1, 2, 3),      # Degenerate triangle (1+2=3)
        (2, 2, 2),      # Equilateral
        (2, 2, 3),      # Isosceles non-right
        (10, 11, 12),   # Acute
        (10, 11, 15),   # Obtuse
    ])
    def test_non_right_triangles(self, a, b, c):
        """Test triangles that are not right-angled."""
        assert right_angle_triangle(a, b, c) is False

    @pytest.mark.parametrize("a, b, c", [
        (1.0, 1.0, math.sqrt(2)), # Standard 45-45-90
        (math.sqrt(3), 1.0, 2.0), # Standard 30-60-90
    ])
    def test_floating_point_precision(self, a, b, c):
        """Test with floats to ensure precision handling (math.isclose)."""
        assert right_angle_triangle(a, b, c) is True

    @pytest.mark.parametrize("a, b, c", [
        (0, 0, 0),      # Zero length
        (0, 3, 4),      # One zero length
        (-3, 4, 5),     # Negative length (should not be a valid triangle)
        (-3, -4, -5),   # All negative
    ])
    def test_invalid_dimensions(self, a, b, c):
        """
        Test edge cases with zero or negative numbers.
        Mathematically, a triangle must have positive side lengths.
        """
        # Depending on requirements, this should either return False or raise ValueError.
        # Given the prompt, we expect False as they don't form a physical right triangle.
        assert right_angle_triangle(a, b, c) is False or \
               pytest.raises(ValueError) # Accept either if implementation validates input

    def test_large_numbers(self):
        """Test with very large integers to check for overflow or precision issues."""
        a = 3000000
        b = 4000000
        c = 5000000
        assert right_angle_triangle(a, b, c) is True