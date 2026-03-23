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
    if num == 0:
        return (1, 0)
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num //= 10
    return (even_count, odd_count)

def test_even_odd_count_negative():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-123) == (1, 2)
    assert even_odd_count(-21) == (1, 1)
    assert even_odd_count(-1) == (0, 1)
    assert even_odd_count(-2) == (1, 1)

def test_even_odd_count_positive():
    assert even_odd_count(12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(21) == (1, 1)
    assert even_odd_count(1) == (0, 1)
    assert even_odd_count(2) == (1, 1)
    assert even_odd_count(1234567890) == (5, 5)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_single_digit_even():
    assert even_odd_count(2) == (1, 0)

def test_even_odd_count_single_digit_odd():
    assert even_odd_count(1) == (0, 1)

def test_even_odd_count_large_number():
    assert even_odd_count(12345678901234567890) == (10, 10)

def test_even_odd_count_all_even():
    assert even_odd_count(2468) == (4, 0)

def test_even_odd_count_all_odd():
    assert even_odd_count(13579) == (0, 5)