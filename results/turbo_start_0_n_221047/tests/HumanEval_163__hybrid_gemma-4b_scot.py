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
                if not result or int(digit) > result[-1]:
                    result.append(int(digit))
    return result

### SCoT Steps:

# STEP 1: REASONING
# The function `generate_integers(a, b)` aims to extract even digits from the range of integers between `a` and `b` (inclusive) and return them in ascending order.
# The function handles cases where `a` is greater than `b` by reversing the range.
# The function should return an empty list if no even digits are found within the range.
# The function should correctly handle single-digit and multi-digit numbers.
# The function should handle edge cases such as `a` and `b` being equal, or `a` being greater than `b`.

# STEP 2: PLAN
# Test Cases:
# 1. Basic case: a = 2, b = 8 (Expected: [2, 4, 6, 8])
# 2. Reversed range: a = 8, b = 2 (Expected: [2, 4, 6, 8])
# 3. No even digits: a = 10, b = 14 (Expected: [])
# 4. Single digit a and b: a = 2, b = 2 (Expected: [2])
# 5. Single digit a and b, both odd (Expected: [])
# 6. Larger range with multiple even digits: a = 12, b = 20 (Expected: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
# 7. a and b are close to each other, with some even digits in between (Expected: [2, 4, 6, 8])
# 8. a is 1, b is 10 (Expected: [2, 4, 6, 8, 10])
# 9. a is 1, b is 1 (Expected: [])

### STEP 3: CODE
def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reversed():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_digit_a_b():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_single_digit_odd():
    assert generate_integers(1, 3) == []

def test_generate_integers_larger_range():
    assert generate_integers(12, 20) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def test_generate_integers_close_digits():
    assert generate_integers(7, 9) == [8]

def test_generate_integers_a_is_1_b_is_10():
    assert generate_integers(1, 10) == [2, 4, 6, 8, 10]

def test_generate_integers_a_is_1_b_is_1():
    assert generate_integers(1, 1) == []

def test_generate_integers_a_greater_than_b():
    assert generate_integers(5, 1) == [1, 2, 3, 4, 5]