import pytest
import math

def test_even_odd_count():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(246) == (3, 0)
    assert even_odd_count(13579) == (0, 5)
    assert even_odd_count(0) == (1, 0)

import pytest

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    num = abs(num)
    if num == 0:
        return (1, 0)
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num //= 10
    return (even_count, odd_count)

### SCoT Steps:
### STEP 1: REASONING - The function `even_odd_count` counts the number of even and odd digits in an integer. An edge case is when the input is 0. The function should return (1, 0) in this case.
### STEP 2: PLAN - Test function name: `test_zero`. Scenario: Input is 0.
### STEP 3: CODE - Write the high-quality pytest suite.
def test_zero():
    assert even_odd_count(0) == (1, 0)

import pytest

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even = 0
    odd = 0
    s = str(abs(num))
    for digit in s:
        digit = int(digit)
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)

### SCoT Steps:
### STEP 1: REASONING - The function `even_odd_count` counts the number of even and odd digits in an integer. We need to test a case where the input is zero. The current implementation handles negative numbers correctly by taking the absolute value.
### STEP 2: PLAN - Test function name: `test_zero_input`. Scenario: Input is 0. Expected output: (1, 0) because 0 is even.
### STEP 3: CODE - Write the high-quality pytest suite.
def test_zero_input():
    assert even_odd_count(0) == (1, 0)