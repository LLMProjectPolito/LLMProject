
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
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    """
    count = 0
    for num in nums:
        if num > 10:
            s_num = str(num)
            # First digit and last digit check
            if int(s_num[0]) % 2 != 0 and int(s_num[-1]) % 2 != 0:
                count += 1
    return count

@pytest.mark.parametrize("input_list, expected", [
    # --- Provided Examples ---
    ([15, -73, 14, -15], 1),        # 15 is > 10, 1 and 5 are odd
    ([33, -2, -3, 45, 21, 109], 2), # 33 and 109 fit criteria
    
    # --- Boundary Cases for Value > 10 ---
    ([], 0),                        # Empty list
    ([10], 0),                      # Exactly 10 (must be > 10)
    ([11], 1),                      # Just above 10, both digits odd
    ([9], 0),                       # Single digit odd number (must be > 10)
    ([0], 0),                       # Zero
    
    # --- Negative Numbers ---
    # Should always be excluded as they are < 10
    ([-11, -13, -15, -31], 0),
    ([-101], 0),
    
    # --- Digit Logic (Odd/Even Combinations) ---
    ([12], 0),                      # First odd, last even
    ([21], 0),                      # First even, last odd
    ([22], 0),                      # Both even
    ([13], 1),                      # Both odd
    ([21, 23, 41, 47, 63, 69, 81, 85], 0), # All first digit even
    ([12, 14, 30, 32, 56, 58, 74, 90], 0), # All last digit even
    
    # --- Large Numbers & Mixed Lengths ---
    ([10001], 1),                   # First 1, Last 1 (Both odd)
    ([30007], 1),                   # First 3, Last 7 (Both odd)
    ([20009], 0),                   # First 2 (Even)
    ([10008], 0),                   # Last 8 (Even)
    ([55555], 1),                   # All odd
    ([1000000001, 3000000007, 5000000009], 3),
    
    # --- Mixed Lists ---
    ([11, 13, 15, 17, 19], 5),      # All match
    ([20, 40, 60, 80], 0),          # None match
    ([101, 202, 303, 404], 2),      # 101 and 303 match
    ([11, 12, 21, 22, 101, 102, 201, 202, 303], 3), # 11, 101, 303
    ([11, 33, 55, 77, 99, 101, 303, 505, 707, 909], 10),
])
def test_special_filter(input_list, expected):
    assert specialFilter(input_list) == expected

def test_special_filter_non_integers():
    """
    Tests how the function handles floats.
    Based on str() conversion: 11.1 -> '11.1'. First '1' (odd), Last '1' (odd).
    """
    assert specialFilter([11.1]) == 1 
    assert specialFilter([11.2]) == 0