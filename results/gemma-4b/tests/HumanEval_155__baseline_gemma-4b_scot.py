
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
    for digit in str(abs(num)):
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

### SCoT Steps:

### STEP 1: REASONING
# The function `even_odd_count` takes an integer as input and returns a tuple containing the count of even and odd digits in the integer.
# We need to test various scenarios including positive numbers, negative numbers, numbers with only even digits, numbers with only odd digits, and numbers with a mix of even and odd digits.
# We should also consider edge cases like zero and negative numbers.

### STEP 2: PLAN
# Test cases:
# 1. Positive number with even and odd digits: (123, (1, 2))
# 2. Negative number with even and odd digits: (-12, (1, 1))
# 3. Positive number with only even digits: (246, (3, 0))
# 4. Positive number with only odd digits: (135, (0, 3))
# 5. Zero: (0, (0, 0))
# 6. Negative zero: (-0, (0, 0))
# 7. Single digit even: (2, (0, 1))
# 8. Single digit odd: (1, (0, 1))

### STEP 3: CODE
def test_positive_mixed():
    assert even_odd_count(123) == (1, 2)

def test_negative_mixed():
    assert even_odd_count(-12) == (1, 1)

def test_positive_even_only():
    assert even_odd_count(246) == (3, 0)

def test_positive_odd_only():
    assert even_odd_count(135) == (0, 3)

def test_zero():
    assert even_odd_count(0) == (0, 0)

def test_negative_zero():
    assert even_odd_count(-0) == (0, 0)

def test_single_digit_even():
    assert even_odd_count(2) == (1, 0)

def test_single_digit_odd():
    assert even_odd_count(1) == (0, 1)

def test_large_number():
    assert even_odd_count(1234567890) == (5, 5)

def test_negative_large_number():
    assert even_odd_count(-1234567890) == (5, 5)