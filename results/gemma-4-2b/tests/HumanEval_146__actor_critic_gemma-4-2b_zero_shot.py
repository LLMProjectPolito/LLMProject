
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
            if len(num_str) > 0:
                first_digit = int(num_str[0])
                last_digit = int(num_str[-1])
                if first_digit % 2 != 0 and last_digit % 2 != 0:
                    count += 1
    return count

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_numbers_greater_than_10():
    assert specialFilter([-1, -2, -3]) == 0

def test_all_numbers_greater_than_10_but_not_meeting_criteria():
    assert specialFilter([11, 13, 15]) == 0

def test_all_numbers_greater_than_10_and_meeting_criteria():
    assert specialFilter([11, 13, 15]) == 3

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_negative_numbers():
    assert specialFilter([-15, -73, -14, -15]) == 1

def test_zero():
    assert specialFilter([0, 10]) == 0

def test_single_number_greater_than_10_meeting_criteria():
    assert specialFilter([15]) == 1

def test_single_number_greater_than_10_not_meeting_criteria():
    assert specialFilter([14]) == 0

def test_single_number_less_than_10():
    assert specialFilter([5]) == 0

def test_large_numbers():
    assert specialFilter([1000000000, 1000000001]) == 1

def test_large_negative_numbers():
    assert specialFilter([-1000000000, -1000000001]) == 1

def test_mixed_positive_and_negative_greater_than_10():
    assert specialFilter([15, -73, 14, -15, 100, -100]) == 1

def test_all_same_number():
    assert specialFilter([15, 15, 15, 15]) == 1

def test_all_same_number_not_meeting_criteria():
    assert specialFilter([14, 14, 14, 14]) == 0

def test_single_digit_number_greater_than_10():
    assert specialFilter([11]) == 1

def test_single_digit_number_less_than_10():
    assert specialFilter([5]) == 0

def test_single_digit_number_equal_to_10():
    assert specialFilter([10]) == 0

def test_single_digit_number_not_greater_than_10():
    assert specialFilter([1]) == 0

def test_single_digit_number_not_greater_than_10_and_not_meeting_criteria():
    assert specialFilter([2]) == 0

def test_single_digit_number_not_greater_than_10_and_not_meeting_criteria_2():
    assert specialFilter([4]) == 0

def test_single_digit_number_not_greater_than_10_and_not_meeting_criteria_3():
    assert specialFilter([6]) == 0

def test_single_digit_number_not_greater_than_10_and_not_meeting_criteria_4():
    assert specialFilter([8]) == 0

def test_single_digit_number_not_greater_than_10_and_not_meeting_criteria_5():
    assert specialFilter([9]) == 0

def test_single_digit_number_not_greater_than_10_and_not_meeting_criteria_6():
    assert specialFilter([1]) == 0

def test_single_digit_number_not_greater_than_10_and_not_meeting_criteria_7():
    assert specialFilter([2]) == 0

def test_single_digit_number_not_greater_than_10_and_not_meeting_criteria_8():
    assert specialFilter([4]) == 0

def test_single_digit_number_not_greater_than_10_and_not_meeting_criteria_9():
    assert specialFilter([6]) == 0

def test_single_digit_number_not_greater_than_10_and_not_meeting_criteria_10():
    assert specialFilter([8]) == 0

def test_single_digit_number_not_greater_than_10_and_not_meeting_criteria_11():
    assert specialFilter([9]) == 0

def test_single_digit_number_not_greater_than_10_and_not_meeting_criteria_12():
    assert specialFilter([1]) == 0

def test_single_digit_number_not_greater_than_10_and_not_meeting_criteria_13():
    assert specialFilter([2]) == 0

def test_single_digit_number_not_greater_than_10_and_not_meeting_criteria_14():
    assert specialFilter([4]) == 0

def test_single_digit_number_not_greater_than_10_and_not_meeting_criteria_15():
    assert specialFilter([6]) == 0

def test_single_digit_number_not_greater_than_10_and_not_meeting_criteria_16():
    assert specialFilter([8]) == 0

def test_single_digit_number_not_greater_than_10_and_not_meeting_criteria_17():
    assert specialFilter([9]) == 0

def test_single_digit_number_not_greater_than_10_and_not_meeting_criteria_18():
    assert specialFilter([1]) == 0

def test_single_digit_number_not_greater_than_10_and_not_meeting_criteria_19():
    assert specialFilter([2]) == 0

def test_single_digit_number_not_greater_than_10_and_not_meeting_criteria_20():
    assert specialFilter([4]) == 0

def test_single_digit_number_not_greater_than_10_and_not_meeting_criteria_21():
    assert specialFilter([6]) == 0

def test_single_digit_number_not_greater_than_10_and_not_meeting_criteria_22():
    assert specialFilter([8]) == 0

def test_single_digit_number_not_greater_than_10_and_not_meeting_criteria_23():
    assert specialFilter([9]) == 0