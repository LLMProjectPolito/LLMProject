
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


def test_even_odd_count_positive_number():
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(12345) == (2, 3)
    assert even_odd_count(11111) == (0, 5)
    assert even_odd_count(22222) == (5, 0)
    assert even_odd_count(1) == (0, 1)
    assert even_odd_count(2) == (1, 0)
    assert even_odd_count(3) == (0, 1)
    assert even_odd_count(4) == (1, 0)
    assert even_odd_count(5) == (0, 1)
    assert even_odd_count(6) == (1, 0)
    assert even_odd_count(7) == (0, 1)
    assert even_odd_count(8) == (1, 0)
    assert even_odd_count(9) == (0, 1)

def test_even_odd_count_negative_number():
    assert even_odd_count(-123) == (1, 2)
    assert even_odd_count(-12345) == (2, 3)
    assert even_odd_count(-11111) == (0, 5)
    assert even_odd_count(-12222) == (5, 0)
    assert even_odd_count(-1) == (0, 1)
    assert even_odd_count(-2) == (1, 0)
    assert even_odd_count(-3) == (0, 1)
    assert even_odd_count(-4) == (1, 0)
    assert even_odd_count(-5) == (0, 1)
    assert even_odd_count(-6) == (1, 0)
    assert even_odd_count(-7) == (0, 1)
    assert even_odd_count(-8) == (1, 0)
    assert even_odd_count(-9) == (0, 1)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (0, 0)
    assert even_odd_count(-0) == (0, 0)
    assert even_odd_count(000) == (0, 0)
    assert even_odd_count(-000) == (0, 0)

def test_even_odd_count_large_number():
    assert even_odd_count(1234567890) == (4, 5)
    assert even_odd_count(12345678901) == (5, 4)
    assert even_odd_count(2222222222) == (10, 0)
    assert even_odd_count(1111111111) == (0, 10)

def test_even_odd_count_mixed_digits():
    assert even_odd_count(102345) == (2, 3)
    assert even_odd_count(24680) == (5, 0)
    assert even_odd_count(13579) == (0, 5)

def test_even_odd_count_all_even_digits():
    assert even_odd_count(22222) == (5, 0)

def test_even_odd_count_all_odd_digits():
    assert even_odd_count(11111) == (0, 5)

def test_even_odd_count_leading_zeros():
    assert even_odd_count(00123) == (2, 3)