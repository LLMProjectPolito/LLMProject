


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
    total_sum = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            total_sum += num**2
        elif i % 4 == 0 and i % 3 != 0:
            total_sum += num**3
    return total_sum

def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_basic_positive():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_multiple_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 139

def test_sum_squares_multiple_of_4_not_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 441

def test_sum_squares_mixed():
    assert sum_squares([-1, -5, 2, -1, -5]) == -252

def test_sum_squares_all_multiples_of_3():
    assert sum_squares([3, 6, 9, 12]) == 270

def test_sum_squares_all_multiples_of_4_not_3():
    assert sum_squares([4, 8, 12, 16]) == 6400

def test_sum_squares_no_multiples():
    assert sum_squares([1, 2, 4, 5, 7, 8]) == 23