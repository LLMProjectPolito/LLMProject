


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
        elif i % 4 == 0 and i % 3 != 0:
            total += num ** 3
    return total

def test_empty_list():
    assert sum_squares([]) == 0

def test_simple_list():
    assert sum_squares([1, 2, 3]) == 6

def test_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_multiple_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 4 + 36 + 4 + 25 + 36

def test_multiple_of_4_not_3():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 8 + 27 + 64 + 125 + 216 + 343 + 512

def test_mixed_multiples():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1 + 4 + 9 + 64 + 125 + 36 + 343 + 512 + 81 + 100

def test_large_numbers():
    assert sum_squares([100, 200, 300, 400]) == 10000 + 800000 + 27000000 + 64000000

def test_zero_in_list():
    assert sum_squares([0, 1, 2, 3]) == 0 + 1 + 4 + 9

def test_list_with_zeros():
    assert sum_squares([0, 0, 0]) == 0

def test_list_with_only_multiples_of_4():
    assert sum_squares([4, 8, 12, 16]) == 64 + 512 + 1728 + 4096

def test_list_with_only_multiples_of_3():
    assert sum_squares([3, 6, 9, 12]) == 9 + 36 + 81 + 144