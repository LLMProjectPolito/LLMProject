
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
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10:
            num_str = str(abs(num))
            if int(num_str[0]) % 2 != 0 and int(num_str[-1]) % 2 != 0:
                count += 1
    return count

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([15, -73, 14, -15], 1),
        ([33, -2, -3, 45, 21, 109], 2),
        ([11, 33, 55, 77, 99], 5),
        ([-11, -33, -55, -77, -99], 0),
        ([1, 3, 5, 7, 9], 0),
        ([13, 35, 57, 79, 91], 5),
        ([12, 14, 16, 18, 20], 0),
        ([-12, -14, -16, -18, -20], 0),
        ([10, 11, 12, 13], 2),
        ([-10, -11, -12, -13], 2),
        ([], 0),
        ([100, 101, 103, 105, 107, 109], 6),
        ([-100, -101, -103, -105, -107, -109], 0),
        ([15, 33, 55, 77, 99, 111, 133, 155, 177, 199], 10),
        ([-15, -33, -55, -77, -99, -111, -133, -155, -177, -199], 0),
        ([11, 13, 15, 17, 19, 33, 35, 37, 39, 55, 57, 59, 77, 79, 99, 101, 103, 105, 107, 109], 20),
        ([-11, -13, -15, -17, -19, -33, -35, -37, -39, -55, -57, -59, -77, -79, -99, -101, -103, -105, -107, -109], 0)
    ],
)
def test_specialFilter(nums, expected):
    assert specialFilter(nums) == expected