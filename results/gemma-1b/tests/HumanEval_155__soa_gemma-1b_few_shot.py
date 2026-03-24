
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

def test_even_odd_count_positive():
    assert even_odd_count(-12) == (1, 1)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (0, 0)

def test_even_odd_count_one():
    assert even_odd_count(1) == (1, 1)

def test_even_odd_count_three():
    assert even_odd_count(3) == (1, 1)

def test_even_odd_count_five():
    assert even_odd_count(5) == (1, 1)

def test_even_odd_count_nine():
    assert even_odd_count(9) == (1, 1)

def test_even_odd_count_ten():
    assert even_odd_count(10) == (1, 1)

def test_even_odd_count_12345():
    assert even_odd_count(12345) == (1, 1)

def test_even_odd_count_123456():
    assert even_odd_count(123456) == (1, 1)