
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
            num_str = str(abs(num))  # Handle negative numbers
            if len(num_str) > 0:
                first_digit = int(num_str[0])
                last_digit = int(num_str[-1])
                if first_digit % 2 != 0 and last_digit % 2 != 0:
                    count += 1
    return count

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([15, -73, 14, -15], 1),
        ([33, -2, -3, 45, 21, 109], 2),
        ([11, 22, 33, 44, 55], 0),
        ([111, 333, 555, 777, 999], 5),
        ([12, 23, 34, 45, 56], 0),
        ([101, 111, 121, 131, 141], 3),
        ([10, 20, 30, 40, 50], 0),
        ([11, 12, 13, 14, 15], 1),
        ([1, 2, 3, 4, 5], 0),
        ([11, 13, 15, 17, 19], 0),
        ([11, 13, 15, 17, 19, 111], 1),
        ([111, 111, 111], 3),
        ([111, 111, 111, 10], 3),
        ([111, 111, 111, 10, 20], 3),
        ([], 0),
        ([11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 1),
        ([11, 13, 15, 17, 19, 21, 23, 25, 27, 29], 0),
        ([11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 111], 1),
        ([11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 111, 333], 2),
    ]
)
def test_specialFilter(nums, expected):
    assert specialFilter(nums) == expected

def test_specialFilter_negative_numbers():
    assert specialFilter([-15, -73, -14, -15]) == 1

def test_specialFilter_large_numbers():
    assert specialFilter([151, 353, 555, 757, 959]) == 5

def test_specialFilter_mixed_numbers():
    assert specialFilter([15, -73, 14, -15, 111, -333]) == 2

def test_specialFilter_zero():
    assert specialFilter([0, 10, 11, 12]) == 0

# Additional tests from Suite 2
def test_special_filter_basic():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_special_filter_multiple():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_special_filter_empty():
    assert specialFilter([]) == 0

def test_special_filter_no_match():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_special_filter_all_match():
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_special_filter_mixed_positive_negative():
    assert specialFilter([11, -33, 55, -77, 99, 12, -21]) == 5

def test_special_filter_large_numbers_suite2():
    assert specialFilter([123, 345, 567, 789, 901]) == 5

def test_special_filter_single_digit_suite2():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_special_filter_zero_suite2():
    assert specialFilter([0]) == 0

def test_special_filter_negative_numbers_only_suite2():
    assert specialFilter([-11, -33, -55, -77, -99]) == 0

def test_special_filter_numbers_greater_than_100_suite2():
    assert specialFilter([111, 333, 555, 777, 999]) == 5

def test_special_filter_numbers_with_leading_zeros_suite2():
    assert specialFilter([101, 303, 505, 707, 909]) == 5

def test_special_filter_numbers_with_mixed_digits_suite2():
    assert specialFilter([121, 343, 565, 787, 909]) == 0

def test_special_filter_edge_case_1_suite2():
    assert specialFilter([11, 12, 13, 14, 15]) == 1

def test_special_filter_edge_case_2_suite2():
    assert specialFilter([99, 98, 97, 96, 95]) == 1

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None