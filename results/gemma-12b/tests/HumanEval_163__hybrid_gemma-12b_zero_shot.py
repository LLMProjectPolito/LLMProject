
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

import pytest
from your_module import generate_integers  # Replace your_module

class TestGenerateIntegers:
    """
    Test suite for the generate_integers function.
    """

    def test_basic_ascending(self):
        """Test with a and b in ascending order."""
        assert generate_integers(2, 8) == [2, 4, 6, 8]

    def test_basic_descending(self):
        """Test with a and b in descending order."""
        assert generate_integers(8, 2) == [2, 4, 6, 8]

    def test_no_even_numbers(self):
        """Test when there are no even numbers between a and b."""
        assert generate_integers(10, 14) == []

    def test_single_even_number(self):
        """Test when there is only one even number between a and b."""
        assert generate_integers(3, 5) == [4]

    def test_a_is_even(self):
        """Test when a is an even number."""
        assert generate_integers(4, 10) == [4, 6, 8, 10]

    def test_b_is_even(self):
        """Test when b is an even number."""
        assert generate_integers(2, 6) == [2, 4, 6]

    def test_a_and_b_are_even(self):
        """Test when both a and b are even numbers."""
        assert generate_integers(2, 6) == [2, 4, 6]

    def test_a_equals_b(self):
        """Test when a and b are equal."""
        assert generate_integers(4, 4) == []

    def test_a_and_b_are_equal_even(self):
        """Test when a and b are equal and even."""
        assert generate_integers(4, 4) == [4]

    def test_a_and_b_are_equal_odd(self):
        """Test when a and b are equal and odd."""
        assert generate_integers(5, 5) == []

    def test_large_range(self):
        """Test with a larger range of numbers."""
        assert generate_integers(1, 20) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    def test_negative_input_raises_error(self):
        """Test that negative input raises a ValueError."""
        with pytest.raises(ValueError):
            generate_integers(-2, 8)
        with pytest.raises(ValueError):
            generate_integers(2, -8)
        with pytest.raises(ValueError):
            generate_integers(-2, -8)

    def test_zero_input_raises_error(self):
        """Test that zero input raises a ValueError."""
        with pytest.raises(ValueError):
            generate_integers(0, 8)
        with pytest.raises(ValueError):
            generate_integers(2, 0)
        with pytest.raises(ValueError):
            generate_integers(0, 0)

    def test_non_integer_input_raises_type_error(self):
        """Test that non-integer input raises a TypeError."""
        with pytest.raises(TypeError):
            generate_integers(2.5, 8)
        with pytest.raises(TypeError):
            generate_integers(2, 8.5)
        with pytest.raises(TypeError):
            generate_integers("2", 8)
        with pytest.raises(TypeError):
            generate_integers(2, "8")