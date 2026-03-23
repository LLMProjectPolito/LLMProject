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
    if num == 0:
        return (1, 0)
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num //= 10
    return (even_count, odd_count)

### SCoT Steps:

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `even_odd_count` takes an integer as input and returns a tuple containing the count of even and odd digits in the integer.
# The function should handle negative numbers by taking the absolute value.
# The function should handle the case where the input is 0.
# The function should correctly count even and odd digits for various positive and negative integers.

# STEP 2: PLAN - List test functions names and scenarios.
# test_positive_number
# test_negative_number
# test_zero
# test_single_digit_even
# test_single_digit_odd
# test_multiple_digits_even
# test_multiple_digits_odd
# test_mixed_digits
# test_large_number

# STEP 3: CODE - Write the high-quality pytest suite.
###
def test_positive_number():
    assert even_odd_count(123) == (1, 2)

def test_negative_number():
    assert even_odd_count(-12) == (1, 1)

def test_zero():
    assert even_odd_count(0) == (1, 0)

def test_single_digit_even():
    assert even_odd_count(2) == (1, 0)

def test_single_digit_odd():
    assert even_odd_count(1) == (0, 1)

def test_multiple_digits_even():
    assert even_odd_count(2468) == (4, 0)

def test_multiple_digits_odd():
    assert even_odd_count(13579) == (0, 5)

def test_mixed_digits():
    assert even_odd_count(1234567890) == (5, 5)

def test_large_number():
    assert even_odd_count(12345678901234567890) == (10, 10)

def test_negative_large_number():
    assert even_odd_count(-12345678901234567890) == (10, 10)