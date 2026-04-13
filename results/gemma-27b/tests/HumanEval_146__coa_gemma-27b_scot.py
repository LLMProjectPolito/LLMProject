
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


# Focus: Boundary Values
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
            if num_str[0] in '13579' and num_str[-1] in '13579':
                count += 1
    return count

def test_boundary_empty_array():
    assert specialFilter([]) == 0

def test_boundary_single_element_less_than_10():
    assert specialFilter([5]) == 0

def test_boundary_single_element_greater_than_10_valid():
    assert specialFilter([11]) == 1

def test_boundary_single_element_greater_than_10_invalid_first_digit():
    assert specialFilter([21]) == 0

def test_boundary_single_element_greater_than_10_invalid_last_digit():
    assert specialFilter([12]) == 0

def test_boundary_single_element_negative_valid():
    assert specialFilter([-11]) == 1

def test_boundary_single_element_negative_invalid_first_digit():
    assert specialFilter([-21]) == 0

def test_boundary_single_element_negative_invalid_last_digit():
    assert specialFilter([-12]) == 0

# Focus: Logic Branches
import pytest

def test_special_filter_empty_list():
    assert specialFilter([]) == 0

def test_special_filter_no_special_numbers():
    assert specialFilter([2, 4, 6, 8, 10, 12]) == 0

def test_special_filter_mixed_numbers():
    assert specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109]) == 4

# Focus: Invalid Input Handling
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

def test_invalid_input_empty_list():
    assert specialFilter([]) == 0

def test_invalid_input_list_with_non_numeric_values():
    with pytest.raises(TypeError):
        specialFilter([15, "abc", 14])

def test_invalid_input_list_with_mixed_types():
    with pytest.raises(TypeError):
        specialFilter([15, 14, 15.5])