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

def test_even_odd_count_positive_number():
    """Test with a positive number."""
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(2468) == (4, 0)
    assert even_odd_count(13579) == (0, 5)
    assert even_odd_count(24680) == (5, 0)
    assert even_odd_count(1234567890) == (5, 5)

def test_even_odd_count_negative_number():
    """Test with a negative number."""
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-2468) == (4, 0)
    assert even_odd_count(-13579) == (0, 5)
    assert even_odd_count(-24680) == (5, 0)
    assert even_odd_count(-1234567890) == (5, 5)

def test_even_odd_count_zero():
    """Test with zero."""
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_single_digit_even():
    """Test with a single digit even number."""
    assert even_odd_count(2) == (1, 0)

def test_even_odd_count_single_digit_odd():
    """Test with a single digit odd number."""
    assert even_odd_count(1) == (0, 1)

def test_even_odd_count_large_number():
    """Test with a large number."""
    assert even_odd_count(12345678901234567890) == (10, 10)

def test_even_odd_count_mixed_digits():
    """Test with a number containing mixed even and odd digits."""
    assert even_odd_count(123456789) == (4, 5)

def test_even_odd_count_negative_mixed_digits():
    """Test with a negative number containing mixed even and odd digits."""
    assert even_odd_count(-123456789) == (4, 5)