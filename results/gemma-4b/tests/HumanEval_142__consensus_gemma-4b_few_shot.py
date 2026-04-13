


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

def test_mixed_positive_negative():
    assert sum_squares([1, -2, 3, -4, 5]) == 1 + 4 + 9 + (-64) + 25 == 1 + 4 + 9 - 64 + 25 == -25

def test_multiple_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1**2 + 2**2 + 3**2 + 4**2 + 5**2 + 6**2 == 1 + 4 + 9 + 16 + 25 + 36 == 91

def test_multiple_4_not_3():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1**2 + 2**2 + 3**2 + 4**3 + 5**2 + 6**2 + 7**2 + 8**3 == 1 + 4 + 9 + 64 + 25 + 36 + 49 + 512 == 690

def test_all_multiples_of_3():
    assert sum_squares([3, 6, 9, 12]) == 3**2 + 6**2 + 9**2 + 12**2 == 9 + 36 + 81 + 144 == 269

def test_all_multiples_of_4_not_3():
    assert sum_squares([4, 8, 12, 16]) == 4**3 + 8**3 + 12**3 + 16**3 == 64 + 512 + 1728 + 4096 == 6400

def test_mixed_multiples():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1**2 + 2**2 + 3**2 + 4**3 + 5**2 + 6**2 + 7**2 + 8**3 + 9**2 + 10**2 == 1 + 4 + 9 + 64 + 25 + 36 + 49 + 512 + 81 + 100 == 881