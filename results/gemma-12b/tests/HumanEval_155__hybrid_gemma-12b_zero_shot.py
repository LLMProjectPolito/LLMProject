
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest
from your_module import even_odd_count  # Replace your_module

class TestEvenOddCount:
    """
    Test suite for the even_odd_count function.
    """

    def test_positive_integer(self):
        """Test with a positive integer."""
        assert even_odd_count(123456) == (3, 3)
        assert even_odd_count(12345) == (2, 3)

    def test_negative_integer(self):
        """Test with a negative integer."""
        assert even_odd_count(-123456) == (3, 3)
        assert even_odd_count(-12) == (1, 1)

    def test_zero(self):
        """Test with zero."""
        assert even_odd_count(0) == (1, 0)

    def test_single_digit_even(self):
        """Test with a single-digit even number."""
        assert even_odd_count(2) == (1, 0)
        assert even_odd_count(4) == (1, 0)

    def test_single_digit_odd(self):
        """Test with a single-digit odd number."""
        assert even_odd_count(1) == (0, 1)
        assert even_odd_count(7) == (0, 1)

    def test_all_even_digits(self):
        """Test with an integer containing only even digits."""
        assert even_odd_count(2468) == (4, 0)

    def test_all_odd_digits(self):
        """Test with an integer containing only odd digits."""
        assert even_odd_count(13579) == (0, 5)

    def test_mixed_digits(self):
        """Test with an integer containing a mix of even and odd digits."""
        assert even_odd_count(1234567890) == (5, 5)

    def test_large_number(self):
        """Test with a large integer."""
        assert even_odd_count(12345678901234567890) == (5, 10)

    def test_negative_large_number(self):
        """Test with a large negative integer."""
        assert even_odd_count(-12345678901234567890) == (5, 10)

    def test_integer_with_leading_zeros(self):
        """Test with an integer that might be interpreted as having leading zeros (though the function shouldn't be affected)."""
        assert even_odd_count(10203) == (2, 2)

    def test_edge_case_one_even_and_one_odd(self):
        """Test an edge case with one even and one odd digit."""
        assert even_odd_count(10) == (1, 1)

    def test_edge_case_multiple_zeros(self):
        """Test an edge case with multiple zeros."""
        assert even_odd_count(1000) == (3, 1)

    def test_number_with_zeros(self):
        assert even_odd_count(10203) == (2, 2)

    def test_number_with_leading_zeros_treated_as_positive(self):
        assert even_odd_count(100) == (2, 1)

    def test_negative_number_with_zeros(self):
        assert even_odd_count(-10203) == (2, 2)

    def test_input_type_integer(self):
        """Test that the input is an integer."""
        with pytest.raises(TypeError):
            even_odd_count("123")

        with pytest.raises(TypeError):
            even_odd_count(12.3)

        with pytest.raises(TypeError):
            even_odd_count([1,2,3])