


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

def test_sum_squares_with_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_with_single_element_multiple_of_3():
    assert sum_squares([5]) == 25

def test_sum_squares_with_single_element_multiple_of_4():
    assert sum_squares([2]) == 8

def test_sum_squares_with_single_element_not_multiple_of_3_or_4():
    assert sum_squares([7]) == 7

def test_sum_squares_with_example_1():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_with_example_2():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_with_mixed_list():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 727

def test_sum_squares_with_list_with_zeros():
    assert sum_squares([0, 0, 0, 0, 0]) == 0

def test_sum_squares_with_negative_numbers():
    assert sum_squares([-2, 2, -3, 4]) == 4 + 2 + 27 + 64

def test_sum_squares_with_index_multiple_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 9 + 64 + 5 + 36 + 7 + 512 + 81 + 10 + 121 + 144

def test_sum_squares_with_larger_list():
    assert sum_squares(list(range(20))) == 1 + 2 + 9 + 64 + 5 + 36 + 7 + 512 + 81 + 10 + 121 + 144 + 13 + 16 + 25 + 64 + 17 + 36

def test_sum_squares_with_mixed_positive_negative_zeros():
    assert sum_squares([-1, 0, 1, -2, 2, 0, 3, -3]) == 1 + 0 + 1 + -8 + 8 + 0 + 9 + 9