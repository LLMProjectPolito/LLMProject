
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
    '''
    if a <= 0 or b <= 0 or c <= 0:
        return False
    sides = sorted([a, b, c])
    # Using pytest.approx to handle floating point precision within the logic
    return pytest.approx(sides[0]**2 + sides[1]**2) == sides[2]**2

class TestRightAngleTriangle:
    """A superior, consolidated test suite for the right_angle_triangle function."""

    @pytest.mark.parametrize("a, b, c", [
        (3, 4, 5),
        (5, 12, 13),
        (8, 15, 17),
        (7, 24, 25),
        (20, 21, 29),
        (9, 40, 41),
    ])
    def test_standard_pythagorean_triples(self, a, b, c):
        """Test known integer Pythagorean triples in ascending order."""
        assert right_angle_triangle(a, b, c) is True

    @pytest.mark.parametrize("a, b, c", [
        (4, 3, 5),
        (5, 3, 4),
        (13, 5, 12),
        (5, 13, 12),
        (5, 4, 3),
        (13, 12, 5),
        (17, 8, 15),
        (25, 24, 7),
        (29, 21, 20),
    ])
    def test_order_independence(self, a, b, c):
        """Test that the function works regardless of the input order (hypotenuse position)."""
        assert right_angle_triangle(a, b, c) is True

    @pytest.mark.parametrize("a, b, c", [
        (1, 2, 3),     # Degenerate (not a triangle)
        (2, 2, 2),     # Equilateral
        (5, 5, 5),     # Equilateral
        (10, 10, 11),  # Acute
        (10, 10, 15),  # Obtuse
        (1, 1, 10),    # Impossible triangle
        (2, 2, 3),     # Isosceles (not right)
        (4, 5, 6),     # Scalene (not right)
        (1.1, 1.2, 1.5), # Floating point non-right
    ])
    def test_non_right_angled_triangles(self, a, b, c):
        """Test various triangles that are valid but do not have a 90-degree angle."""
        assert right_angle_triangle(a, b, c) is False

    @pytest.mark.parametrize("a, b, c", [
        (0.3, 0.4, 0.5),
        (1.5, 2.0, 2.5),
        (1.0, 0.75, 1.25),
        (1.2, 1.6, 2.0),
    ])
    def test_floating_point_triples(self, a, b, c):
        """Test with floating point numbers (scaled triples)."""
        assert right_angle_triangle(a, b, c) is True

    @pytest.mark.parametrize("a, b, c", [
        (0, 4, 5),
        (-3, 4, 5),
        (3, -4, 5),
        (3, 4, -5),
        (0, 0, 0),
        (0, 3, 4),
    ])
    def test_invalid_side_lengths(self, a, b, c):
        """Test that zero or negative side lengths return False."""
        assert right_angle_triangle(a, b, c) is False

    def test_extreme_values(self):
        """Test with very large and very small values."""
        # Large values
        assert right_angle_triangle(3000000, 4000000, 5000000) is True
        # Very small values
        assert right_angle_triangle(0.0003, 0.0004, 0.0005) is True

    def test_precision_edge_case(self):
        """Test a case very close to a right angle to verify precision handling."""
        # 3^2 + 4^2 = 25. 
        # 5.0000000001^2 is slightly more than 25.
        assert right_angle_triangle(3, 4, 5.0000000001) is False