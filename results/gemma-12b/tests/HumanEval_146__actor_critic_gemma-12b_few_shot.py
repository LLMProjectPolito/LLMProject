
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
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    
    count = 0
    for num in nums:
        if not isinstance(num, (int, float)) or num <= 10:
            continue  # Skip non-numeric elements and numbers <= 10

        num_str = str(int(num))  # Convert to integer first to handle floats and avoid floating-point string representation issues
        if num_str[0] in '13579' and num_str[-1] in '13579':
            count += 1
    return count

import pytest

def test_specialFilter_basic():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_multiple():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_empty():
    assert specialFilter([]) == 0

def test_specialFilter_no_numbers_greater_than_10():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_specialFilter_numbers_greater_than_10_not_meeting_criteria():
    assert specialFilter([11, 12, 13, 14, 15]) == 0

def test_specialFilter_negative_numbers_meeting_criteria():
    assert specialFilter([-11, -13, -15]) == 3

def test_specialFilter_with_zero():
    assert specialFilter([0, 15, 33]) == 2

def test_specialFilter_single_digit_number_greater_than_10():
    assert specialFilter([11]) == 0

def test_specialFilter_mixed_positive_and_negative():
    assert specialFilter([-15, 15, -33, 33]) == 4

def test_specialFilter_invalid_input_type():
    with pytest.raises(TypeError):
        specialFilter("not a list")

def test_specialFilter_list_with_non_numeric_elements():
    assert specialFilter([15, "abc", 33, True]) == 2

def test_specialFilter_floating_point():
    assert specialFilter([15.0, 33.0]) == 2

def test_specialFilter_leading_zeros():
    assert specialFilter([015]) == 0