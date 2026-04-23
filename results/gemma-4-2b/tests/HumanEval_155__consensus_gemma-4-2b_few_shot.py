
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
    for digit in str(num):
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
    assert even_odd_count(0) == (0, 1)

def test_even_odd_count_negative():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-246) == (3, 0)
    assert even_odd_count(-135) == (0, 3)
    assert even_odd_count(-1234567890) == (4, 6)
    assert even_odd_count(-1) == (0, 1)
    assert even_odd_count(-2) == (1, 0)
    assert even_odd_count(-0) == (0, 1)

def test_even_odd_count_mixed():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(-1234) == (2, 2)
    assert even_odd_count(12345) == (2, 3)
    assert even_odd_count(-123456) == (3, 3)

def test_even_odd_count_large_number():
    assert even_odd_count(12345678901234567890) == (8, 8)
    assert even_odd_count(2222222222) == (10, 0)
    assert even_odd_count(1111111111) == (0, 10)
    assert even_odd_count(1234567890123456789) == (9, 9)