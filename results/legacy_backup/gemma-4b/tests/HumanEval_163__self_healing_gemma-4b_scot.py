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
# The function `generate_integers(a, b)` should return a list of even digits between `a` and `b` (inclusive), sorted in ascending order.
# The function should handle cases where `a > b` by reversing the range.
# The function should handle cases where no even digits are present in the range.
# The function should handle duplicate even digits.

### STEP 2: PLAN
# Test cases:
# 1. Basic case: a = 2, b = 8 (expected: [2, 4, 6, 8])
# 2. a > b: a = 8, b = 2 (expected: [2, 4, 6, 8])
# 3. No even digits: a = 10, b = 14 (expected: [])
# 4. Single digit even number: a = 2, b = 2 (expected: [2])
# 5. Multiple even digits: a = 2, b = 6 (expected: [2, 4, 6])
# 6. Larger range with even digits: a = 10, b = 20 (expected: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
# 7. Edge case: a = b (expected: [a])
# 8. a and b are consecutive even numbers: a = 4, b = 6 (expected: [4, 6])

### STEP 3: CODE
def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_a_greater_than_b():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_digit_even():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_multiple_even_digits():
    assert generate_integers(2, 6) == [2, 4, 6]

def test_generate_integers_larger_range():
    assert generate_integers(10, 20) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def test_generate_integers_a_equals_b():
    assert generate_integers(5, 5) == [5]

def test_generate_integers_consecutive_even():
    assert generate_integers(4, 6) == [4, 6]

def test_generate_integers_with_duplicates():
    assert generate_integers(2, 6) == [2, 4, 6]

def test_generate_integers_with_zero():
    assert generate_integers(0, 10) == [0, 2, 4, 6, 8, 10]