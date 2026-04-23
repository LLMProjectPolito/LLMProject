
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

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

import pytest

def test_positive_even_odd_count():
    assert even_odd_count(123) == (1, 2)

def test_all_even_even_odd_count():
    assert even_odd_count(2468) == (4, 0)

def test_all_odd_even_odd_count():
    assert even_odd_count(1357) == (0, 4)

def test_zero_even_odd_count():
    assert even_odd_count(0) == (1, 0)

def test_mixed_even_odd_count():
    assert even_odd_count(123456) == (3, 3)

def test_single_even_even_odd_count():
    assert even_odd_count(2) == (1, 0)

def test_single_odd_even_odd_count():
    assert even_odd_count(1) == (0, 1)

def test_large_number_even_odd_count():
    assert even_odd_count(1234567890) == (5, 5)

def test_negative_even_odd_count():
    assert even_odd_count(-123) == (1, 2)

def test_very_large_number_even_odd_count():
    assert even_odd_count(99999999999999999999) == (0, 20)

def test_max_int_even_odd_count():
    assert even_odd_count(2147483647) == (4, 6)

def test_min_int_even_odd_count():
    assert even_odd_count(-2147483648) == (1, 9)