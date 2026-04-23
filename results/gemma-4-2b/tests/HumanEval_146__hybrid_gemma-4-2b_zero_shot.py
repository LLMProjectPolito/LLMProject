
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
        num_str = str(abs(num))  # Handle negative numbers
        if num > 10 and num_str[0] in '13579' and num_str[-1] in '13579':
            count += 1
    return count

@pytest.mark.parametrize("nums, expected", [
    ([15, -73, 14, -15], 1),
    ([33, -2, -3, 45, 21, 109], 2),
    ([1, 3, 5, 7, 9], 0),
    ([10, 12, 14, 16], 0),
    ([-1, -3, -5, -7, -9], 0),
    ([11, 13, 15, 17, 19], 5),
    ([-11, -13, -15, -17, -19], 0),
    ([1, 11, 111, 1111], 4),
    ([-1, -11, -111, -1111], 0),
    ([100, 101, 102], 1),
    ([1000, 1001, 1002], 1),
    ([-100, -101, -102], 1),
    ([123, 456, 789], 0),
    ([123, 456, 789, 11], 0),
    ([11111, 22222, 33333], 3),
    ([-11111, -22222, -33333], 0),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 0),
    ([15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109], 2),
    ([-15, -17, -19, -21, -23, -25, -27, -29, -31, -33, -35, -37, -39, -41, -43, -45, -47, -49, -51, -53, -55, -57, -59, -61, -63, -65, -67, -69, -71, -73, -75, -77, -79, -81, -83, -85, -87, -89, -91, -93, -95, -97, -99, -101, -103, -105, -107, -109], 0)
])
def test_special_filter(nums, expected):
    assert specialFilter(nums) == expected

@pytest.mark.parametrize("nums", [
    [],
    [10],
    [-10],
    [1, 2, 3],
    [-1, -2, -3],
    [11, 12, 13],
    [-11, -12, -13],
    [1, 11, 111, 1111],
    [-1, -11, -111, -1111]
])
def test_empty_array(nums):
    assert specialFilter(nums) == 0

@pytest.mark.parametrize("nums", [
    [15, 33, 45, 109, 121],
    [-15, -33, -45, -109, -121],
    [15, 33, 45, 109, -121],
    [-15, -33, -45, -109, 121],
    [1, 11, 111, 1111],
    [-1, -11, -111, -1111]
])
def test_negative_numbers(nums):
    assert specialFilter(nums) == 0