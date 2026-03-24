
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
    """Test with a positive number containing mixed digits."""
    assert even_odd_count(12345) == (2, 3)

def test_negative_number():
    """Test with a negative number containing mixed digits."""
    assert even_odd_count(-12345) == (2, 3)

def test_zero():
    """Test with the number zero."""
    assert even_odd_count(0) == (1, 0)

def test_single_even_digit():
    """Test with a single even digit."""
    assert even_odd_count(2) == (1, 0)

def test_single_odd_digit():
    """Test with a single odd digit."""
    assert even_odd_count(1) == (0, 1)

def test_all_even_digits():
    """Test with a number containing only even digits."""
    assert even_odd_count(2468) == (4, 0)

def test_all_odd_digits():
    """Test with a number containing only odd digits."""
    assert even_odd_count(13579) == (0, 5)

def test_mixed_digits():
    """Test with a number containing mixed even and odd digits."""
    assert even_odd_count(1234567890) == (5, 5)

def test_large_number():
    """Test with a large number containing mixed digits."""
    assert even_odd_count(12345678901234567890) == (5, 15)

def test_number_with_zeros():
    """Test with a number containing zeros."""
    assert even_odd_count(1020304050) == (5, 5)

def test_negative_number_with_zeros():
    """Test with a negative number containing zeros."""
    assert even_odd_count(-1020304050) == (5, 5)

def test_number_with_leading_zeros():
    """Test with a number containing leading zeros (e.g., 0000123)."""
    assert even_odd_count(0000123) == (1, 2)

def test_empty_string():
    """Test with an empty string input."""
    with pytest.raises(TypeError):
        even_odd_count("")

def test_max_integer():
    """Test with a number close to the maximum integer size."""
    assert even_odd_count(2147483647) == (3, 8)