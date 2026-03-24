
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

def test_even_odd_count_negative():
    assert even_odd_count(-12) == (1, 1)

def test_even_odd_count_positive():
    assert even_odd_count(123) == (1, 2)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (0, 0)

def test_even_odd_count_negative():
    assert even_odd_count(-12) == (1, 1)

def test_even_odd_count_large_number():
    assert even_odd_count(1234567890) == (2, 3)

def test_even_odd_count_single_digit():
    assert even_odd_count(5) == (0, 1)

def test_even_odd_count_multiple_digits():
    assert even_odd_count(12345) == (2, 2)

def test_even_odd_count_positive_large():
    assert even_odd_count(1234567890) == (4, 2)