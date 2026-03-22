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

@pytest.mark.parametrize("nums, expected", [
    ([15, -73, 14, -15], 1),
    ([33, -2, -3, 45, 21, 109], 2),
    ([-11, -13, -15], 0),
    ([11, 13, 15], 0),
    ([111, 131, 151], 0),
    ([1111, 1313, 1515], 0),
    ([11111, 13131, 15151], 0),
    ([111111, 131313, 151515], 0),
    ([1111111, 1313131, 1515151], 0),
    ([11111111, 13131313, 15151515], 0),
    ([111111111, 131313131, 151515151], 0),
    ([1111111111, 1313131313, 1515151515], 0),
    ([11, 13, 15, 17, 19], 5),
    ([-11, -13, -15, -17, -19], 5),
    ([11, 13, 15, 17, 19, -1], 5),
    ([-11, -13, -15, -17, -19, 1], 5),
    ([11, 13, 15, 17, 19, -11], 5),
    ([-11, -13, -15, -17, -19, 13], 5),
])
def test_specialFilter(nums, expected):
    assert specialFilter(nums) == expected

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_matching_numbers():
    assert specialFilter([-1, -2, -3]) == 0

def test_single_matching_number():
    assert specialFilter([11]) == 0

def test_single_matching_number_greater_than_10():
    assert specialFilter([111]) == 0

def test_multiple_matching_numbers():
    assert specialFilter([15, 33, 45, 109]) == 3

def test_negative_numbers():
    assert specialFilter([-15, -33, -45]) == 0

def test_mixed_positive_negative():
    assert specialFilter([-15, 33, -45, 109]) == 2

def test_edge_case_single_digit_odd():
    assert specialFilter([11]) == 0

def test_edge_case_single_digit_even():
    assert specialFilter([22]) == 0

def test_edge_case_first_last_digit_same_odd():
    assert specialFilter([111]) == 0

def test_edge_case_first_last_digit_same_even():
    assert specialFilter([222]) == 0

def test_edge_case_first_last_digit_different_odd():
    assert specialFilter([15, 33, 55, 77, 99]) == 5