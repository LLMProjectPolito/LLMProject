# STEP 1: REASONING
# The function `specialFilter` counts numbers in a list that meet two criteria:
# 1. The number is greater than 10.
# 2. Both the first and last digits of the number are odd.
# We need to test various scenarios, including:
# - Positive and negative numbers.
# - Numbers with multiple digits.
# - Numbers that satisfy both criteria.
# - Numbers that satisfy only one criterion.
# - Numbers that satisfy neither criterion.
# - Empty list.
# - List with numbers less than or equal to 10.
# - Numbers with leading zeros (should be handled correctly).

# STEP 2: PLAN
# 1. test_empty_list: Test with an empty list.
# 2. test_no_special_numbers: Test with a list containing no special numbers.
# 3. test_single_special_number: Test with a list containing a single special number.
# 4. test_multiple_special_numbers: Test with a list containing multiple special numbers.
# 5. test_mixed_numbers: Test with a list containing special and non-special numbers.
# 6. test_negative_numbers: Test with negative numbers, including special and non-special.
# 7. test_numbers_less_than_or_equal_to_10: Test with numbers less than or equal to 10.
# 8. test_large_numbers: Test with large numbers to ensure digit extraction works correctly.
# 9. test_leading_zeros: Test with numbers that have leading zeros (e.g., 015).

# STEP 3: CODE
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
            num_str = str(abs(num))  # Handle negative numbers
            if len(num_str) > 0:
                first_digit = int(num_str[0])
                last_digit = int(num_str[-1])
                if first_digit % 2 != 0 and last_digit % 2 != 0:
                    count += 1
    return count

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_special_numbers():
    assert specialFilter([2, 4, 6, 8, 10]) == 0

def test_single_special_number():
    assert specialFilter([15]) == 1

def test_multiple_special_numbers():
    assert specialFilter([15, 33, 55, 77, 99]) == 5

def test_mixed_numbers():
    assert specialFilter([15, 2, 33, 4, 55, 6]) == 3

def test_negative_numbers():
    assert specialFilter([-15, -33, -2, -4, -55, -6]) == 2

def test_numbers_less_than_or_equal_to_10():
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0

def test_large_numbers():
    assert specialFilter([12345, 13579, 97531]) == 2

def test_leading_zeros():
    assert specialFilter([15, 015, 109]) == 2