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
            if len(num_str) > 0:
                first_digit = int(num_str[0])
                last_digit = int(num_str[-1])
                if first_digit % 2 != 0 and last_digit % 2 != 0:
                    count += 1
    return count

@pytest.mark.parametrize("nums", [
    [11],  # Single element, boundary value (just above 10, odd digits)
    [9],   # Single element, below 10
    [10],  # Single element, equal to 10
    [12],  # Single element, just above 10, even last digit
    [21],  # Single element, odd first, even last
    [15],  # Single element, odd first and last
    [101], # Three digits, odd first and last
    [100], # Three digits, even last
    [111], # Three digits, all odd
    [112], # Three digits, odd first, even last
    [121], # Three digits, even first, odd last
])
def test_specialFilter_boundary_values(nums):
    assert specialFilter(nums) == pytest.param(
        0 if len(nums) == 1 and nums[0] <= 10 else (1 if len(nums) == 1 and nums[0] == 11 else (1 if len(nums) == 1 and nums[0] == 15 else (1 if len(nums) == 1 and nums[0] == 101 else (0 if len(nums) == 1 and nums[0] == 100 else (1 if len(nums) == 1 and nums[0] == 111 else (0 if len(nums) == 1 and nums[0] == 112 else (0 if len(nums) == 1 and nums[0] == 121 else 0)))))),
        id=f"nums={nums}"
    )

# Focus: Logic Branches
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

def test_specialFilter_empty_array():
    assert specialFilter([]) == 0

def test_specialFilter_no_special_numbers():
    assert specialFilter([2, 4, 6, 8, 10]) == 0

def test_specialFilter_mixed_numbers():
    assert specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109]) == 4

def test_specialFilter_all_special_numbers():
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_specialFilter_negative_numbers():
    assert specialFilter([-11, -13, -15, -17, -19]) == 5

def test_specialFilter_single_special_number():
    assert specialFilter([15]) == 1

def test_specialFilter_single_non_special_number():
    assert specialFilter([12]) == 0

def test_specialFilter_large_numbers():
    assert specialFilter([1001, 1002, 1011, 1012]) == 2

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
        specialFilter([15, "abc", 33])

def test_invalid_input_list_with_mixed_types():
    with pytest.raises(TypeError):
        specialFilter([15, 2.5, 33])