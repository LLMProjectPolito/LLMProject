import pytest
import math

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

def test_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

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
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `generate_integers(a, b)` should return a list of even digits between `a` and `b` (inclusive), sorted in ascending order.
### The edge case to test is when `a` is greater than `b`. In this case, the loop should not execute, and an empty list should be returned.
### STEP 2: PLAN - List test functions names and scenarios.
### Test function name: `test_a_greater_than_b`
### Scenario: `a > b`
### STEP 3: CODE - Write the high-quality pytest suite.
###
def test_a_greater_than_b():
    assert generate_integers(10, 2) == []

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
### STEP 1: REASONING - The function `generate_integers` is designed to extract even digits within a given range.  A critical edge case to test is when `a` is greater than `b`. The function should still return an empty list in this scenario, as there are no numbers within the range to check.
### STEP 2: PLAN - Test function name: `test_invalid_range`. Scenario: Test the case where `a > b`.
### STEP 3: CODE - Write the high-quality pytest suite.
def test_invalid_range():
    assert generate_integers(10, 2) == []