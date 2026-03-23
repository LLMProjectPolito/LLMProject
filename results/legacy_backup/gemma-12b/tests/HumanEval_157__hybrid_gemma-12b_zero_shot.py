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
        assert right_angle_triangle(6, 8, 10) == True  # Multiple of 3,4,5

    def test_invalid_triangle(self):
        """Tests with triangles that are not right-angled."""
        assert right_angle_triangle(1, 2, 3) == False
        assert right_angle_triangle(2, 3, 4) == False
        assert right_angle_triangle(4, 5, 6) == False
        assert right_angle_triangle(1, 1, 1) == False  # Equilateral
        assert right_angle_triangle(5, 5, 5) == False  # Equilateral
        assert right_angle_triangle(10, 11, 12) == False

    def test_edge_cases(self):
        """Tests with edge cases and boundary conditions."""
        assert right_angle_triangle(0, 0, 0) == False  # All sides zero
        assert right_angle_triangle(1, 1, 1.41421356) == True #Approximate sqrt(2)
        assert right_angle_triangle(1, 0, 1) == False #One side zero
        assert right_angle_triangle(1, 1, 0) == False #One side zero
        assert right_angle_triangle(0, 1, 1) == False #One side zero

    def test_large_numbers(self):
        """Tests with large numbers to check for potential overflow issues."""
        assert right_angle_triangle(1000, 1000, 1414.21356) == True
        assert right_angle_triangle(10000, 10000, 14142.1356) == True
        assert right_angle_triangle(100000, 100000, 141421.356) == True

    def test_floating_point_numbers(self):
        """Tests with floating-point numbers to check for precision issues."""
        assert right_angle_triangle(3.0, 4.0, 5.0) == True
        assert right_angle_triangle(3.1, 4.1, 5.1) == False
        assert right_angle_triangle(0.3, 0.4, 0.5) == True
        assert right_angle_triangle(0.5, 0.5, 0.70710678) == True #Approximate sqrt(2)/2

    def test_input_types(self):
        """Tests with different input types to ensure robustness."""
        with pytest.raises(TypeError):
            right_angle_triangle("3", 4, 5)  # String input
        with pytest.raises(TypeError):
            right_angle_triangle(3, "4", 5)  # String input
        with pytest.raises(TypeError):
            right_angle_triangle(3, 4, "5")  # String input
        with pytest.raises(TypeError):
            right_angle_triangle(3, 4.5, "5") #Mixed types
        with pytest.raises(TypeError):
            right_angle_triangle(3, 4, 5.5) #Mixed types

    def test_negative_numbers(self):
        """Tests with negative numbers, which are invalid for side lengths."""
        assert right_angle_triangle(-3, 4, 5) == False
        assert right_angle_triangle(3, -4, 5) == False
        assert right_angle_triangle(3, 4, -5) == False
        assert right_angle_triangle(-3, -4, -5) == False

    def test_zero_and_positive(self):
        """Tests with a combination of zero and positive numbers."""
        assert right_angle_triangle(0, 5, 5) == False
        assert right_angle_triangle(5, 0, 5) == False
        assert right_angle_triangle(5, 5, 0) == False