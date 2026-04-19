
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
            s = str(num)
            # First digit and last digit check
            if int(s[0]) % 2 != 0 and int(s[-1]) % 2 != 0:
                count += 1
    return count

@pytest.mark.parametrize("nums, expected", [
    # Provided examples
    ([15, -73, 14, -15], 1),
    ([33, -2, -3, 45, 21, 109], 2),
    
    # Edge Case: Empty list
    ([], 0),
    
    # Edge Case: No numbers greater than 10
    ([1, 3, 5, 7, 9, 10], 0),
    
    # Edge Case: Numbers > 10 but first digit even
    ([21, 43, 65, 87, 209], 0),
    
    # Edge Case: Numbers > 10 but last digit even
    ([12, 34, 56, 78, 100], 0),
    
    # Edge Case: Numbers > 10 but both digits even
    ([22, 44, 66, 88, 202], 0),
    
    # Edge Case: Negative numbers that would satisfy digit rules but fail > 10
    ([-11, -13, -31, -33, -101], 0),
    
    # Edge Case: Boundary value 11 (Smallest positive integer > 10 satisfying rules)
    ([11], 1),
    
    # Edge Case: Boundary value 10 (Should not be counted)
    ([10], 0),
    
    # Large numbers
    ([1000000001, 3000000007, 2000000001], 2),
    
    # Mixed list with various scenarios
    ([11, 12, 21, 22, 13, 31, 33, 10, 9, -11, 101, 102, 201], 5), 
    # Matches: 11, 13, 31, 33, 101
])
def test_special_filter(nums, expected):
    assert specialFilter(nums) == expected

def test_non_integer_floats():
    """
    Testing how the function handles floats. 
    Based on the problem description 'array of numbers', 
    if floats are passed, str(num) might include a decimal point.
    """
    # 11.1: > 10, first digit '1' (odd), last digit '1' (odd)
    # Note: The current implementation treats the last character of the string as the last digit.
    assert specialFilter([11.1]) == 1
    # 11.2: > 10, first digit '1' (odd), last digit '2' (even)
    assert specialFilter([11.2]) == 0