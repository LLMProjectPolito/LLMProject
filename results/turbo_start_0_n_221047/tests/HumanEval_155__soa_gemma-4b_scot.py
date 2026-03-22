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

### STEP 1: REASONING - Analyze functional goals and constraints.
# The function `even_odd_count` takes an integer as input and returns a tuple containing the count of even and odd digits in the integer.
# The function should handle negative integers correctly by taking the absolute value.
# The function should handle integers with zero as a digit.
# The function should handle integers with only even or only odd digits.
# The function should handle integers with a mix of even and odd digits.

### STEP 2: PLAN - List test functions names and scenarios.
# Test cases for positive integers
# Test cases for negative integers
# Test cases for integers with only even digits
# Test cases for integers with only odd digits
# Test cases for integers with zero as a digit
# Test cases for integers with a mix of even and odd digits
# Test cases for edge cases (e.g., 0, 1, 10, 11, 12345)

### STEP 3: CODE - Write the high-quality pytest suite.
def test_positive_integer():
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(2468) == (4, 0)
    assert even_odd_count(1357) == (0, 4)

def test_negative_integer():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-2468) == (4, 0)
    assert even_odd_count(-1357) == (0, 4)

def test_zero():
    assert even_odd_count(0) == (1, 0)

def test_single_digit_even():
    assert even_odd_count(2) == (1, 0)

def test_single_digit_odd():
    assert even_odd_count(1) == (0, 1)

def test_mixed_digits():
    assert even_odd_count(1234567890) == (5, 5)
    assert even_odd_count(24681357) == (4, 4)

def test_large_number():
    assert even_odd_count(12345678901234567890) == (10, 10)

def test_negative_large_number():
    assert even_odd_count(-12345678901234567890) == (10, 10)