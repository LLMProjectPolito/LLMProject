import pytest
import math


# Focus: Boundary Values
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
### The function `generate_integers` should return a list of even digits within a given range [a, b] (inclusive), sorted in ascending order.
### Boundary values are a=b, a>b, and a=1, b=10. We need to test cases where a and b are close to each other, far apart, and at the extreme ends of the possible input range.
### STEP 2: PLAN - List test functions names and scenarios.
### test_generate_integers_same_start_end
### test_generate_integers_a_greater_than_b
### test_generate_integers_a_equals_1_b_equals_10
### STEP 3: CODE - Write the high-quality pytest suite.

def test_generate_integers_same_start_end():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(4, 4) == [4]
    assert generate_integers(6, 6) == [6]

def test_generate_integers_a_greater_than_b():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_a_equals_1_b_equals_10():
    assert generate_integers(1, 10) == [2, 4, 6, 8]

# Focus: Type Scenarios
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
### The function `generate_integers` should return a list of even digits within a given range [a, b] (inclusive), sorted in ascending order. The function should handle cases where a > b, and where no even digits exist within the range. The test cases should cover these scenarios.
### STEP 2: PLAN - List test functions names and scenarios.
### test_generate_integers_ascending
### test_generate_integers_descending
### test_generate_integers_no_even
### STEP 3: CODE - Write the high-quality pytest suite.
###
def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(4, 6) == [4, 6]
    assert generate_integers(1, 5) == [2, 4]

def test_generate_integers_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(6, 4) == [4, 6]
    assert generate_integers(5, 1) == [2, 4]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []
    assert generate_integers(11, 13) == []
    assert generate_integers(1, 3) == []

# Focus: Logic Branches
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
### The function `generate_integers` should return a list of even digits within a given range [a, b] (inclusive), sorted in ascending order.
### The function should handle cases where a > b, and where no even digits exist within the range.
### The function should handle duplicate even digits within the range.

### STEP 2: PLAN - List test functions names and scenarios.
### test_generate_integers_ascending
### test_generate_integers_descending
### test_generate_integers_no_even_digits

### STEP 3: CODE - Write the high-quality pytest suite.
def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(1, 9) == [2, 4, 6, 8]
    assert generate_integers(4, 4) == [4]
    assert generate_integers(2, 2) == [2]

def test_generate_integers_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(9, 1) == [2, 4, 6, 8]
    assert generate_integers(4, 4) == [4]
    assert generate_integers(2, 2) == [2]

def test_generate_integers_no_even_digits():
    assert generate_integers(10, 14) == []
    assert generate_integers(11, 13) == []
    assert generate_integers(1, 3) == []
    assert generate_integers(15, 17) == []