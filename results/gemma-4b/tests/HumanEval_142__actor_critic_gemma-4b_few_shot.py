


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

def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_basic():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_negative():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_mixed():
    assert sum_squares([1, -2, 3, -4, 5]) == 1 + (-2)**2 + 3**2 + (-4)**3 + 5**2 == 1 + 4 + 9 + (-64) + 25 == 1 + 4 + 9 - 64 + 25 == -25

def test_sum_squares_multiple_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 4 + 9 + 64 + 25 + 36 == 1 + 4 + 9 + 64 + 25 + 36 == 149

def test_sum_squares_multiple_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1 + 8 + 27 + 64 + 125 + 216 + 343 + 512 + 729 + 1000 == 3096

def test_sum_squares_no_multiples():
    assert sum_squares([1, 2, 4, 5, 7, 8, 10]) == 1 + 2 + 5 + 7 + 8 + 10 == 33