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

### STEP 1: REASONING
# The function `even_odd_count` takes an integer as input and returns a tuple containing the number of even and odd digits in the integer.
# We need to test various scenarios including positive numbers, negative numbers, numbers with only even digits, numbers with only odd digits, and numbers with a mix of even and odd digits.
# Edge cases: 0, negative numbers, single digit numbers.

### STEP 2: PLAN
# Test cases:
# 1. Positive number with even and odd digits
# 2. Negative number with even and odd digits
# 3. Number with only even digits
# 4. Number with only odd digits
# 5. Zero
# 6. Single digit even number
# 7. Single digit odd number
# 8. Large number with mixed digits

### STEP 3: CODE
def test_positive_mixed():
    assert even_odd_count(123) == (1, 2)

def test_negative_mixed():
    assert even_odd_count(-12) == (1, 1)

def test_positive_even_only():
    assert even_odd_count(2468) == (4, 0)

def test_positive_odd_only():
    assert even_odd_count(13579) == (0, 5)

def test_zero():
    assert even_odd_count(0) == (1, 0)

def test_single_digit_even():
    assert even_odd_count(2) == (1, 0)

def test_single_digit_odd():
    assert even_odd_count(1) == (0, 1)

def test_large_mixed():
    assert even_odd_count(1234567890) == (5, 5)

def test_negative_zero():
    assert even_odd_count(-0) == (1, 0)

def test_negative_even_only():
    assert even_odd_count(-2468) == (4, 0)

def test_negative_odd_only():
    assert even_odd_count(-13579) == (0, 5)