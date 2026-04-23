


def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """

import pytest
from your_module import sum_squares  # Replace your_module

def test_empty_list():
    assert sum_squares([]) == 0

def test_basic_list():
    assert sum_squares([1, 2, 3]) == 6

def test_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_mixed_positive_negative():
    assert sum_squares([1, -2, 3, -4, 5, -6]) == -11

def test_multiples_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 135

def test_multiples_of_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 144

def test_multiples_of_both():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 288

def test_large_numbers():
    assert sum_squares([10, 20, 30, 40]) == 3000

def test_zeroes():
    assert sum_squares([0, 0, 0, 0]) == 0

def test_single_element():
    assert sum_squares([5]) == 5

def test_complex_list():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 285

def test_list_with_duplicates():
    assert sum_squares([2, 2, 2, 2, 2]) == 10

def test_list_with_only_multiples_of_3():
    assert sum_squares([3, 6, 9, 12]) == 297

def test_list_with_only_multiples_of_4():
    assert sum_squares([4, 8, 12, 16]) == 416

def test_list_with_mixed_numbers_and_indices():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 748

def test_list_with_multiples_of_3_suite2():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 2 + 9 + 4 + 5 + 36  # 3^2 = 9, 6^2 = 36

def test_list_with_multiples_of_4_suite2():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 2 + 3 + 64 + 5 + 6 + 7 + 64 # 4^3 = 64, 8^3 = 512

def test_list_with_multiples_of_both_3_and_4_suite2():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 9 + 64 + 5 + 6 + 7 + 512 + 9 + 10 + 11 + 1728 # 12^3 = 1728

def test_list_with_negative_numbers_suite2():
    assert sum_squares([-1, -5, 2, -1, -5]) == -1 - 125 + 2 - 1 - 125

def test_list_with_mixed_positive_and_negative_suite2():
    assert sum_squares([-1, 2, -3, 4, -5, 6]) == -1 + 8 - 9 + 64 - 125 + 36

def test_list_with_zeros_suite2():
    assert sum_squares([0, 1, 2, 3, 4, 5]) == 0 + 1 + 2 + 9 + 4 + 5

def test_large_list_suite2():
    large_list = list(range(1, 21))
    expected_sum = 0
    for i, num in enumerate(large_list):
        if i % 3 == 0:
            expected_sum += num**2
        elif i % 4 == 0:
            expected_sum += num**3
        else:
            expected_sum += num
    assert sum_squares(large_list) == expected_sum

def test_list_with_duplicates_suite2():
    assert sum_squares([1, 1, 1, 1, 1]) == 1 + 1 + 9 + 1 + 1

def test_list_with_floats_suite2():
    assert sum_squares([1.0, 2.0, 3.0]) == 6

def test_list_with_large_numbers_suite2():
    assert sum_squares([100, 200, 300]) == 100 + 200 + 90000