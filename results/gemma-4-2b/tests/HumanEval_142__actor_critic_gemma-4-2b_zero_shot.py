


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

def test_single_element_list():
    assert sum_squares([5]) == 5

def test_multiple_of_3_and_4():
    assert sum_squares([12, 15, 18]) == 120

def test_multiple_of_4_and_3():
    assert sum_squares([12, 15, 18]) == 120

def test_mixed_multiples():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 21

def test_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_mixed_positive_and_negative():
    assert sum_squares([1, -2, 3, -4, 5]) == 10

def test_zero_in_list():
    assert sum_squares([0, 1, 2, 3, 4]) == 10

def test_all_zeros():
    assert sum_squares([0, 0, 0, 0]) == 0

def test_large_numbers():
    assert sum_squares([100, 200, 300, 400]) == 300000

def test_multiple_of_4_and_3_mixed():
    assert sum_squares([12, 15, 16, 18]) == 120

def test_single_element_multiple_of_4():
    assert sum_squares([4]) == 4

def test_single_element_multiple_of_3():
    assert sum_squares([3]) == 9

def test_list_of_multiples_of_3():
    assert sum_squares([3, 6, 9]) == 162

def test_list_of_multiples_of_4():
    assert sum_squares([4, 8, 12]) == 288

def test_list_of_multiples_of_3_and_4():
    assert sum_squares([12, 24, 36]) == 216