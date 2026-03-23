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
# STEP 1: REASONING - The function `specialFilter` counts the number of elements in a list that are greater than 10 and have both their first and last digits as odd numbers. We need to test various scenarios including positive and negative numbers, numbers greater than 10, numbers less than or equal to 10, and cases where the first or last digit is not odd.

# STEP 2: PLAN -
# Test cases:
# 1. Empty list
# 2. List with no numbers greater than 10
# 3. List with some numbers greater than 10 and satisfying the condition
# 4. List with some numbers greater than 10 but not satisfying the condition
# 5. List with negative numbers
# 6. List with zero
# 7. List with a single number
# 8. List with duplicate numbers
# 9. List with a mix of positive and negative numbers

# Test function names:
# test_empty_list
# test_no_numbers_greater_than_10
# test_some_numbers_greater_than_10_and_valid
# test_some_numbers_greater_than_10_but_invalid
# test_negative_numbers
# test_zero
# test_single_number
# test_duplicate_numbers
# test_mixed_positive_and_negative_numbers


# STEP 3: CODE -
###
def test_empty_list():
    assert specialFilter([]) == 0

def test_no_numbers_greater_than_10():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_some_numbers_greater_than_10_and_valid():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_some_numbers_greater_than_10_but_invalid():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_negative_numbers():
    assert specialFilter([-15, -33, -73]) == 0

def test_zero():
    assert specialFilter([0, 10, 11]) == 0

def test_single_number():
    assert specialFilter([15]) == 1

def test_duplicate_numbers():
    assert specialFilter([15, 15, 15]) == 3

def test_mixed_positive_and_negative_numbers():
    assert specialFilter([-15, 15, -33, 33, -73, 73]) == 2

def test_large_numbers():
    assert specialFilter([1111111111, 1333333333]) == 2

def test_edge_cases():
    assert specialFilter([11, 12, 13]) == 0
    assert specialFilter([11, 13, 15]) == 2
    assert specialFilter([-11, -13, -15]) == 0