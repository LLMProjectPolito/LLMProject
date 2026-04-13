
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

def even_odd_count(num):
    """Given an integer (positive or negative), return a tuple that has the number of even and odd digits respectively.
    The function handles negative numbers by taking the absolute value.

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


### Tests (Pytest):
import pytest

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_single_digit_even():
    assert even_odd_count(2) == (1, 0)

def test_even_odd_count_single_digit_odd():
    assert even_odd_count(1) == (0, 1)

def test_even_odd_count_all_even():
    assert even_odd_count(2468) == (4, 0)

def test_even_odd_count_all_odd():
    assert even_odd_count(13579) == (0, 5)

def test_even_odd_count_larger_number_mixed():
    assert even_odd_count(1234567890) == (5, 5)

def test_even_odd_count_larger_number_even_dominant():
    assert even_odd_count(24680246) == (7, 1)

def test_even_odd_count_larger_number_odd_dominant():
    assert even_odd_count(135791357) == (1, 8)

def test_even_odd_count_negative_number():
    assert even_odd_count(-1234) == (2, 2)

def test_even_odd_count_number_with_leading_zeros():
    assert even_odd_count(0000) == (4, 0)

def test_even_odd_count_very_large_number():
    large_number = 123456789012345678901234567890
    assert even_odd_count(large_number) == (10, 20)