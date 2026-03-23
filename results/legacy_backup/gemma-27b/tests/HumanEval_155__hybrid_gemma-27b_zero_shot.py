import pytest

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num_str = str(abs(num))
    even_count = 0
    odd_count = 0
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
        assert even_odd_count(12345) == (2, 3)

    def test_negative_number(self):
        assert even_odd_count(-12) == (1, 1)
        assert even_odd_count(-12345) == (2, 3)

    def test_all_even(self):
        assert even_odd_count(2468) == (4, 0)

    def test_all_odd(self):
        assert even_odd_count(1357) == (0, 4)
        assert even_odd_count(13579) == (0, 5)

    def test_single_even(self):
        assert even_odd_count(2) == (1, 0)

    def test_single_odd(self):
        assert even_odd_count(1) == (0, 1)

    def test_zero(self):
        assert even_odd_count(0) == (1, 0)

    def test_mixed_positive(self):
        assert even_odd_count(1234567890) == (5, 5)

    def test_mixed_negative(self):
        assert even_odd_count(-9876543210) == (5, 5)

    def test_large_number(self):
        assert even_odd_count(12345678901234567890) == (10, 10)

    def test_number_with_leading_zeros_as_string(self):
        assert even_odd_count(0022) == (2, 0)

    def test_number_with_trailing_zeros(self):
        assert even_odd_count(12300) == (2, 1)

    def test_edge_case_max_int(self):
        assert even_odd_count(2147483647) == (4, 6)
        assert even_odd_count(2147483647) == (4, 5) #from suite 2

    def test_edge_case_min_int(self):
        assert even_odd_count(-2147483648) == (1, 7)

    def test_repeated_digits(self):
        assert even_odd_count(22222) == (5, 0)

    def test_repeated_odd_digits(self):
        assert even_odd_count(11111) == (0, 5)

    def test_negative_zero(self):
        assert even_odd_count(-0) == (1, 0)

    def test_number_with_repeated_digits(self):
        assert even_odd_count(2222) == (4, 0)
        assert even_odd_count(1111) == (0, 4)

    def test_number_with_only_one_digit_zero(self):
        assert even_odd_count(0) == (1, 0)

    def test_number_with_only_one_digit_one(self):
        assert even_odd_count(1) == (0, 1)

    def test_number_with_only_one_digit_nine(self):
        assert even_odd_count(9) == (0, 1)