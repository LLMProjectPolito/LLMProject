
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

# Focus: Equivalence Partitioning
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

def test_equivalence_partitioning_1():
    """Test case: Array with numbers satisfying the condition."""
    assert specialFilter([15, 33, 57, 79, 91]) == 5

def test_equivalence_partitioning_2():
    """Test case: Array with numbers not satisfying the condition."""
    assert specialFilter([2, 4, 6, 8, 10]) == 0

def test_equivalence_partitioning_3():
    """Test case: Mixed array with some numbers satisfying and some not."""
    assert specialFilter([15, 22, 33, 44, 55, 66, 77, 88, 99, 10]) == 3

# Focus: Logic Branches
import pytest

def test_special_filter_empty_list():
    assert specialFilter([]) == 0

def test_special_filter_no_special_numbers():
    assert specialFilter([2, 4, 6, 8, 10, 12]) == 0

def test_special_filter_mixed_numbers():
    assert specialFilter([15, -73, 14, -15, 33, 109, 21]) == 3

def test_special_filter_all_special_numbers():
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_special_filter_negative_numbers():
    assert specialFilter([-15, -33, -55, -77, -99]) == 5

def test_special_filter_single_special_number():
    assert specialFilter([15]) == 1

def test_special_filter_single_non_special_number():
    assert specialFilter([14]) == 0