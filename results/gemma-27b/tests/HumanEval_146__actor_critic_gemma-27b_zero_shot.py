
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
        if not isinstance(num, int):
            continue  # Skip non-integer inputs
        if num > 10:
            num_str = str(abs(num))
            first_digit = int(num_str[0])
            last_digit = int(num_str[-1])
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
    return count

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_special_numbers():
    assert specialFilter([2, 4, 6, 8, 10]) == 0

def test_multiple_special_numbers():
    assert specialFilter([15, 33, 57, 79, 91]) == 5

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_negative_numbers():
    assert specialFilter([-11, -13, -15, -17, -19]) == 5

def test_large_numbers():
    assert specialFilter([101, 123, 155, 177, 199]) == 5

def test_numbers_with_even_digits():
    assert specialFilter([12, 34, 56, 78, 90]) == 0

def test_numbers_less_than_or_equal_to_10():
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0

def test_mixed_positive_and_negative():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

@pytest.mark.parametrize("num", [11, 99, 101])
def test_edge_cases(num):
    assert specialFilter([num]) == 1

def test_edge_case_100():
    assert specialFilter([100]) == 0

def test_edge_case_10():
    assert specialFilter([10]) == 0

def test_greater_than_10_no_special():
    assert specialFilter([12, 14, 16, 18, 21, 23]) == 0

def test_zero_padding():
    assert specialFilter([11]) == 1

def test_large_number_with_even_digit():
    assert specialFilter([1234567890]) == 0

def test_non_integer_input():
    assert specialFilter([15, "abc", 33]) == 2

def test_multiple_non_integer_inputs():
    assert specialFilter([15, "abc", "def", 33, 1.2]) == 2

def test_very_large_number():
    assert specialFilter([1234567891]) == 1