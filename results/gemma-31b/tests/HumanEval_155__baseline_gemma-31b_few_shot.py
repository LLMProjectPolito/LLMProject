
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

def test_even_odd_count_basic_positive():
    """Test basic positive integers with mixed digits."""
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(4567) == (2, 2)

def test_even_odd_count_basic_negative():
    """Test negative integers to ensure the sign is ignored."""
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-482) == (3, 0)
    assert even_odd_count(-135) == (0, 3)

def test_even_odd_count_zero():
    """Test the number zero, which is considered an even digit."""
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_all_even():
    """Test numbers containing only even digits."""
    assert even_odd_count(2468) == (4, 0)
    assert even_odd_count(-204) == (3, 0)

def test_even_odd_count_all_odd():
    """Test numbers containing only odd digits."""
    assert even_odd_count(13579) == (0, 5)
    assert even_odd_count(-111) == (0, 3)

def test_even_odd_count_single_digit():
    """Test single digit edge cases."""
    assert even_odd_count(2) == (1, 0)
    assert even_odd_count(3) == (0, 1)
    assert even_odd_count(-4) == (1, 0)
    assert even_odd_count(-5) == (0, 1)

def test_even_odd_count_large_number():
    """Test a large integer to ensure scalability."""
    # 10 digits: 5 even (2, 4, 6, 8, 0), 5 odd (1, 3, 5, 7, 9)
    assert even_odd_count(1234567890) == (5, 5)