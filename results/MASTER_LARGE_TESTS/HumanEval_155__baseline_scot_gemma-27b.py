# STEP 1: REASONING
# The function `even_odd_count` takes an integer as input and returns a tuple containing the count of even and odd digits in that integer.
# We need to test various scenarios:
# - Positive numbers
# - Negative numbers
# - Zero
# - Numbers with only even digits
# - Numbers with only odd digits
# - Numbers with a mix of even and odd digits
# - Large numbers
# - Edge cases like single-digit numbers

# STEP 2: PLAN
# 1. test_positive_number: Test with a positive number containing both even and odd digits.
# 2. test_negative_number: Test with a negative number containing both even and odd digits.
# 3. test_zero: Test with zero.
# 4. test_only_even_digits: Test with a number containing only even digits.
# 5. test_only_odd_digits: Test with a number containing only odd digits.
# 6. test_single_digit_even: Test with a single-digit even number.
# 7. test_single_digit_odd: Test with a single-digit odd number.
# 8. test_large_number: Test with a large number.
# 9. test_negative_large_number: Test with a large negative number.
# 10. test_number_with_leading_zeros: Test with a number that has leading zeros (e.g., 0012).

# STEP 3: CODE
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

def test_positive_number():
    assert even_odd_count(123) == (1, 2)

def test_negative_number():
    assert even_odd_count(-12) == (1, 1)

def test_zero():
    assert even_odd_count(0) == (1, 0)

def test_only_even_digits():
    assert even_odd_count(2468) == (4, 0)

def test_only_odd_digits():
    assert even_odd_count(1357) == (0, 4)

def test_single_digit_even():
    assert even_odd_count(2) == (1, 0)

def test_single_digit_odd():
    assert even_odd_count(1) == (0, 1)

def test_large_number():
    assert even_odd_count(1234567890) == (5, 5)

def test_negative_large_number():
    assert even_odd_count(-9876543210) == (5, 5)

def test_number_with_leading_zeros():
    assert even_odd_count(0012) == (1, 1)