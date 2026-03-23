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
                if first_digit % 2 != 0 and last_digit % 2 != 0:
                    count += 1
    return count

@pytest.mark.parametrize("nums", [
    [11],  # Single element, boundary value (just above 10, odd digits)
    [9],   # Single element, below 10
    [10],  # Single element, equal to 10
    [12],  # Single element, just above 10, even last digit
    [21],  # Single element, odd first, even last
    [15],  # Single element, odd first and last
    [101], # Three digits, odd first and last
    [100], # Three digits, even last
    [111], # Three digits, all odd
    [112], # Three digits, odd first, even last
    [121], # Three digits, even first, odd last
])
def test_specialFilter_boundary_values(nums):
    assert specialFilter(nums) == pytest.param(
        0 if len(nums) == 1 and nums[0] <= 10 else (1 if len(nums) == 1 and nums[0] == 15 else (2 if nums == [33, -2, -3, 45, 21, 109] else (1 if nums == [15, -73, 14, -15] else 0))),
        marks=pytest.mark.xfail(reason="Incorrect expected value") if nums == [33, -2, -3, 45, 21, 109] else None
    )

# Focus: Equivalence Partitioning
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
            if num_str[0] in '13579' and num_str[-1] in '13579':
                count += 1
    return count

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function filters numbers based on two criteria:
# 1. Greater than 10
# 2. First and last digits are odd.
# Equivalence partitioning will focus on creating test cases that cover:
# - Numbers > 10 with odd first and last digits (valid)
# - Numbers > 10 with even first or last digits (invalid)
# - Numbers <= 10 (invalid)
# - Negative numbers (should work correctly due to abs())

# STEP 2: PLAN - List test functions names and scenarios.
# Test function 1: Valid numbers - numbers > 10 with odd first and last digits
# Test function 2: Invalid numbers - numbers > 10 with even first or last digits
# Test function 3: Boundary/Invalid numbers - numbers <= 10

# STEP 3: CODE - Write the high-quality pytest suite.

def test_valid_numbers():
    assert specialFilter([15, 33, 57, 79, 91, 109, 111]) == 6
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, 45, 21, 109]) == 2
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_invalid_numbers():
    assert specialFilter([12, 34, 56, 78, 90]) == 0
    assert specialFilter([21, 43, 65, 87, 10]) == 0
    assert specialFilter([10, 20, 30, 40, 50]) == 0
    assert specialFilter([14, 36, 58, 70, 92]) == 0

def test_boundary_and_invalid_numbers():
    assert specialFilter([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert specialFilter([-11, -12, -13, -14, -15]) == 0
    assert specialFilter([]) == 0
    assert specialFilter([11, 12, 13, 14, 15]) == 1

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
                if first_digit % 2 != 0 and last_digit % 2 != 0:
                    count += 1
    return count

def test_specialFilter_empty_array():
    assert specialFilter([]) == 0

def test_specialFilter_no_special_numbers():
    assert specialFilter([2, 4, 6, 8, 10]) == 0

def test_specialFilter_mixed_numbers():
    assert specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109]) == 4

def test_specialFilter_all_special_numbers():
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_specialFilter_negative_numbers():
    assert specialFilter([-11, -13, -15, -17, -19]) == 5

def test_specialFilter_single_special_number():
    assert specialFilter([15]) == 1

def test_specialFilter_single_non_special_number():
    assert specialFilter([12]) == 0

def test_specialFilter_large_numbers():
    assert specialFilter([1001, 1002, 1011, 1012]) == 2