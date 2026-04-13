
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

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `generate_integers(a, b)` should return a list of even digits
# present in the range [a, b] (inclusive), sorted in ascending order.
# The function should handle cases where a > b, where there are no even digits,
# and where the input integers are single-digit numbers.
# Edge cases include:
#   - a and b are equal
#   - a is greater than b
#   - no even digits in the range
#   - a and b are both even or both odd
#   - a and b are single digits

# STEP 2: PLAN - List test functions names and scenarios.
# test_generate_integers_basic: Test with a simple range containing even digits.
# test_generate_integers_reverse: Test with a range in reverse order.
# test_generate_integers_no_even: Test with a range containing no even digits.
# test_generate_integers_single_digit: Test with a single-digit input.
# test_generate_integers_a_greater_than_b: Test with a > b.
# test_generate_integers_a_equals_b: Test with a == b.
# test_generate_integers_mixed_digits: Test with a range containing mixed digits.

# STEP 3: CODE - Write the high-quality pytest suite.
###
def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reverse():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(1, 3) == []

def test_generate_integers_single_digit():
    assert generate_integers(2, 2) == [2]
    assert generate_integers(7, 7) == []
    assert generate_integers(8, 8) == [8]
    assert generate_integers(2, 2) == [2]

def test_generate_integers_a_greater_than_b():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_a_equals_b():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_mixed_digits():
    assert generate_integers(10, 14) == []
    assert generate_integers(20, 24) == [2, 4]
    assert generate_integers(12, 16) == [2, 4, 6]
    assert generate_integers(1, 5) == [2, 4]
    assert generate_integers(1, 1) == []