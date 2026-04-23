


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

def test_no_multiples_of_3_or_4():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 4 + 9 + 16 + 25 + 36 == 91

def test_only_multiples_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9 + 9 + 9 + 16 + 25 + 36 + 49 + 64 + 81 == 333

def test_only_multiples_of_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 16 + 64 + 125 + 256 + 441 + 729 == 1611

def test_mixed_multiples_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100 + 121 + 144 == 669

def test_negative_numbers():
    assert sum_squares([-1, -2, -3]) == 1 + 9 + 27 == 37
    assert sum_squares([-1, -5, 2, -1, -5]) == 1 + 25 + 4 + 1 + 25 == 56

def test_zero():
    assert sum_squares([0, 1, 2, 3]) == 0 + 1 + 4 + 9 == 14

def test_all_zeros():
    assert sum_squares([0, 0, 0, 0]) == 0

def test_large_numbers():
    assert sum_squares([100, 200, 300, 400]) == 10000 + 40000 + 90000 + 160000 == 300000

def test_complex_list():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100 + 121 + 144 + 169 + 196 + 225 == 1439