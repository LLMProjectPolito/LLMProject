
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

# STEP 1: REASONING
# The function `generate_integers(a, b)` aims to extract even digits from the range [a, b] (inclusive) and return them in ascending order.
# The function handles cases where a > b by reversing the range.
# The function should return an empty list if no even digits are found within the range.
# The function should handle duplicate even digits correctly, ensuring only unique even digits are included in the result.
# The function should handle single-digit and multi-digit numbers correctly.

# STEP 2: PLAN
# Test Cases:
# 1. Basic case: a = 2, b = 8 (Expected: [2, 4, 6, 8])
# 2. a > b: a = 8, b = 2 (Expected: [2, 4, 6, 8])
# 3. No even digits: a = 10, b = 14 (Expected: [])
# 4. Single digit even number: a = 2, b = 2 (Expected: [2])
# 5. Single digit odd number: a = 1, b = 1 (Expected: [])
# 6. Mixed even and odd digits: a = 1, b = 5 (Expected: [2, 4])
# 7. Larger range with multiple even digits: a = 10, b = 20 (Expected: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
# 8. Edge case: a = b (Expected: [a])
# 9. a and b are both even: a = 2, b = 6 (Expected: [2, 4, 6])

# Test Function Names:
# test_generate_integers_basic
# test_generate_integers_reverse
# test_generate_integers_no_even
# test_generate_integers_single_even
# test_generate_integers_single_odd
# test_generate_integers_mixed
# test_generate_integers_larger_range
# test_generate_integers_edge_case
# test_generate_integers_both_even

# STEP 3: CODE
def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reverse():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_even():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_single_odd():
    assert generate_integers(1, 1) == []

def test_generate_integers_mixed():
    assert generate_integers(1, 5) == [2, 4]

def test_generate_integers_larger_range():
    assert generate_integers(10, 20) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def test_generate_integers_edge_case():
    assert generate_integers(5, 5) == [5]

def test_generate_integers_both_even():
    assert generate_integers(2, 6) == [2, 4, 6]