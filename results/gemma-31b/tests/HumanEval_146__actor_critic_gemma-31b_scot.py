
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

# The function is assumed to be defined as:
# def specialFilter(nums):
#     count = 0
#     for num in nums:
#         if num > 10:
#             s = str(num)
#             if int(s[0]) % 2 != 0 and int(s[-1]) % 2 != 0:
#                 count += 1
#     return count

def test_provided_examples():
    """Test the examples provided in the problem description."""
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_empty_list():
    """Test that an empty list returns 0."""
    assert specialFilter([]) == 0

def test_boundary_conditions():
    """Test numbers around the threshold of 10."""
    # 9: odd/odd but not > 10
    # 10: > 10 is false, and 0 is even
    # 11: > 10, first 1 (odd), last 1 (odd) -> Match
    assert specialFilter([9, 10, 11]) == 1

def test_negative_numbers():
    """Test that negative numbers are excluded regardless of digits."""
    # -11: first digit '1' (odd), last '1' (odd), but not > 10
    # -13: first digit '1' (odd), last '3' (odd), but not > 10
    assert specialFilter([-11, -13, -15, -17, -19]) == 0

def test_digit_combinations():
    """Test various combinations of first and last digits for numbers > 10."""
    # 11: Odd/Odd -> Match
    # 12: Odd/Even -> No Match
    # 21: Even/Odd -> No Match
    # 22: Even/Even -> No Match
    # 33: Odd/Odd -> Match
    # 43: Even/Odd -> No Match
    # 54: Odd/Even -> No Match
    # 77: Odd/Odd -> Match
    nums = [11, 12, 21, 22, 33, 43, 54, 77]
    assert specialFilter(nums) == 3

def test_large_numbers():
    """Test numbers with multiple digits to ensure first/last extraction."""
    # 1001: First 1 (odd), Last 1 (odd) -> Match
    # 1002: First 1 (odd), Last 2 (even) -> No Match
    # 2001: First 2 (even), Last 1 (odd) -> No Match
    # 3005: First 3 (odd), Last 5 (odd) -> Match
    # 4004: First 4 (even), Last 4 (even) -> No Match
    assert specialFilter([1001, 1002, 2001, 3005, 4004]) == 2

def test_no_matches():
    """Test a list where no elements satisfy the criteria."""
    # All either <= 10 or have an even digit at start/end
    nums = [2, 4, 6, 8, 10, 21, 12, 22, 44, 66]
    assert specialFilter(nums) == 0

@pytest.mark.parametrize("input_list, expected", [
    ([11, 13, 15, 17, 19], 5),      # All match
    ([21, 32, 43, 54], 0),          # Mixed failures
    ([101, 303, 505, 707, 909], 5), # Large odd/odd
    ([100, 200, 300], 0),           # End in zero (even)
])
def test_parametrized_cases(input_list, expected):
    """Additional parametrized test cases for robustness."""
    assert specialFilter(input_list) == expected