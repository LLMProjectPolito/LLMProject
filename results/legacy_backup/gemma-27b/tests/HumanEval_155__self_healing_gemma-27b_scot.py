import pytest

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num_str = str(abs(num))
    even_count = 0
    odd_count = 0
    for digit in num_str:
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

# STEP 1: REASONING
# The function `even_odd_count` takes an integer as input and returns a tuple containing the counts of even and odd digits.
# The input can be positive or negative. The absolute value of the input is used to process the digits.
# The function should handle single-digit numbers, multi-digit numbers, and zero correctly.
# Edge cases include negative numbers, zero, and numbers with leading zeros (although leading zeros are not relevant since the input is an integer).

# STEP 2: PLAN
# Test functions:
# - test_positive_number: Tests with a positive number containing both even and odd digits.
# - test_negative_number: Tests with a negative number containing both even and odd digits.
# - test_all_even_digits: Tests with a number containing only even digits.
# - test_all_odd_digits: Tests with a number containing only odd digits.
# - test_single_digit_even: Tests with a single even digit.
# - test_single_digit_odd: Tests with a single odd digit.
# - test_zero: Tests with zero as input.
# - test_large_number: Tests with a large number to ensure scalability.
# - test_number_with_leading_zero: Tests with a number that would have leading zeros if represented as a string (e.g., 102).

# STEP 3: CODE
def test_positive_number():
    assert even_odd_count(123) == (1, 2)

def test_negative_number():
    assert even_odd_count(-12) == (1, 1)

def test_all_even_digits():
    assert even_odd_count(2468) == (4, 0)

def test_all_odd_digits():
    assert even_odd_count(1357) == (0, 4)

def test_single_digit_even():
    assert even_odd_count(2) == (1, 0)

def test_single_digit_odd():
    assert even_odd_count(1) == (0, 1)

def test_zero():
    assert even_odd_count(0) == (1, 0)

def test_large_number():
    assert even_odd_count(1234567890) == (5, 5)

def test_number_with_leading_zero():
    assert even_odd_count(102) == (2, 1)

def test_negative_large_number():
    assert even_odd_count(-9876543210) == (5, 5)

def test_mixed_positive_negative():
    assert even_odd_count(123456789) == (4, 5)