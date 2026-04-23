


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
        elif i % 4 != 0:
            total += num ** 3
    return total

import pytest

def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_no_moduli():
    assert sum_squares([1, 2, 3, 4, 5]) == 15

def test_sum_squares_only_moduli_3():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 144

def test_sum_squares_only_moduli_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1728

def test_sum_squares_mixed_moduli():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1728

def test_sum_squares_negative_numbers():
    assert sum_squares([-1, -2, -3, -4, -5]) == -126

def test_sum_squares_mixed_positive_negative():
    assert sum_squares([-1, 2, -3, 4, -5]) == -126

def test_sum_squares_zero():
    assert sum_squares([0, 1, 2, 3, 4]) == 0

def test_sum_squares_all_zeros():
    assert sum_squares([0, 0, 0, 0]) == 0

def test_sum_squares_single_element():
    assert sum_squares([5]) == 25

def test_sum_squares_list_with_one_element_multiple_of_3():
    assert sum_squares([3]) == 9

def test_sum_squares_list_with_one_element_multiple_of_4():
    assert sum_squares([4]) == 64

def test_sum_squares_large_list():
    large_list = list(range(1, 101))
    assert sum_squares(large_list) == 1729000