
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

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
            s = str(num)
            if int(s[0]) % 2 != 0 and int(s[-1]) % 2 != 0:
                count += 1
    return count

import pytest

@pytest.mark.parametrize("nums, expected", [
    # Provided examples
    ([15, -73, 14, -15], 1),
    ([33, -2, -3, 45, 21, 109], 2),
    
    # Edge cases: Empty and small lists
    ([], 0),
    ([10], 0), # Exactly 10 should be excluded (must be > 10)
    ([11], 1), # Smallest valid number
    
    # Negative numbers (should be excluded because they are not > 10)
    ([-11, -13, -15], 0),
    ([-15, 15], 1),
    
    # Numbers > 10 but failing digit checks
    ([21], 0),     # First digit even
    ([12], 0),     # Last digit even
    ([22], 0),     # Both digits even
    ([45], 0),     # First digit even
    ([10], 0),     # Not > 10 and last digit even
    
    # Numbers > 10 passing digit checks
    ([11, 13, 15, 17, 19], 5),
    ([31, 33, 35, 37, 39], 5),
    ([51, 53, 55, 57, 59], 5),
    ([71, 73, 75, 77, 79], 5),
    ([91, 93, 95, 97, 99], 5),
    
    # Multi-digit numbers
    ([101], 1),    # Odd first (1), Odd last (1)
    ([102], 0),    # Odd first (1), Even last (2)
    ([201], 0),    # Even first (2), Odd last (1)
    ([1001], 1),   # Odd first (1), Odd last (1)
    ([3007], 1),   # Odd first (3), Odd last (7)
    ([9999], 1),   # Odd first (9), Odd last (9)
    
    # Mixed case
    ([11, 22, 33, 44, 55, 66, 77, 88, 99], 5), # 11, 33, 55, 77, 99
    ([109, 209, 309, 409], 2), # 109 and 309
])
def test_specialFilter(nums, expected):
    assert specialFilter(nums) == expected