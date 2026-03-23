def even_odd_count(num):
    """Given an integer, return a tuple containing the count of even and odd digits in its absolute value.
    The function handles negative numbers by taking the absolute value before processing.
    The function returns the counts for the *absolute value* of the input.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
        even_odd_count(0) ==> (1, 0)
        even_odd_count(2468) ==> (4, 0)
        even_odd_count(13579) ==> (0, 5)
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

def test_even_odd_count_single_even():
    assert even_odd_count(2) == (1, 0)

def test_even_odd_count_single_odd():
    assert even_odd_count(1) == (0, 1)

def test_even_odd_count_all_even():
    assert even_odd_count(2468) == (4, 0)

def test_even_odd_count_all_odd():
    assert even_odd_count(13579) == (0, 5)

def test_even_odd_count_mixed_digits():
    assert even_odd_count(1234567890) == (5, 5)

def test_even_odd_count_negative_number():
    assert even_odd_count(-12345) == (2, 3)

def test_even_odd_count_another_larger_number():
    assert even_odd_count(987654321) == (4, 6)

def test_even_odd_count_all_zeros():
    assert even_odd_count(1000) == (4, 0)

def test_even_odd_count_large_number():
    assert even_odd_count(12345678901234567890) == (10, 10)