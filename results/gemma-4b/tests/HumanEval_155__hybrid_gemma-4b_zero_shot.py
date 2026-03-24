
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
    num = abs(num)
    if num == 0:
        return (1, 0)
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num //= 10
    return (even_count, odd_count)

class TestEvenOddCount:

    def test_positive_number_with_even_and_odd_digits(self):
        assert even_odd_count(123) == (1, 2)

    def test_positive_number_with_only_even_digits(self):
        assert even_odd_count(2468) == (4, 0)

    def test_positive_number_with_only_odd_digits(self):
        assert even_odd_count(13579) == (0, 5)

    def test_negative_number_with_even_and_odd_digits(self):
        assert even_odd_count(-12) == (1, 1)

    def test_negative_number_with_only_even_digits(self):
        assert even_odd_count(-2468) == (4, 0)

    def test_negative_number_with_only_odd_digits(self):
        assert even_odd_count(-13579) == (0, 5)

    def test_zero(self):
        assert even_odd_count(0) == (1, 0)

    def test_large_number_with_mixed_digits(self):
        assert even_odd_count(1234567890) == (5, 5)

    def test_number_with_leading_zeros(self):
        assert even_odd_count(0123) == (1, 2)

    def test_number_with_negative_leading_zeros(self):
        assert even_odd_count(-0123) == (1, 2)

    def test_single_digit_even(self):
        assert even_odd_count(2) == (1, 0)

    def test_single_digit_odd(self):
        assert even_odd_count(1) == (0, 1)

    def test_number_with_only_zeros(self):
        assert even_odd_count(0000) == (4, 0)