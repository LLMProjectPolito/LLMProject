
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
        num_str = str(abs(num))
        if num > 10 and num_str[0] in '13579' and num_str[-1] in '13579':
            count += 1
    return count

@pytest.mark.parametrize(
    "nums, expected",
    [
        (
            [],
            0,
        ),
        (
            [15, -73, 14, -15],
            1,
        ),
        (
            [33, -2, -3, 45, 21, 109],
            2,
        ),
        (
            [11, 13, 15, 17, 19],
            5,
        ),
        (
            [-11, -13, -15, -17, -19],
            5,
        ),
        (
            [12, 34, 56, 78, 90],
            0,
        ),
        (
            [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            5,
        ),
        (
            [100, 101, 102, 103],
            2,
        ),
        (
            [0],
            0,
        ),
        (
            [10],
            0,
        ),
        (
            [11],
            1,
        ),
        (
            [13],
            1,
        ),
        (
            [15],
            1,
        ),
        (
            [17],
            1,
        ),
        (
            [19],
            1,
        ),
        (
            [109],
            1,
        ),
        (
            [-109],
            1,
        ),
        (
            [11111],
            5,
        ),
        (
            [-11111],
            5,
        ),
        (
            [135791],
            5,
        ),
        (
            [-135791],
            5,
        ),
    ],
)
def test_special_filter(nums, expected):
    assert specialFilter(nums) == expected