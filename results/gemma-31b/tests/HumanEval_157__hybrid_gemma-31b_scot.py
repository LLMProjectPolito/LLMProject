
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

class TestRightAngleTriangle:
    """
    Superior test suite for the right_angle_triangle function.
    Validates geometric correctness, input permutations, floating point precision,
    and robust error handling.
    """

    @pytest.mark.parametrize("a, b, c", [
        # Standard Pythagorean Triples
        (3, 4, 5),
        (5, 12, 13),
        (8, 15, 17),
        (7, 24, 25),
        (20, 21, 29),
        # Permutations (Hypotenuse in different positions)
        (5, 3, 4),
        (4, 5, 3),
        (13, 12, 5),
        (12, 5, 13),
        (17, 8, 15),
    ])
    def test_valid_right_triangles(self, a, b, c):
        """Verify that all valid right triangles return True regardless of order."""
        assert right_angle_triangle(a, b, c) is True

    @pytest.mark.parametrize("a, b, c", [
        (3, 3, 3),    # Equilateral
        (6, 6, 7),    # Acute
        (3, 4, 6),    # Obtuse
        (2, 2, 3),    # Obtuse
        (10, 10, 10), # Equilateral
        (5, 5, 8),    # Obtuse
    ])
    def test_non_right_triangles(self, a, b, c):
        """Verify that valid triangles that are not right-angled return False."""
        assert right_angle_triangle(a, b, c) is False

    @pytest.mark.parametrize("a, b, c", [
        (1, 2, 3),    # Degenerate (flat line: 1+2=3)
        (1, 1, 10),   # Impossible (1+1 < 10)
        (0, 0, 0),    # Zero lengths
        (0, 4, 5),    # Partial zero
        (-3, -4, -5), # Negative lengths (Mathematically squares to True, Geometrically False)
        (3, -4, 5),   # Mixed signs
    ])
    def test_invalid_geometry(self, a, b, c):
        """
        Verify that degenerate, impossible, or non-positive side lengths return False.
        A triangle must have side lengths > 0.
        """
        assert right_angle_triangle(a, b, c) is False

    @pytest.mark.parametrize("a, b, c", [
        (0.3, 0.4, 0.5),           # Exact float triple
        (1.5, 2.0, 2.5),           # Exact float triple
        (1.0, 1.0, math.sqrt(2)),  # Irrational hypotenuse
        (math.sqrt(2), 1.0, 1.0),  # Irrational side
    ])
    def test_floating_point_precision(self, a, b, c):
        """
        Verify that the function handles floating point numbers and precision.
        This tests if the implementation uses something like math.isclose().
        """
        assert right_angle_triangle(a, b, c) is True

    def test_large_integers(self):
        """Test with very large numbers to ensure no precision loss or overflow."""
        # Triple: 3*10^6, 4*10^6, 5*10^6
        assert right_angle_triangle(3000000, 4000000, 5000000) is True
        # Even larger triple
        assert right_angle_triangle(300000000, 400000000, 500000000) is True

    @pytest.mark.parametrize("a, b, c", [
        ("3", "4", "5"),       # Strings
        (None, 4, 5),          # NoneType
        ([3], [4], [5]),       # Lists
        (complex(1,1), 4, 5),  # Complex numbers
    ])
    def test_type_safety(self, a, b, c):
        """Ensure that non-numeric inputs raise a TypeError."""
        with pytest.raises(TypeError):
            right_angle_triangle(a, b, c)