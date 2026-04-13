


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
    total = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            total += num**2
        elif i % 4 == 0 and i % 3 != 0:
            total += num**3
    return total

def test_empty_list():
    assert sum_squares([]) == 0

def test_single_element_not_multiple_of_3_or_4():
    assert sum_squares([5]) == 5

def test_single_element_multiple_of_3():
    assert sum_squares([5]) == 25

def test_single_element_multiple_of_4_not_3():
    assert sum_squares([5]) == 125

def test_multiple_of_3():
    assert sum_squares([1, 2, 3]) == 14

def test_multiple_of_4_not_3():
    assert sum_squares([1, 2, 3, 4]) == 100

def test_multiple_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 126

def test_mixed_cases():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_large_list():
    lst = list(range(1, 11))
    expected_sum = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            expected_sum += num**2
        elif i % 4 == 0 and i % 3 != 0:
            expected_sum += num**3
    assert sum_squares(lst) == expected_sum

def test_negative_numbers():
    assert sum_squares([-1, -2, -3]) == -14

def test_zeroes():
    assert sum_squares([0, 0, 0]) == 0

def test_mixed_positive_negative_zeroes():
    assert sum_squares([-1, 0, 1]) == 2

def test_complex_list():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 385

def test_large_numbers():
    assert sum_squares([10, 20, 30, 40]) == 30000

def test_list_with_zeros():
    assert sum_squares([0, 0, 0]) == 0

def test_list_with_mixed_positive_and_negative():
    assert sum_squares([-2, 1, -3, 4, -5]) == -126

def test_list_with_duplicate_values():
    assert sum_squares([1, 1, 1, 1]) == 4

def test_list_with_large_index_multiples():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 648