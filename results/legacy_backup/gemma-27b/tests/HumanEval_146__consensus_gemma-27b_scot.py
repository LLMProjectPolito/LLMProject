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

# STEP 2: PLAN
# Test function names and scenarios:
# - test_empty_array: Test with an empty array.
# - test_no_special_numbers: Test with an array containing no special numbers.
# - test_single_special_number: Test with an array containing a single special number.
# - test_multiple_special_numbers: Test with an array containing multiple special numbers.
# - test_negative_numbers: Test with an array containing negative numbers.
# - test_numbers_less_than_or_equal_to_10: Test with numbers less than or equal to 10.
# - test_mixed_numbers: Test with a mix of special and non-special numbers.
# - test_large_numbers: Test with large numbers.
# - test_zero: Test with zero.
# - test_single_digit_numbers: Test with single digit numbers.

@pytest.mark.parametrize("nums, expected", [
    ([], 0),
    ([2, 4, 6, 8, 10], 0),
    ([15], 1),
    ([15, 33, 55], 3),
    ([-73, -11, -13], 0),
    ([1, 3, 5, 7, 9], 0),
    ([15, 22, 33, 44, 55], 2),
    ([1001, 1003, 1005], 3),
    ([0], 0),
    ([1, 3, 5, 11, 13, 15], 3),
    ([12345, 54321, 98765], 2),
    ([-15, 15], 1),
    ([11, 33, 55, 77, 99], 5),
    ([12, 34, 56, 78, 90], 0),
    ([111], 1),
    ([10, 11, 12, 13, 14, 15], 2),
    ([-15, -33, -55], 0),
    ([15, -73, 14, -15], 1),
    ([11, 22, 33, 44, 55], 2),
    ([101, 111, 121, 131], 4)
])
def test_specialFilter(nums, expected):
    assert specialFilter(nums) == expected