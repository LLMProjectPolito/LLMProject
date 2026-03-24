


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

def test_empty_list():
    assert sum_squares([]) == 0

def test_single_element_not_multiple_of_3_or_4():
    assert sum_squares([5]) == 5

def test_single_element_multiple_of_3():
    assert sum_squares([5]) == 25

def test_single_element_multiple_of_4_not_3():
    assert sum_squares([5]) == 125

def test_example_1():
    assert sum_squares([1, 2, 3]) == 6

def test_example_2():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_multiple_multiples_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1 + 8 + 27 + 64 + 125 + 216 + 343 + 512 + 729

def test_mixed_multiples():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1 + 4 + 9 + 64 + 125 + 216 + 343 + 512 + 729 + 100

def test_negative_numbers():
    assert sum_squares([-1, -2, -3]) == -1 + 4 + (-27)

def test_zeroes():
    assert sum_squares([0, 1, 2, 3]) == 0 + 1 + 4 + 9

def test_large_numbers():
    assert sum_squares([100, 200, 300]) == 10000 + 80000 + 270000

def test_long_list():
    lst = list(range(1, 11))
    assert sum_squares(lst) == 1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100