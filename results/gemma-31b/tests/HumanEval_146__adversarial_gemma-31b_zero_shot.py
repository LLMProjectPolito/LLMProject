
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
    for n in nums:
        if n > 10:
            s = str(abs(n))
            if int(s[0]) % 2 != 0 and int(s[-1]) % 2 != 0:
                count += 1
    return count

@pytest.mark.parametrize("nums, expected", [
    # Provided examples
    ([15, -73, 14, -15], 1),
    ([33, -2, -3, 45, 21, 109], 2),
    
    # Edge Case: Empty list
    ([], 0),
    
    # Edge Case: Numbers exactly 10 or below (should be excluded)
    ([10, 9, 1, -11, -15], 0),
    
    # Edge Case: First digit even, last digit odd
    ([21, 43, 65, 87, 201], 0),
    
    # Edge Case: First digit odd, last digit even
    ([12, 34, 56, 78, 102], 0),
    
    # Edge Case: Both digits even
    ([22, 44, 66, 88, 202], 0),
    
    # Edge Case: Both digits odd (Positive matches)
    ([11, 13, 31, 33, 55, 77, 99], 7),
    
    # Edge Case: Large numbers
    ([1000000001, 3000000007, 2000000001], 2),
    
    # Edge Case: Numbers with zeros in the middle
    ([101, 103, 1001, 3003], 4),
    ([100, 300, 500], 0),
    
    # Mixed scenario
    ([11, 12, 21, 22, 101, 102, 201, 202, -11, 10], 2), # 11 and 101
])
def test_special_filter(nums, expected):
    assert specialFilter(nums) == expected

def test_non_integer_types():
    """
    Test how the function handles floats that satisfy the condition.
    Depending on implementation, str(11.0) might fail or behave differently.
    This ensures robustness against numeric types.
    """
    # 11.0 is > 10, first digit '1' (odd), last digit '0' (even) -> 0
    # 11.1 is > 10, first digit '1' (odd), last digit '1' (odd) -> 1
    # Note: The problem specifies 'digits', usually implying integers.
    # If the function is strictly for ints, this is a boundary test.
    try:
        assert specialFilter([11.1]) == 1
    except (ValueError, IndexError):
        pytest.fail("specialFilter failed to handle float input gracefully")