
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



def test_even_odd_count_positive():
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(2468) == (4, 0)
    assert even_odd_count(13579) == (0, 5)
    assert even_odd_count(1234567890) == (4, 6)
    assert even_odd_count(1) == (0, 1)
    assert even_odd_count(2) == (1, 0)
    assert even_odd_count(0) == (0, 0)
    assert even_odd_count(10) == (1, 1)
    assert even_odd_count(11) == (1, 2)
    assert even_odd_count(21) == (1, 1)

def test_even_odd_count_negative():
    assert even_odd_count(-123) == (1, 2)
    assert even_odd_count(-2468) == (4, 0)
    assert even_odd_count(-13579) == (0, 5)
    assert even_odd_count(-1234567890) == (4, 6)
    assert even_odd_count(-1) == (0, 1)
    assert even_odd_count(-2) == (1, 0)
    assert even_odd_count(-0) == (0, 0)
    assert even_odd_count(-10) == (1, 1)
    assert even_odd_count(-11) == (1, 2)
    assert even_odd_count(-21) == (1, 1)

def test_even_odd_count_mixed():
    assert even_odd_count(-1234) == (2, 2)
    assert even_odd_count(12345) == (2, 3)
    assert even_odd_count(-123) == (1, 2)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(-123456) == (2, 4)

def test_even_odd_count_large_number():
    assert even_odd_count(12345678901234567890) == (6, 6)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (0, 0)
    assert even_odd_count(-0) == (0, 0)
    assert even_odd_count(10) == (1, 1)
    assert even_odd_count(-10) == (1, 1)

def test_empty_number():
    assert even_odd_count(0) == (0, 0)

def test_positive_number_even_digits():
    assert even_odd_count(2468) == (4, 0)

def test_positive_number_odd_digits():
    assert even_odd_count(13579) == (0, 9)

def test_positive_number_mixed_digits():
    assert even_odd_count(12345) == (2, 3)

def test_negative_number_even_digits():
    assert even_odd_count(-2468) == (4, 0)

def test_negative_number_odd_digits():
    assert even_odd_count(-13579) == (0, 9)

def test_negative_number_mixed_digits():
    assert even_odd_count(-12345) == (2, 3)

def test_single_digit_even():
    assert even_odd_count(2) == (1, 0)

def test_single_digit_odd():
    assert even_odd_count(1) == (0, 1)

def test_single_digit_mixed():
    assert even_odd_count(5) == (0, 1)

def test_large_number_even_digits():
    assert even_odd_count(246810121416) == (8, 2)

def test_large_number_odd_digits():
    assert even_odd_count(135791113151719) == (0, 20)

def test_large_number_mixed_digits():
    assert even_odd_count(1234567890) == (4, 5)

def test_number_with_zero():
    assert even_odd_count(10203) == (2, 2)

def test_number_with_leading_zero():
    assert even_odd_count(00123) == (2, 1)

def test_number_with_leading_zero_and_negative():
    assert even_odd_count(-0123) == (1, 2)

def test_number_with_only_zeros():
    assert even_odd_count(0000) == (4, 0)