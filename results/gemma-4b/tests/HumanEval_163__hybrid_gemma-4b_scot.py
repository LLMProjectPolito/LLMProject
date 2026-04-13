
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

import pytest

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    result = []
    for i in range(a, b + 1):
        s = str(i)
        for digit in s:
            if int(digit) % 2 == 0:
                if int(digit) not in result:
                    result.append(int(digit))
    result.sort()
    return result

### SCoT Steps:

### STEP 1: REASONING
# The function `generate_integers(a, b)` aims to extract even digits within a given range [a, b] (inclusive) and return them in ascending order.
# The function handles cases where a > b by reversing the range.
# The function should return an empty list if no even digits are found within the range.
# The function should handle duplicate even digits correctly, ensuring only unique even digits are included in the result.
# The function should handle single-digit and multi-digit numbers correctly.
# The function should handle edge cases like a=b, a=1, b=10, etc.

### STEP 2: PLAN
# Test Cases:
# 1. Basic case: a=2, b=8 (Expected: [2, 4, 6, 8])
# 2. Reversed range: a=8, b=2 (Expected: [2, 4, 6, 8])
# 3. No even digits: a=10, b=14 (Expected: [])
# 4. Single digit a and b: a=2, b=2 (Expected: [2])
# 5. Single digit a and b, odd: a=1, b=1 (Expected: [])
# 6. Larger range with multiple even digits: a=10, b=20 (Expected: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
# 7. Range with only one even digit: a=2, b=2 (Expected: [2])
# 8. Range with duplicate even digits: a=2, b=6 (Expected: [2, 4, 6])
# 9. a > b (Expected: [2, 4, 6, 8])
# 10. a and b are zero (Expected: [])

# Test Functions:
# test_basic_range
# test_reversed_range
# test_no_even_digits
# test_single_digit_a_b
# test_single_digit_a_b_odd
# test_larger_range
# test_single_digit_a_b_even
# test_duplicate_even_digits
# test_a_greater_than_b
# test_zero_input

### STEP 3: CODE
def test_basic_range():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_reversed_range():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_no_even_digits():
    assert generate_integers(10, 14) == []

def test_single_digit_a_b():
    assert generate_integers(2, 2) == [2]

def test_single_digit_a_b_odd():
    assert generate_integers(1, 1) == []

def test_larger_range():
    assert generate_integers(10, 20) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def test_single_digit_a_b_even():
    assert generate_integers(2, 2) == [2]

def test_duplicate_even_digits():
    assert generate_integers(2, 6) == [2, 4, 6]

def test_a_greater_than_b():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_zero_input():
    assert generate_integers(0, 0) == []
    assert generate_integers(0, 1) == []
    assert generate_integers(1, 0) == []