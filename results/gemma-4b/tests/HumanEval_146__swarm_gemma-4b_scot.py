
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest
import math

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
                if (first_digit % 2 != 0 and last_digit % 2 != 0):
                    count += 1
    return count
    
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([11, 13, 15, 17, 19], 5),
        ([-11, -13, -15, -17, -19], 0),
        ([11, 13, 15, 17, 19, 21], 5),
        ([11, 13, 15, 17, 19, 23], 5),
        ([11, 13, 15, 17, 19, 25], 5),
        ([11, 13, 15, 17, 19, 27], 5),
        ([11, 13, 15, 17, 19, 29], 5),
        ([11, 13, 15, 17, 19, 31], 5),
        ([11, 13, 15, 17, 19, 33], 5),
        ([11, 13, 15, 17, 19, 35], 5),
        ([11, 13, 15, 17, 19, 37], 5),
        ([11, 13, 15, 17, 19, 39], 5),
        ([11, 13, 15, 17, 19, 41], 0),
        ([11, 13, 15, 17, 19, 43], 0),
        ([11, 13, 15, 17, 19, 45], 0),
        ([11, 13, 15, 17, 19, 47], 0),
        ([11, 13, 15, 17, 19, 49], 0),
        ([11, 13, 15, 17, 19, 51], 0),
        ([11, 13, 15, 17, 19, 53], 0),
        ([11, 13, 15, 17, 19, 55], 0),
        ([11, 13, 15, 17, 19, 57], 0),
        ([11, 13, 15, 17, 19, 59], 0),
        ([11, 13, 15, 17, 19, 61], 0),
        ([11, 13, 15, 17, 19, 63], 0),
        ([11, 13, 15, 17, 19, 65], 0),
        ([11, 13, 15, 17, 19, 67], 0),
        ([11, 13, 15, 17, 19, 69], 0),
        ([11, 13, 15, 17, 19, 71], 0),
        ([11, 13, 15, 17, 19, 73], 0),
        ([11, 13, 15, 17, 19, 75], 0),
        ([11, 13, 15, 17, 19, 77], 0),
        ([11, 13, 15, 17, 19, 79], 0),
        ([11, 13, 15, 17, 19, 81], 0),
        ([11, 13, 15, 17, 19, 83], 0),
        ([11, 13, 15, 17, 19, 85], 0),
        ([11, 13, 15, 17, 19, 87], 0),
        ([11, 13, 15, 17, 19, 89], 0),
        ([11, 13, 15, 17, 19, 91], 0),
        ([11, 13, 15, 17, 19, 93], 0),
        ([11, 13, 15, 17, 19, 95], 0),
        ([11, 13, 15, 17, 19, 97], 0),
        ([11, 13, 15, 17, 19, 99], 0),
    ]
)
def test_specialFilter():
    pass