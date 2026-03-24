
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

def test_no_special_numbers():
    assert specialFilter([2, 4, 6, 8, 10, 12]) == 0

def test_single_special_number():
    assert specialFilter([15]) == 1

def test_multiple_special_numbers():
    assert specialFilter([15, 37, 59, 71, 93]) == 5

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_negative_numbers():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_numbers_with_even_first_digit():
    assert specialFilter([21, 43, 65, 87, 09]) == 0

def test_numbers_with_even_last_digit():
    assert specialFilter([12, 34, 56, 78, 90]) == 0

def test_numbers_with_both_even_digits():
    assert specialFilter([24, 46, 68, 80]) == 0

def test_numbers_greater_than_10_but_not_special():
    assert specialFilter([12, 14, 16, 18, 21]) == 0

def test_numbers_less_than_or_equal_to_10():
    assert specialFilter([1, 3, 5, 7, 9, 10]) == 0

def test_large_numbers():
    assert specialFilter([111, 333, 555, 777, 999, 12345]) == 5

def test_large_numbers_with_even_digits():
    assert specialFilter([123, 345, 567, 789, 901]) == 0

def test_mixed_positive_and_negative():
    assert specialFilter([-15, 37, -59, 71, -93, 11]) == 2

def test_edge_case_11():
    assert specialFilter([11]) == 1

def test_edge_case_99():
    assert specialFilter([99]) == 1

def test_numbers_less_than_10():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_numbers_equal_to_10():
    assert specialFilter([10]) == 0

def test_large_numbers_mixed():
    assert specialFilter([111, 222, 333, 444, 555]) == 3

def test_edge_case_1():
    assert specialFilter([11]) == 0

def test_edge_case_2():
    assert specialFilter([13]) == 1

def test_edge_case_3():
    assert specialFilter([31]) == 1

def test_edge_case_4():
    assert specialFilter([101]) == 0

def test_edge_case_5():
    assert specialFilter([103]) == 1

def test_edge_case_6():
    assert specialFilter([301]) == 1

def test_edge_case_7():
    assert specialFilter([123]) == 0

def test_edge_case_8():
    assert specialFilter([321]) == 0

def test_complex_case():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_zero_in_number():
    assert specialFilter([101, 103, 105, 107, 109]) == 0

def test_all_negative_numbers():
    assert specialFilter([-11, -13, -15, -22, -23]) == 3

def test_large_negative_numbers():
    assert specialFilter([-101, -123, -157, -189, -1001]) == 4

def test_negative_numbers_only():
    assert specialFilter([-11, -13, -15, -17, -19]) == 5