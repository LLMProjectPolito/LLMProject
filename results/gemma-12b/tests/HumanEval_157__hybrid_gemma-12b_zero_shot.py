
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
from your_module import right_angle_triangle  # Replace your_module

class TestRightAngleTriangle:
    """
    Comprehensive pytest suite for the right_angle_triangle function.
    """

    def test_valid_right_triangle(self):
        """Tests with valid right-angled triangles."""
        assert right_angle_triangle(3, 4, 5) == True
        assert right_angle_triangle(5, 12, 13) == True
        assert right_angle_triangle(8, 15, 17) == True
        assert right_angle_triangle(7, 24, 25) == True
        assert right_angle_triangle(20, 21, 29) == True
        assert right_angle_triangle(6, 8, 10) == True  # Scaled version of 3,4,5

    def test_invalid_right_triangle(self):
        """Tests with triangles that are not right-angled."""
        assert right_angle_triangle(1, 2, 3) == False
        assert right_angle_triangle(2, 3, 4) == False
        assert right_angle_triangle(4, 5, 6) == False
        assert right_angle_triangle(1, 1, 1) == False  # Equilateral triangle
        assert right_angle_triangle(5, 5, 5) == False  # Equilateral triangle
        assert right_angle_triangle(10, 11, 12) == False

    def test_edge_cases(self):
        """Tests with edge cases and boundary conditions."""
        assert right_angle_triangle(0, 0, 0) == False  # All sides zero
        assert right_angle_triangle(1, 1, 2) == False  # Degenerate triangle
        assert right_angle_triangle(1, 2, 1) == False  # Different order
        assert right_angle_triangle(2, 1, 1) == False  # Different order
        assert right_angle_triangle(1, 1, 1.41421356237) == True #Approximate sqrt(2)
        assert right_angle_triangle(1, 1, 1.41421356238) == False #Slightly off sqrt(2)

    def test_large_numbers(self):
        """Tests with large numbers to check for potential overflow issues."""
        assert right_angle_triangle(1000, 1000, 1414.21356237) == True
        assert right_angle_triangle(1000, 1001, 1002) == False

    def test_float_inputs(self):
        """Tests with float inputs."""
        assert right_angle_triangle(3.0, 4.0, 5.0) == True
        assert right_angle_triangle(1.5, 2.0, 2.5) == True
        assert right_angle_triangle(1.0, 2.0, 3.0) == False

    def test_negative_inputs(self):
        """Tests with negative inputs (should ideally raise an error or return False)."""
        with pytest.raises(TypeError):
            right_angle_triangle(-3, 4, 5)
        with pytest.raises(TypeError):
            right_angle_triangle(3, -4, 5)
        with pytest.raises(TypeError):
            right_angle_triangle(3, 4, -5)

    def test_mixed_inputs(self):
        """Tests with mixed integer and float inputs."""
        assert right_angle_triangle(3, 4.0, 5) == True
        assert right_angle_triangle(3.0, 4, 5) == True
        assert right_angle_triangle(3, 4, 5.0) == True
        assert right_angle_triangle(3.0, 4.0, 5.0) == True
        assert right_angle_triangle(3, 4.1, 5) == False