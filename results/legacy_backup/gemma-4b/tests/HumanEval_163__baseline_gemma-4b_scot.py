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
# 1.  `a` and `b` are consecutive and contain even digits.
# 2.  `a` and `b` are consecutive and do not contain even digits.
# 3.  `a` and `b` are not consecutive.
# 4.  `a` is greater than `b`.
# 5.  The list of even digits is empty.
# 6.  The list of even digits contains duplicate values.

### STEP 2: PLAN
# Test functions:
# - test_consecutive_even: Tests the case where a and b are consecutive and contain even digits.
# - test_consecutive_odd: Tests the case where a and b are consecutive and do not contain even digits.
# - test_non_consecutive: Tests the case where a and b are not consecutive.
# - test_a_greater_than_b: Tests the case where a is greater than b.
# - test_empty_list: Tests the case where the list of even digits is empty.
# - test_duplicate_values: Tests the case where the list of even digits contains duplicate values.

### STEP 3: CODE
def test_consecutive_even():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_consecutive_odd():
    assert generate_integers(1, 3) == []

def test_non_consecutive():
    assert generate_integers(10, 14) == []

def test_a_greater_than_b():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_empty_list():
    assert generate_integers(1, 1) == []

def test_duplicate_values():
    assert generate_integers(2, 2) == [2]