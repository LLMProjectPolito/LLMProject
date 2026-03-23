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
                if first_digit % 2 != 0 and last_digit % 2 != 0:
                    count += 1
    return count

@pytest.mark.parametrize("nums", [[15, -73, 14, -15], [33, -2, -3, 45, 21, 109], [11, 22, 33, 44, 55], [-11, -22, -33, -44, -55]])
def test_specialFilter_edge_case():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([11, 22, 33, 44, 55]) == 0
    assert specialFilter([-11, -22, -33, -44, -55]) == 0

def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

@pytest.mark.parametrize("nums, expected", [
    ([15, -73, 14, -15], 1),
    ([33, -2, -3, 45, 21, 109], 2),
    ([-11, -13, -15], 0),
    ([11, 13, 15], 0),
    ([111, 133, 155], 0),
    ([1111, 1333, 1555], 0),
    ([11111, 13333, 15555], 0),
    ([111111, 133333, 155555], 0),
    ([1111111, 1333333, 1555555], 0),
    ([11111111, 13333333, 15555555], 0),
    ([111111111, 133333333, 155555555], 0),
    ([11, 13, 15, 17, 19], 5),
    ([-11, -13, -15, -17, -19], 5),
    ([11, 13, 15, 17, 19, -11, -13, -15, -17, -19], 5),
    ([11, 13, 15, 17, 19, -11, -13, -15, -17, -19, 111, 133, 155], 3),
])
def test_specialFilter(nums, expected):
    assert specialFilter(nums) == expected