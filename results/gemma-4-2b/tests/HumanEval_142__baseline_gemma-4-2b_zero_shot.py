


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
            total += num * num
        elif i % 4 != 0:
            total += num * num * num
    return total

def test_empty_list():
    assert sum_squares([]) == 0

def test_list_with_no_multiples_of_3_or_4():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 21

def test_list_with_only_multiples_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 162

def test_list_with_only_multiples_of_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 1728

def test_list_with_multiples_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 1728

def test_list_with_mixed_multiples():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 1728

def test_list_with_negative_numbers():
    assert sum_squares([-1, -2, -3, -4, -5, -6, -7, -8, -9]) == 288

def test_list_with_mixed_positive_and_negative():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_list_with_zero():
    assert sum_squares([0, 1, 2, 3, 4, 5]) == 25

def test_list_with_all_zeros():
    assert sum_squares([0, 0, 0, 0, 0]) == 0