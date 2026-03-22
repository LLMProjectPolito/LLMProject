import pytest
from your_module import right_angle_triangle  # Replace your_module

class TestRightAngleTriangle:
    """
    Test suite for the right_angle_triangle function.
    """

    def test_valid_right_triangle(self):
        """Test cases for valid right-angled triangles."""
        assert right_angle_triangle(3, 4, 5) == True
        assert right_angle_triangle(5, 12, 13) == True
        assert right_angle_triangle(8, 15, 17) == True
        assert right_angle_triangle(7, 24, 25) == True
        assert right_angle_triangle(20, 21, 29) == True
        assert right_angle_triangle(6, 8, 10) == True  # Scaled version of 3,4,5

    def test_invalid_right_triangle(self):
        """Test cases for triangles that are not right-angled."""
        assert right_angle_triangle(1, 2, 3) == False
        assert right_angle_triangle(2, 3, 4) == False
        assert right_angle_triangle(4, 5, 6) == False
        assert right_angle_triangle(1, 1, 1) == False  # Equilateral triangle
        assert right_angle_triangle(5, 5, 5) == False  # Equilateral triangle
        assert right_angle_triangle(10, 11, 12) == False

    def test_edge_cases(self):
        """Test cases for edge conditions and boundary values."""
        assert right_angle_triangle(0, 0, 0) == False  # All sides zero
        assert right_angle_triangle(1, 1, 2) == False  # Degenerate triangle
        assert right_angle_triangle(1, 2, 1) == False  # Different order
        assert right_angle_triangle(2, 1, 1) == False  # Different order
        assert right_angle_triangle(1, 1, 1.41421356237) == True #approx sqrt(2)

    def test_large_numbers(self):
        """Test cases with large numbers to check for potential overflow issues."""
        assert right_angle_triangle(1000, 1000, 1414.21356237) == True
        assert right_angle_triangle(10000, 10000, 14142.1356237) == True
        assert right_angle_triangle(100000, 100000, 141421.356237) == True
        assert right_angle_triangle(1000, 1000, 1414.21356) == False #approximate
        assert right_angle_triangle(1000, 1000, 1414) == False
        assert right_angle_triangle(3000, 4000, 5000) == True

    def test_float_inputs(self):
        """Test cases with floating-point numbers."""
        assert right_angle_triangle(3.0, 4.0, 5.0) == True
        assert right_angle_triangle(1.5, 2.0, 2.5) == True
        assert right_angle_triangle(1.0, 1.0, 1.5) == False
        assert right_angle_triangle(1.0, 1.0, 1.41421356) == True #approximate
        assert right_angle_triangle(1.0, 2.0, 2.5) == False

    def test_negative_inputs(self):
        """Test cases with negative inputs (should ideally raise an error or return False)."""
        with pytest.raises(TypeError):
            right_angle_triangle(-3, 4, 5)
        with pytest.raises(TypeError):
            right_angle_triangle(3, -4, 5)
        with pytest.raises(TypeError):
            right_angle_triangle(3, 4, -5)
        assert right_angle_triangle(-3, -4, -5) == False

    def test_mixed_inputs(self):
        """Test cases with mixed integer and float inputs."""
        assert right_angle_triangle(3, 4.0, 5) == True
        assert right_angle_triangle(3.0, 4, 5) == True
        assert right_angle_triangle(3, 4, 5.0) == True
        assert right_angle_triangle(3.0, 4.0, 5.0) == True
        assert right_angle_triangle(3, 4.5, 5) == False