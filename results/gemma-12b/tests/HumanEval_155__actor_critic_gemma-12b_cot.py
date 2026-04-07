
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
        even_odd_count(-12) -> (1, 1)
        even_odd_count(123) -> (1, 2)
    """
    num = abs(num)
    even_count = 0
    odd_count = 0
    for digit in str(num):
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

def test_positive_number():
    """Tests a positive number with mixed digits."""
    assert even_odd_count(12345) == (2, 3)

def test_negative_number():
    """Tests a negative number with mixed digits."""
    assert even_odd_count(-12345) == (2, 3)

def test_zero():
    """Tests the input zero."""
    assert even_odd_count(0) == (1, 0)

def test_single_even_digit():
    """Tests a single even digit."""
    assert even_odd_count(2) == (1, 0)

def test_single_odd_digit():
    """Tests a single odd digit."""
    assert even_odd_count(1) == (0, 1)

def test_all_even_digits():
    """Tests a number consisting only of even digits."""
    assert even_odd_count(2468) == (4, 0)

def test_all_odd_digits():
    """Tests a number consisting only of odd digits."""
    assert even_odd_count(13579) == (0, 5)

def test_mixed_digits():
    """Tests a number with a mix of even and odd digits."""
    assert even_odd_count(1234567890) == (5, 5)

def test_large_number():
    """Tests a large number with mixed digits."""
    assert even_odd_count(12345678901234567890) == (5, 15)

def test_number_with_zeros():
    """Tests a number containing zeros."""
    assert even_odd_count(1020304050) == (5, 5)

def test_negative_number_with_zeros():
    """Tests a negative number containing zeros."""
    assert even_odd_count(-1020304050) == (5, 5)

def test_simple_number():
    """Tests a simple number."""
    assert even_odd_count(123) == (1, 2)

def test_max_integer():
    """Tests a number close to the maximum integer size."""
    assert even_odd_count(2147483647) == (3, 9)