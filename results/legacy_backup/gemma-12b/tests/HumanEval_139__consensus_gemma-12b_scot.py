import pytest
from your_module import special_factorial  # Replace your_module

class TestSpecialFactorial:

    def test_positive_integer(self):
        """Test with a positive integer."""
        assert special_factorial(4) == 288
        assert special_factorial(1) == 1
        assert special_factorial(2) == 2
        assert special_factorial(3) == 12
        assert special_factorial(5) == 34560

    def test_large_integer(self):
        """Test with a larger positive integer."""
        assert special_factorial(6) == 864000

    def test_edge_case_one(self):
        """Test the edge case where n is 1."""
        assert special_factorial(1) == 1

    def test_zero_input(self):
        """Test with zero input. Should raise ValueError."""
        with pytest.raises(ValueError):
            special_factorial(0)

    def test_negative_input(self):
        """Test with a negative input. Should raise ValueError."""
        with pytest.raises(ValueError):
            special_factorial(-1)

    def test_float_input(self):
        """Test with a float input. Should raise TypeError."""
        with pytest.raises(TypeError):
            special_factorial(2.5)

    def test_string_input(self):
        """Test with a string input. Should raise TypeError."""
        with pytest.raises(TypeError):
            special_factorial("abc")