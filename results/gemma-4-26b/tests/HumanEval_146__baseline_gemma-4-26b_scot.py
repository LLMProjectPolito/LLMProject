
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

@pytest.mark.parametrize("input_nums, expected", [
    # Provided examples
    ([15, -73, 14, -15], 1),
    ([33, -2, -3, 45, 21, 109], 2),
    
    # Empty and small lists
    ([], 0),
    ([1, 3, 5, 7, 9], 0),  # Single digits < 10
    ([10, 11, 12], 1),     # 10 is not > 10; 11 is valid; 12 is invalid
    
    # Negative numbers (must be > 10)
    ([-11, -13, -15, -31, -33], 0),
    
    # Digit logic: First digit even, Last digit odd
    ([21, 43, 65, 87, 200001], 0),
    
    # Digit logic: First digit odd, Last digit even
    ([12, 34, 56, 78, 100002], 0),
    
    # Digit logic: Both even
    ([22, 44, 66, 88], 0),
    
    # All valid (Odd first, Odd last, > 10)
    ([11, 13, 31, 33, 55, 77, 99, 101, 135, 999], 10),
    
    # Large numbers
    ([1000000001, 3000000007, 2000000001], 2),
])
def test_special_filter_scenarios(input_nums, expected):
    """
    Tests various scenarios including provided examples, boundary conditions,
    digit parity combinations, and negative numbers.
    """
    assert specialFilter(input_nums) == expected

def test_special_filter_type_consistency():
    """
    Ensure the function returns an integer.
    """
    result = specialFilter([11, 13, 15])
    assert isinstance(result, int)

def test_special_filter_large_input():
    """
    Test with a larger range of numbers to ensure performance and correctness.
    """
    # Create a list of 1000 numbers: 11, 13, 15... 2009
    # We want to count how many are > 10 and have odd first/last digits.
    # In the range 11-199, numbers starting with 1 (odd) and ending in 1,3,5,7,9 (odd)
    # are 11, 13, 15, 17, 19 (5 numbers)
    # In the range 100-199, numbers starting with 1 (odd) and ending in 1,3,5,7,9 (odd)
    # are 101, 103, 105, 107, 109, 111... 199 (10 * 5 = 50 numbers)
    nums = list(range(1, 200))
    # Manual calculation for 1-199:
    # 11, 13, 15, 17, 19 (5)
    # 31, 33, 35, 37, 39 (5)
    # 51, 53, 55, 57, 59 (5)
    # 71, 73, 75, 77, 79 (5)
    # 91, 93, 95, 97, 99 (5)
    # 101, 103, 105, 107, 109 (5)
    # 111, 113, 115, 117, 119 (5)
    # 121... (no, 121 starts with 1, ends with 1, but 121 is valid)
    # Wait, the rule is FIRST digit and LAST digit.
    # For 100-199, the first digit is ALWAYS 1 (odd).
    # So we just need the last digit to be odd.
    # In every 10 numbers (e.g., 100-109), there are 5 odd last digits.
    # There are 10 such sets in 100-199. 10 * 5 = 50.
    # Total = 5 (from 11-99) + 50 (from 100-199) = 55.
    # Let's verify:
    # 11, 13, 15, 17, 19 (5)
    # 31, 33, 35, 37, 39 (5)
    # 51, 53, 55, 57, 59 (5)
    # 71, 73, 75, 77, 79 (5)
    # 91, 93, 95, 97, 99 (5)
    # 101, 103, 105, 107, 109 (5)
    # 111, 113, 115, 117, 119 (5)
    # 121, 123, 125, 127, 129 (5)
    # 131, 133, 135, 137, 139 (5)
    # 141, 143, 145, 147, 149 (5)
    # 151, 153, 155, 157, 159 (5)
    # 161, 163, 165, 167, 169 (5)
    # 171, 173, 175, 177, 179 (5)
    # 181, 183, 185, 187, 189 (5)
    # 191, 193, 195, 197, 199 (5)
    # Total = 5*3 + 5*10 = 15 + 50 = 65? No.
    # 11-19 (5), 31-39 (5), 51-59 (5), 71-79 (5), 91-99 (5) -> 25
    # 101-199 (50)
    # 25 + 50 = 75.
    
    # Let's use a simpler verification for the test:
    # Just check if the count is correct for a known set.
    expected_count = 0
    for n in nums:
        if n > 10:
            s = str(n)
            if int(s[0]) % 2 != 0 and int(s[-1]) % 2 != 0:
                expected_count += 1
    
    assert specialFilter(nums) == expected_count