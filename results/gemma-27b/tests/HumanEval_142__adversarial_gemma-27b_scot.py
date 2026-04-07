


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

def test_empty_list():
    assert sum_squares([]) == 0

def test_example_1():
    assert sum_squares([1, 2, 3]) == 12

def test_example_2():
    assert sum_squares([]) == 0

def test_example_3():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_list_multiple_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 2 + 9 + 4 + 5 + 36

def test_list_multiple_of_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 2 + 3 + 64 + 5 + 6 + 7 + 512

def test_list_multiple_of_12():
    lst = list(range(12))
    expected_sum = sum(lst)
    expected_sum += lst[0]**2
    expected_sum += lst[3]**3
    expected_sum += lst[6]**2
    expected_sum += lst[9]**3
    assert sum_squares(lst) == expected_sum

def test_negative_numbers():
    assert sum_squares([-1, -2, -3, -4]) == (-1) + (-2) + (-3)**2 + (-4)**3

def test_mixed_numbers():
    assert sum_squares([-1, 2, -3, 4, -5]) == (-1) + 2 + (-3)**2 + 4 + (-5)

def test_zeroes():
    assert sum_squares([0, 0, 0, 0]) == 0

def test_large_numbers():
    assert sum_squares([1000, 2000, 3000]) == 1000 + 2000 + 3000**2