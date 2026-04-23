


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
            total += num ** 2
        elif i % 4 == 0:
            total += num ** 3
        else:
            total += num
    return total

def test_empty_list():
    assert sum_squares([]) == 0

def test_single_element_multiple_of_3():
    assert sum_squares([5]) == 25

def test_single_element_zero_list():
    assert sum_squares([0]) == 0

def test_single_element_non_zero():
    assert sum_squares([2]) == 8

def test_single_element_not_multiple_of_3_or_4():
    assert sum_squares([7]) == 7

def test_example_1():
    assert sum_squares([1, 2, 3]) == 6

def test_example_2():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_multiple_of_12():
    expected_sum = 1 + 2 + 9 + 64 + 5 + 36 + 7 + 8 + 81 + 100 + 121 + 144
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == expected_sum

def test_negative_numbers():
    assert sum_squares([-1, 2, -3, 4, -5]) == -1 + 4 + 9 + 64 - 5

def test_zeros():
    assert sum_squares([0, 0, 0, 0, 0]) == 0

def test_larger_list():
    assert sum_squares(list(range(1, 16))) == 1 + 2 + 9 + 64 + 5 + 36 + 7 + 8 + 81 + 100 + 121 + 144 + 13 + 16 + 25

def test_index_0():
    assert sum_squares([5]) == 25