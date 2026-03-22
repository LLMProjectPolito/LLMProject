import pytest
import math


# Focus: Boundary Values
import pytest

def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10:
            num_str = str(abs(num))
            if len(num_str) > 0:
                first_digit = int(num_str[0])
                last_digit = int(num_str[-1])
                if (first_digit % 2 != 0 and last_digit % 2 != 0):
                    count += 1
    return count

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `specialFilter` counts numbers greater than 10 where both the first and last digits are odd.
### Boundary values to test include:
###   - Numbers less than or equal to 10.
###   - Numbers greater than 10 with first and last digits both odd.
###   - Numbers greater than 10 with first digit odd and last digit even.
###   - Numbers greater than 10 with first digit even and last digit odd.
###   - Numbers greater than 10 with first and last digits both even.
###   - Empty input list.
###   - List with only negative numbers.
### STEP 2: PLAN - List test functions names and scenarios.
### test_specialFilter_empty_list
### test_specialFilter_negative_numbers
### test_specialFilter_boundary_values
### STEP 3: CODE - Write the high-quality pytest suite.

def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_negative_numbers():
    assert specialFilter([-11, -13, -15]) == 0

def test_specialFilter_boundary_values():
    assert specialFilter([11, 13, 15, 17, 19]) == 5
    assert specialFilter([11, 12, 13, 14, 15]) == 1
    assert specialFilter([11, 12, 13, 14, 16]) == 0
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

# Focus: Type Scenarios
import pytest

def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10:
            num_str = str(abs(num))
            if len(num_str) > 0:
                first_digit = int(num_str[0])
                last_digit = int(num_str[-1])
                if (first_digit % 2 != 0 and last_digit % 2 != 0):
                    count += 1
    return count

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `specialFilter` counts numbers greater than 10 where both the first and last digits are odd.
### We need to test different types of input arrays, including empty arrays, arrays with only valid numbers, arrays with invalid numbers, and arrays with mixed valid and invalid numbers.
### STEP 2: PLAN - List test functions names and scenarios.
### test_specialFilter_empty_array
### test_specialFilter_valid_numbers
### test_specialFilter_invalid_numbers
### STEP 3: CODE - Write the high-quality pytest suite.

def test_specialFilter_empty_array():
    assert specialFilter([]) == 0

def test_specialFilter_valid_numbers():
    assert specialFilter([15, 33, 45, 109]) == 4

def test_specialFilter_invalid_numbers():
    assert specialFilter([14, -73, -15]) == 0

def test_specialFilter_mixed_numbers():
    assert specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109]) == 2

# Focus: Logic Branches
import pytest

def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10:
            num_str = str(abs(num))
            if len(num_str) > 0:
                first_digit = int(num_str[0])
                last_digit = int(num_str[-1])
                if (first_digit % 2 != 0 and last_digit % 2 != 0):
                    count += 1
    return count

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `specialFilter` counts numbers greater than 10 where both the first and last digits are odd.
### We need to test cases where the condition is met, not met, and edge cases like empty input or numbers with only one digit.
### STEP 2: PLAN - List test functions names and scenarios.
### test_specialFilter_positive_cases
### test_specialFilter_negative_cases
### test_specialFilter_empty_list
### STEP 3: CODE - Write the high-quality pytest suite.

def test_specialFilter_positive_cases():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([11, 13, 15, 17, 19]) == 5
    assert specialFilter([111, 133, 155, 177, 199]) == 5
    assert specialFilter([1111, 1333, 1555, 1777, 1999]) == 5

def test_specialFilter_negative_cases():
    assert specialFilter([12, 14, 16, 18]) == 0
    assert specialFilter([-15, -73, -14, -15]) == 0
    assert specialFilter([10, 12, 14, 16]) == 0
    assert specialFilter([21, 23, 25, 27, 29]) == 0
    assert specialFilter([111, 133, 155, 177, 199, 200]) == 3

def test_specialFilter_empty_list():
    assert specialFilter([]) == 0