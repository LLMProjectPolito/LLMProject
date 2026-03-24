
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
# The function `generate_integers(a, b)` should return a list of even digits between `a` and `b` (inclusive), sorted in ascending order.
# We need to test various scenarios including:
# 1.  `a` and `b` are equal.
# 2.  `a` is less than `b`.
# 3.  `a` is greater than `b`.
# 4.  No even digits exist between `a` and `b`.
# 5.  The range contains only even digits.
# 6.  The range contains a mix of even and odd digits.
# 7.  Edge cases: `a` and `b` are small numbers.

### STEP 2: PLAN
# Test functions:
# - test_generate_integers_equal
# - test_generate_integers_a_less_than_b
# - test_generate_integers_a_greater_than_b
# - test_generate_integers_no_even_digits
# - test_generate_integers_only_even_digits
# - test_generate_integers_mix_even_odd
# - test_generate_integers_edge_cases

### STEP 3: CODE
def test_generate_integers_equal():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_a_less_than_b():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_a_greater_than_b():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(10, 14) == []

def test_generate_integers_only_even_digits():
    assert generate_integers(2, 6) == [2, 4, 6]

def test_generate_integers_mix_even_odd():
    assert generate_integers(1, 5) == [2, 4]

def test_generate_integers_edge_cases():
    assert generate_integers(0, 1) == []
    assert generate_integers(2, 4) == [2, 4]
    assert generate_integers(4, 2) == [2, 4]