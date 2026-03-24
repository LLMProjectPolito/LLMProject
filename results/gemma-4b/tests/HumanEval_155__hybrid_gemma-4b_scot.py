
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

### SCoT Steps:

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `even_odd_count` takes an integer as input and returns a tuple containing the count of even and odd digits in the integer.
# The function should handle negative integers by taking the absolute value.
# The function should correctly count even and odd digits for various integer inputs, including single-digit numbers, multi-digit numbers, and numbers with leading zeros (implicitly handled by converting to string).
# Edge cases: 0, negative numbers, large numbers, single digit numbers.

# STEP 2: PLAN - List test functions names and scenarios.
# test_even_odd_count_positive
# test_even_odd_count_negative
# test_even_odd_count_zero
# test_even_odd_count_single_digit_even
# test_even_odd_count_single_digit_odd
# test_even_odd_count_multiple_digits
# test_even_odd_count_large_number
# test_even_odd_count_mixed_digits

# STEP 3: CODE - Write the high-quality pytest suite.
def test_even_odd_count_positive():
    assert even_odd_count(123) == (1, 2)

def test_even_odd_count_negative():
    assert even_odd_count(-12) == (1, 1)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_single_digit_even():
    assert even_odd_count(2) == (1, 0)

def test_even_odd_count_single_digit_odd():
    assert even_odd_count(1) == (0, 1)

def test_even_odd_count_multiple_digits():
    assert even_odd_count(123456789) == (4, 5)

def test_even_odd_count_large_number():
    assert even_odd_count(1234567890) == (5, 5)

def test_even_odd_count_mixed_digits():
    assert even_odd_count(123454321) == (3, 4)