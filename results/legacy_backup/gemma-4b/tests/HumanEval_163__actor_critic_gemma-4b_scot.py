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
# test_generate_integers_basic: Test with a simple range of numbers.
# test_generate_integers_reverse_range: Test with a range in reverse order.
# test_generate_integers_no_even_digits: Test with a range containing no even digits.
# test_generate_integers_single_digit: Test with a single-digit input.
# test_generate_integers_a_equals_b: Test when a and b are equal.
# test_generate_integers_a_greater_than_b: Test when a is greater than b.
# test_generate_integers_mixed_digits: Test with a range containing mixed digits.
# test_generate_integers_large_numbers: Test with larger numbers to ensure no overflow issues.


# STEP 3: CODE - Write the high-quality pytest suite.
def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reverse_range():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(1, 3) == []

def test_generate_integers_single_digit():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_a_equals_b():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_a_greater_than_b():
    assert generate_integers(5, 3) == [3, 5]

def test_generate_integers_mixed_digits():
    assert generate_integers(10, 14) == []

def test_generate_integers_large_numbers():
    assert generate_integers(100, 102) == [1, 0]

def test_generate_integers_even_and_odd():
    assert generate_integers(1, 5) == [2, 4]

def test_generate_integers_all_even():
    assert generate_integers(2, 6) == [2, 4, 6]

def test_generate_integers_empty_range():
    assert generate_integers(1, 1) == []

def test_generate_integers_both_even():
    assert generate_integers(2, 4) == [2, 4]

def test_generate_integers_single_even():
    assert generate_integers(1, 1) == []

def test_generate_integers_single_even_and_even():
    assert generate_integers(1, 2) == [2]