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
### The function `even_odd_count` takes an integer as input and returns a tuple containing the count of even and odd digits.
### Boundary values to test include: negative numbers, zero, numbers with only even digits, numbers with only odd digits, and numbers with mixed even and odd digits.
### STEP 2: PLAN - List test functions names and scenarios.
### Test functions:
### - test_negative_number
### - test_zero
### - test_all_even
### - test_all_odd
### - test_mixed
### STEP 3: CODE - Write the high-quality pytest suite.
###

# Focus: Type Scenarios
import pytest

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even = 0
    odd = 0
    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `even_odd_count` takes an integer as input and returns a tuple containing the count of even and odd digits.
### We need to test different scenarios to ensure the function correctly counts even and odd digits, including negative numbers and numbers with varying digit counts.
### STEP 2: PLAN - List test functions names and scenarios.
### Test functions:
### - test_positive_even_odd
### - test_positive_all_even
### - test_positive_all_odd
### STEP 3: CODE - Write the high-quality pytest suite.
### CODE:
def test_positive_even_odd():
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(2468) == (4, 0)
    assert even_odd_count(1357) == (0, 4)
    assert even_odd_count(123456789) == (4, 5)

def test_positive_all_even():
    assert even_odd_count(2468) == (4, 0)
    assert even_odd_count(2222) == (4, 0)
    assert even_odd_count(0) == (1, 0)

def test_positive_all_odd():
    assert even_odd_count(1357) == (0, 4)
    assert even_odd_count(1111) == (0, 4)
    assert even_odd_count(9) == (0, 1)

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
### We need to test different scenarios including positive numbers, negative numbers, and numbers with varying digit counts.
### The logic branches are based on whether a digit is even or odd.

### STEP 2: PLAN - List test functions names and scenarios.
### test_even_odd_count_positive
### test_even_odd_count_negative
### test_even_odd_count_zero
### test_even_odd_count_single_digit

### STEP 3: CODE - Write the high-quality pytest suite.
### CODE
def test_even_odd_count_positive():
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(246) == (3, 0)
    assert even_odd_count(13579) == (0, 5)

def test_even_odd_count_negative():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-246) == (3, 0)
    assert even_odd_count(-13579) == (0, 5)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_single_digit():
    assert even_odd_count(2) == (1, 0)
    assert even_odd_count(1) == (0, 1)