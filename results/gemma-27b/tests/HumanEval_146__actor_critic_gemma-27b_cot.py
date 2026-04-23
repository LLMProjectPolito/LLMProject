
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

# Assumption: A "special number" is a number where the sum of its digits is divisible by 3.
# Negative numbers are ignored.

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_special_numbers():
    assert specialFilter([2, 4, 6, 8, 10, 12]) == 0

def test_single_special_number():
    assert specialFilter([15]) == 1

def test_multiple_special_numbers():
    assert specialFilter([15, 37, 59, 71, 93]) == 5

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_more_mixed_numbers():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_negative_numbers():
    assert specialFilter([-15, -37, -59, -71, -93]) == 0

def test_large_numbers():
    assert specialFilter([111, 333, 555, 777, 999]) == 5

def test_large_numbers_mixed():
    assert specialFilter([111, 222, 333, 444, 555]) == 3

def test_edge_case_99():
    assert specialFilter([99]) == 1

def test_edge_case_101():
    assert specialFilter([101]) == 0

def test_edge_case_131():
    assert specialFilter([131]) == 1

def test_zero_as_first_digit():
    assert specialFilter([01, 03, 05]) == 0

def test_string_input_ignored():
    assert specialFilter([15, "abc", 37, True, 59]) == 3

def test_mixed_input_with_non_integers():
    assert specialFilter([15, "abc", 37, 59, 1.5]) == 3

def test_type_error_handling():
    with pytest.raises(TypeError):
        specialFilter([15, "abc", 37, 59, [1,2,3]])
    with pytest.raises(TypeError):
        specialFilter([15, "abc", 37, 59, {1:2}])
    with pytest.raises(TypeError):
        specialFilter([15, "abc", 37, 59, {1,2}])

def test_zero():
    assert specialFilter([0]) == 0

def test_large_number_divisible_by_3():
    assert specialFilter([111111111111111111111111111111]) == 1

def test_large_number_not_divisible_by_3():
    assert specialFilter([111111111111111111111111111112]) == 0

def test_mixed_positive_negative_special():
    assert specialFilter([15, -2, 33, -11, 51, -45]) == 2

def test_all_negative():
    assert specialFilter([-1, -3, -5, -7, -9]) == 0