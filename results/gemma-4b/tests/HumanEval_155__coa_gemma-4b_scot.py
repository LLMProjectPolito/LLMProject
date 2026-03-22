import pytest
import math


# Focus: Boundary Values
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
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `even_odd_count` takes an integer as input and returns a tuple containing the number of even and odd digits in the integer.
### Boundary values to consider:
### 1. Negative numbers: The function should handle negative numbers correctly by taking the absolute value.
### 2. Zero: The function should return (1, 0) for zero as it has one digit (0) which is even.
### 3. Large numbers: The function should handle large numbers without overflow issues.
### 4. Numbers with only even or only odd digits.

### STEP 2: PLAN - List test functions names and scenarios.
### Test functions:
### - test_negative_number
### - test_zero
### - test_all_even_digits
### - test_all_odd_digits

### STEP 3: CODE - Write the high-quality pytest suite.
###
### test_negative_number - Test with a negative number.
### test_zero - Test with zero.
### test_all_even_digits - Test with a number containing only even digits.
### test_all_odd_digits - Test with a number containing only odd digits.

###
pytest.mark.parametrize("input, expected", [
    (-12, (1, 1)),
    (123, (1, 2)),
    (0, (1, 0)),
    (-246, (2, 2)),
    (13579, (0, 5)),
    (24680, (4, 0)),
    (11111, (0, 5)),
    (-11111, (0, 5)),
    (22222, (5, 0)),
    (-22222, (5, 0))
])
def test_negative_number(input, expected):
    assert even_odd_count(input) == expected

pytest.mark.parametrize("input, expected", [
    (0, (1, 0)),
    (24680, (4, 0)),
    (13579, (0, 5)),
    (11111, (0, 5)),
    (-11111, (0, 5)),
    (22222, (5, 0)),
    (-22222, (5, 0))
])
def test_zero(input, expected):
    assert even_odd_count(input) == expected

pytest.mark.parametrize("input, expected", [
    (2468, (4, 0)),
    (13579, (0, 5)),
    (11111, (0, 5)),
    (22222, (5, 0)),
    (33333, (5, 0)),
    (44444, (4, 0)),
    (55555, (5, 0))
])
def test_all_even_digits(input, expected):
    assert even_odd_count(input) == expected

pytest.mark.parametrize("input, expected", [
    (13579, (0, 5)),
    (11111, (0, 5)),
    (33333, (5, 0)),
    (55555, (5, 0)),
    (77777, (5, 0)),
    (99999, (5, 0))
])
def test_all_odd_digits(input, expected):
    assert even_odd_count(input) == expected

# Focus: Type Scenarios
import pytest

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for digit in str(abs(num)):
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `even_odd_count` takes an integer as input and returns a tuple containing the number of even and odd digits in the integer.
### The test functions should cover various scenarios including positive numbers, negative numbers, numbers with only even digits, numbers with only odd digits, and numbers with a mix of even and odd digits.
### STEP 2: PLAN - List test functions names and scenarios.
### Test functions:
### - test_positive_mixed: Test with a positive number containing both even and odd digits.
### - test_negative_mixed: Test with a negative number containing both even and odd digits.
### - test_all_even: Test with a number containing only even digits.
### - test_all_odd: Test with a number containing only odd digits.
### STEP 3: CODE - Write the high-quality pytest suite.

### Test functions
def test_positive_mixed():
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(2468) == (4, 0)
    assert even_odd_count(13579) == (0, 5)

def test_negative_mixed():
    assert even_odd_count(-123) == (1, 2)
    assert even_odd_count(-2468) == (4, 0)
    assert even_odd_count(-13579) == (0, 5)

def test_all_even():
    assert even_odd_count(2468) == (4, 0)
    assert even_odd_count(0) == (1, 0)

def test_all_odd():
    assert even_odd_count(13579) == (0, 5)
    assert even_odd_count(-13579) == (0, 5)

# Focus: Logic Branches
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
    for digit in str(num):
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `even_odd_count` takes an integer as input and returns a tuple containing the count of even and odd digits.
### We need to test different scenarios including positive numbers, negative numbers, numbers with only even digits, numbers with only odd digits, and mixed numbers.
### STEP 2: PLAN - List test functions names and scenarios.
### Test functions:
### - test_positive_mixed: Test with a positive number containing both even and odd digits.
### - test_negative_mixed: Test with a negative number containing both even and odd digits.
### - test_all_even: Test with a number containing only even digits.
### - test_all_odd: Test with a number containing only odd digits.
### STEP 3: CODE - Write the high-quality pytest suite.

### Test functions
def test_positive_mixed():
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(2468) == (4, 0)
    assert even_odd_count(13579) == (0, 5)

def test_negative_mixed():
    assert even_odd_count(-123) == (1, 2)
    assert even_odd_count(-2468) == (4, 0)
    assert even_odd_count(-13579) == (0, 5)

def test_all_even():
    assert even_odd_count(2468) == (4, 0)
    assert even_odd_count(0) == (1, 0)

def test_all_odd():
    assert even_odd_count(13579) == (0, 5)
    assert even_odd_count(-13579) == (0, 5)