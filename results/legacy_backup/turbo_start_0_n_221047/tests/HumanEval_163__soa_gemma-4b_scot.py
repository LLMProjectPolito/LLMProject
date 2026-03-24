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
# The function `generate_integers(a, b)` should return a list of even digits present in the integers between `a` and `b` (inclusive), sorted in ascending order.
# The function should handle cases where `a > b` correctly by reversing the range.
# The function should handle cases where no even digits are present in the range.
# The function should handle duplicate even digits correctly.
# The function should handle single-digit and multi-digit numbers.

### STEP 2: PLAN
# Test cases:
# 1. Basic case: a=2, b=8 (expected: [2, 4, 6, 8])
# 2. a > b: a=8, b=2 (expected: [2, 4, 6, 8])
# 3. No even digits: a=10, b=14 (expected: [])
# 4. Single digit even number: a=2, b=2 (expected: [2])
# 5. Single digit odd number: a=1, b=1 (expected: [])
# 6. Mixed even and odd digits: a=1, b=5 (expected: [])
# 7. Larger range with multiple even digits: a=10, b=20 (expected: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
# 8. Edge case: a=0, b=1 (expected: [])
# 9. Edge case: a=1, b=0 (expected: [])
# 10. a and b are the same even number: a=2, b=2 (expected: [2])

### STEP 3: CODE
def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reverse_order():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_digit_even():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_single_digit_odd():
    assert generate_integers(1, 1) == []

def test_generate_integers_mixed_digits():
    assert generate_integers(1, 5) == []

def test_generate_integers_larger_range():
    assert generate_integers(10, 20) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def test_generate_integers_edge_case_zero_one():
    assert generate_integers(0, 1) == []

def test_generate_integers_edge_case_one_zero():
    assert generate_integers(1, 0) == []

def test_generate_integers_same_even_number():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_larger_range_with_duplicates():
    assert generate_integers(2, 6) == [2, 4, 6]

def test_generate_integers_range_with_large_numbers():
    assert generate_integers(100, 110) == [100, 102, 104, 106, 108, 110]