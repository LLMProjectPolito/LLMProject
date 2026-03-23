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

# STEP 1: REASONING
# The function `specialFilter` counts numbers in a list that meet specific criteria:
# 1. The number must be greater than 10.
# 2. The first and last digits of the number (when considered as a string) must be odd (1, 3, 5, 7, or 9).
# The function handles both positive and negative numbers by taking the absolute value before converting to a string.

# STEP 2: PLAN
# Test Cases:
# 1. Empty list: Should return 0.
# 2. List with no matching numbers: Should return 0.
# 3. List with one matching number: Should return 1.
# 4. List with multiple matching numbers: Should return the correct count.
# 5. List with negative numbers: Should handle negative numbers correctly.
# 6. List with numbers close to 10: Should correctly identify numbers greater than 10.
# 7. List with numbers having even first or last digits: Should not count these numbers.
# 8. List with a mix of positive, negative, and zero values.
# 9. List with large numbers.

# Test Function Names:
# - test_empty_list
# - test_no_matching_numbers
# - test_one_matching_number
# - test_multiple_matching_numbers
# - test_negative_numbers
# - test_numbers_close_to_10
# - test_even_digits
# - test_mixed_values
# - test_large_numbers

# STEP 3: CODE
def test_empty_list():
    assert specialFilter([]) == 0

def test_no_matching_numbers():
    assert specialFilter([2, 4, 6, 8, 10]) == 0

def test_one_matching_number():
    assert specialFilter([15, 2, 4, 6, 8]) == 1

def test_multiple_matching_numbers():
    assert specialFilter([15, 33, 57, 79, 91]) == 5

def test_negative_numbers():
    assert specialFilter([-15, -33, -57, -79, -91]) == 5

def test_numbers_close_to_10():
    assert specialFilter([9, 11, 13, 15]) == 3

def test_even_digits():
    assert specialFilter([12, 34, 56, 78, 90]) == 0

def test_mixed_values():
    assert specialFilter([15, -73, 14, -15, 21, 0, 10]) == 2

def test_large_numbers():
    assert specialFilter([1001, 12345, 13579, 97531]) == 2

def test_example_1():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_example_2():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_single_digit_odd():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_two_digit_odd_first_even_last():
    assert specialFilter([12, 34, 56, 78, 90]) == 0

def test_two_digit_even_first_odd_last():
    assert specialFilter([21, 43, 65, 87, 09]) == 0