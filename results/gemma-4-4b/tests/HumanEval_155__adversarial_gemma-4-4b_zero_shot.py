
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    num_str = str(abs(num))  # Handle negative numbers
    for digit in num_str:
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

class TestEvenOddCount:

    def test_positive_number(self):
        assert even_odd_count(123) == (1, 2)

    def test_negative_number(self):
        assert even_odd_count(-12) == (1, 1)

    def test_zero(self):
        assert even_odd_count(0) == (1, 0)

    def test_single_digit_even(self):
        assert even_odd_count(2) == (1, 0)

    def test_single_digit_odd(self):
        assert even_odd_count(3) == (0, 1)

    def test_all_even(self):
        assert even_odd_count(2468) == (4, 0)

    def test_all_odd(self):
        assert even_odd_count(13579) == (0, 5)

    def test_mixed_digits(self):
        assert even_odd_count(1234567890) == (5, 5)

    def test_large_number(self):
        assert even_odd_count(12345678901234567890) == (10, 10)

    def test_negative_large_number(self):
        assert even_odd_count(-12345678901234567890) == (10, 10)

    def test_number_with_leading_zero(self):
        assert even_odd_count(0123) == (1, 2)

    def test_number_with_mixed_leading_and_trailing_zeros(self):
        assert even_odd_count(102030) == (3, 2)

    def test_empty_string_input(self):
        with pytest.raises(TypeError):
            even_odd_count("") #Should raise TypeError

    def test_non_integer_input(self):
        with pytest.raises(TypeError):
            even_odd_count(12.34) #Should raise TypeError

    def test_none_input(self):
        with pytest.raises(TypeError):
            even_odd_count(None) #Should raise TypeError