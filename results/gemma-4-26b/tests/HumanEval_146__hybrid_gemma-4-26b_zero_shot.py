
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

def specialFilter(nums):
    """
    Counts numbers in a list that are greater than 10 and have 
    both an odd first digit and an odd last digit.
    """
    count = 0
    for n in nums:
        if n > 10:
            s = str(n)
            first_digit = int(s[0])
            last_digit = int(s[-1])
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
    return count

@pytest.mark.parametrize("nums, expected", [
    # --- Provided Examples ---
    ([15, -73, 14, -15], 1),          # 15 is > 10, starts with 1 (odd), ends with 5 (odd)
    ([33, -2, -3, 45, 21, 109], 2),   # 33 and 109 match; 45/21 have even first digits
    
    # --- Boundary Conditions (n > 10) ---
    ([], 0),                          # Empty list
    ([10], 0),                        # Exactly 10 (must be > 10)
    ([11], 1),                        # Smallest integer > 10 that matches (1, 1)
    ([12], 0),                        # Smallest integer > 10 that fails (1, 2)
    ([9], 0),                         # Single digit (must be > 10)
    ([0], 0),                         # Zero
    
    # --- Negative Numbers & Single Digits ---
    ([-11, -13, -15, -17, -19], 0),   # Odd digits, but values are < 10
    ([-73, -31], 0),                  # Negative values fail the > 10 check
    ([1, 3, 5, 7, 9], 0),             # Odd digits but not > 10
    ([0, -1, -11], 0),                # Zero and negatives
    
    # --- First Digit Logic ---
    ([21, 23, 45, 67, 89], 0),        # All have even first digits
    ([11, 31, 51, 71, 91], 5),        # All have odd first digits and odd last digits
    ([11, 13, 21, 31, 41, 51], 4),    # Mixed parity first digits (11, 13, 31, 51 match)
    
    # --- Last Digit Logic ---
    ([12, 14, 16, 18, 30, 32], 0),    # All have even last digits
    ([11, 33, 55, 77, 99], 5),        # All have odd last digits and odd first digits
    
    # --- Mixed Digit Logic ---
    ([22, 44, 66, 88], 0),            # Both even
    ([12, 21, 43, 34], 0),            # One odd, one even
    
    # --- Middle Digit Logic (Should not affect result) ---
    ([101, 121, 141, 161, 181], 5),   # Middle digits are even
    ([133, 353, 575, 797, 919], 5),   # Middle digits are odd
    ([1000000001, 3000000003], 2),    # Large numbers with many zeros
    
    # --- Large Numbers ---
    ([1000000000000000000001, 9999999999999999999999], 2),
    ([2000000000000000000001, 1000000000000000000002], 0),
    ([200000000000000000002, 100000000000000000004], 0), # Large numbers with even ends
])
def test_special_filter(nums, expected):
    """
    Comprehensive test covering boundaries, negative numbers, 
    digit parity, and large integers.
    """
    assert specialFilter(nums) == expected

def test_type_consistency():
    """
    Ensures the function always returns an integer.
    """
    assert isinstance(specialFilter([11, 13, 15]), int)
    assert isinstance(specialFilter([]), int)
    assert isinstance(specialFilter([0, -10, 5]), int)