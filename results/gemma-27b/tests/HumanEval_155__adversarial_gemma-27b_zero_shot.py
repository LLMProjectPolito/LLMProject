
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
    for digit in str(abs(num)):
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

    def test_all_even_digits(self):
        assert even_odd_count(2468) == (4, 0)

    def test_all_odd_digits(self):
        assert even_odd_count(1357) == (0, 4)

    def test_single_even_digit(self):
        assert even_odd_count(2) == (1, 0)

    def test_single_odd_digit(self):
        assert even_odd_count(1) == (0, 1)

    def test_zero(self):
        assert even_odd_count(0) == (1, 0)

    def test_large_number(self):
        assert even_odd_count(1234567890) == (5, 5)

    def test_mixed_positive_and_negative(self):
        assert even_odd_count(-1234567890) == (5, 5)

    def test_number_with_leading_zeros(self):
        assert even_odd_count(0022) == (2, 0)

    def test_number_with_repeated_digits(self):
        assert even_odd_count(2222) == (4, 0)
        assert even_odd_count(1111) == (0, 4)

    def test_edge_case_max_int(self):
        assert even_odd_count(2147483647) == (4, 6)

    def test_edge_case_min_int(self):
        assert even_odd_count(-2147483648) == (1, 9)