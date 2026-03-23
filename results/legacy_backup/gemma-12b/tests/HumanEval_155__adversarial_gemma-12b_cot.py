import pytest

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num = abs(num)
    even = 0
    odd = 0
    for digit in str(num):
        digit = int(digit)
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)

class TestEvenOddCount:
    def test_positive_number(self):
        assert even_odd_count(123) == (1, 2)

    def test_negative_number(self):
        assert even_odd_count(-12) == (1, 1)

    def test_zero(self):
        assert even_odd_count(0) == (1, 0)

    def test_all_even(self):
        assert even_odd_count(2468) == (4, 0)

    def test_all_odd(self):
        assert even_odd_count(13579) == (0, 5)

    def test_mixed_even_odd(self):
        assert even_odd_count(123456) == (3, 3)

    def test_single_digit_even(self):
        assert even_odd_count(2) == (1, 0)

    def test_single_digit_odd(self):
        assert even_odd_count(1) == (0, 1)

    def test_large_number(self):
        assert even_odd_count(1234567890) == (5, 5)

    def test_number_with_zeros(self):
        assert even_odd_count(10203) == (2, 2)

    def test_negative_all_even(self):
        assert even_odd_count(-2468) == (4, 0)

    def test_negative_all_odd(self):
        assert even_odd_count(-13579) == (0, 5)