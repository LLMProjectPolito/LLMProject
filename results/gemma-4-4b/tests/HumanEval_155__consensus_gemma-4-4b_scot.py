
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
    num_str = str(abs(num))
    for digit in num_str:
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

class TestEvenOddCount:

    def test_positive_number(self):
        assert even_odd_count(12345) == (2, 3)
        assert even_odd_count(2468) == (4, 0)
        assert even_odd_count(13579) == (0, 5)
        assert even_odd_count(123) == (1, 2)

    def test_negative_number(self):
        assert even_odd_count(-123) == (1, 2)
        assert even_odd_count(-2468) == (4, 0)
        assert even_odd_count(-1357) == (0, 3)
        assert even_odd_count(-123) == (1, 2)

    def test_zero(self):
        assert even_odd_count(0) == (1, 0)

    def test_single_digit_even(self):
        assert even_odd_count(2) == (1, 0)
        assert even_odd_count(4) == (1, 0)
        assert even_odd_count(6) == (1, 0)
        assert even_odd_count(8) == (1, 0)

    def test_single_digit_odd(self):
        assert even_odd_count(1) == (0, 1)
        assert even_odd_count(3) == (0, 1)
        assert even_odd_count(5) == (0, 1)
        assert even_odd_count(7) == (0, 1)
        assert even_odd_count(9) == (0, 1)

    def test_mixed_digits(self):
        assert even_odd_count(12) == (1, 1)
        assert even_odd_count(21) == (1, 1)
        assert even_odd_count(10) == (1, 1)
        assert even_odd_count(01) == (1, 0)
        assert even_odd_count(102) == (2, 1)
        assert even_odd_count(201) == (1, 2)

    def test_large_number(self):
        assert even_odd_count(1234567890) == (5, 5)
        assert even_odd_count(24680) == (5, 0)
        assert even_odd_count(135790) == (0, 5)

    def test_negative_with_zero(self):
      assert even_odd_count(-102) == (2, 1)
      assert even_odd_count(-201) == (1, 2)
      assert even_odd_count(-120) == (2, 1)
      assert even_odd_count(-100) == (2, 0)