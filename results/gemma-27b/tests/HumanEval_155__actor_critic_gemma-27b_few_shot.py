
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(12) ==> (1, 1)
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

def test_even_odd_count_positive():
    """Test with a positive number."""
    assert even_odd_count(123) == (1, 2)

def test_even_odd_count_all_even():
    """Test with a number containing only even digits."""
    assert even_odd_count(2468) == (4, 0)

def test_even_odd_count_all_odd():
    """Test with a number containing only odd digits."""
    assert even_odd_count(1357) == (0, 4)

def test_even_odd_count_zero():
    """Test with zero as input."""
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_mixed():
    """Test with a number containing a mix of even and odd digits."""
    assert even_odd_count(123456) == (3, 3)

def test_even_odd_count_single_even_digit():
    """Test with a single even digit."""
    assert even_odd_count(2) == (1, 0)

def test_even_odd_count_single_odd_digit():
    """Test with a single odd digit."""
    assert even_odd_count(1) == (0, 1)

def test_even_odd_count_large_number():
    """Test with a large number."""
    assert even_odd_count(1234567890) == (5, 5)

def test_even_odd_count_repeated_digits():
    """Test with a number containing repeated digits."""
    assert even_odd_count(1122) == (2, 2)

def test_even_odd_count_very_large_number():
    """Test with a very large number to check for potential integer overflow issues."""
    assert even_odd_count(9999999999) == (0, 10)

def test_even_odd_count_negative():
    """Test with a negative number."""
    assert even_odd_count(-123) == (1, 2)

def test_even_odd_count_max_int():
    """Test with the maximum possible integer value."""
    assert even_odd_count(2147483647) == (4, 6)