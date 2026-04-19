
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

# The function is provided in the environment; we are testing it.
# from solution import right_angle_triangle 

class TestRightAngleTriangle:
    
    @pytest.mark.parametrize("a, b, c", [
        (3, 4, 5),    # Standard 3-4-5
        (5, 12, 13),  # Standard 5-12-13
        (8, 15, 17),  # Standard 8-15-17
        (7, 24, 25),  # Standard 7-24-25
        (20, 21, 29), # Standard 20-21-29
    ])
    def test_valid_right_triangles(self, a, b, c):
        """Test standard Pythagorean triples."""
        assert right_angle_triangle(a, b, c) is True

    @pytest.mark.parametrize("a, b, c", [
        (5, 3, 4),    # Hypotenuse first
        (4, 5, 3),    # Hypotenuse second
        (13, 5, 12),  # Hypotenuse first
        (12, 13, 5),  # Hypotenuse second
    ])
    def test_permutations(self, a, b, c):
        """Ensure the function identifies the hypotenuse regardless of order."""
        assert right_angle_triangle(a, b, c) is True

    @pytest.mark.parametrize("a, b, c", [
        (1, 1, 1),    # Equilateral
        (2, 2, 3),    # Isosceles obtuse
        (3, 3, 4),    # Isosceles acute
        (1, 2, 3),    # Degenerate (collinear)
        (10, 11, 12), # Scalene non-right
    ])
    def test_non_right_triangles(self, a, b, c):
        """Test triangles that are not right-angled."""
        assert right_angle_triangle(a, b, c) is False

    @pytest.mark.parametrize("a, b, c", [
        (0, 0, 0),    # All zeros
        (0, 3, 4),    # One zero
        (-3, 4, 5),   # Negative side
        (-3, -4, -5), # All negative
    ])
    def test_invalid_lengths(self, a, b, c):
        """Test cases with zero or negative lengths which cannot form a triangle."""
        assert right_angle_triangle(a, b, c) is False

    @pytest.mark.parametrize("a, b, c", [
        (1.0, 1.0, math.sqrt(2)), # 45-45-90 triangle
        (0.3, 0.4, 0.5),          # Scaled down 3-4-5
    ])
    def test_floating_point_triangles(self, a, b, c):
        """Test with floating point numbers."""
        # Note: Depending on implementation, floating point precision 
        # might require math.isclose. We test for standard float behavior.
        assert right_angle_triangle(a, b, c) is True

    def test_large_values(self):
        """Test with very large integers to ensure no overflow/precision loss."""
        # 3000000^2 + 4000000^2 = 5000000^2
        assert right_angle_triangle(3000000, 4000000, 5000000) is True
        # Slightly off large triple
        assert right_angle_triangle(3000000, 4000000, 5000001) is False