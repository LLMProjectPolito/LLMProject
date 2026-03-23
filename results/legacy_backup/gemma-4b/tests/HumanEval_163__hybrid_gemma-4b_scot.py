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
# present in the integers between `a` and `b` (inclusive), sorted in ascending
# order.  The function should handle cases where `a > b` (reversing the range),
# where no even digits are present, and where the input integers contain
# multiple occurrences of the same even digit.  The digits should be integers,
# not strings.

# STEP 2: PLAN - List test functions names and scenarios.
# test_generate_integers_basic: Test with simple ranges containing even digits.
# test_generate_integers_reverse: Test with `a > b` to ensure the range is reversed.
# test_generate_integers_no_even: Test with a range containing no even digits.
# test_generate_integers_duplicate_even: Test with duplicate even digits in the range.
# test_generate_integers_single_digit: Test with a single digit range.
# test_generate_integers_large_range: Test with a larger range to check performance.
# test_generate_integers_zero_range: Test with a range that includes zero.

# STEP 3: CODE - Write the high-quality pytest suite.
def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(4, 6) == [4, 6]
    assert generate_integers(1, 5) == [2, 4]

def test_generate_integers_reverse():
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(14, 10) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(1, 3) == []
    assert generate_integers(5, 7) == []

def test_generate_integers_duplicate_even():
    assert generate_integers(2, 6) == [2, 4, 6]
    assert generate_integers(4, 8) == [4, 6, 8]

def test_generate_integers_single_digit():
    assert generate_integers(2, 2) == [2]
    assert generate_integers(8, 8) == [8]
    assert generate_integers(1, 1) == []

def test_generate_integers_large_range():
    assert generate_integers(100, 110) == [10, 12, 14, 16, 18]
    assert generate_integers(1000, 1010) == [10, 12, 14, 16, 18]

def test_generate_integers_zero_range():
    assert generate_integers(0, 2) == [0, 2]
    assert generate_integers(2, 0) == [2, 4, 6, 8]