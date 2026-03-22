import pytest
import math

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
    new_lst = []
    for i in range(len(lst)):
        if i % 3 == 0:
            new_lst.append(lst[i]**2)
        elif i % 4 == 0 and i % 3 != 0:
            new_lst.append(lst[i]**3)
        else:
            new_lst.append(lst[i])
    return sum(new_lst)

def test_basic():
    assert sum_squares([1, 2, 3]) == 6

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
        else:
            total += num
    return total

def test_empty_list():
    assert sum_squares([]) == 0

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
        else:
            total += num
    return total

def test_empty_list():
    assert sum_squares([]) == 0

def test_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_mixed_positive_negative():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 605

def test_large_numbers():
    assert sum_squares([100, 200, 300, 400, 500]) == 550000

def test_index_multiples():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 605

def test_list_with_zeros():
    assert sum_squares([0, 0, 0, 0, 0]) == 0

def test_list_with_one_element():
    assert sum_squares([5]) == 5

def test_list_with_two_elements():
    assert sum_squares([1, 2]) == 3

def test_list_with_three_elements():
    assert sum_squares([1, 2, 3]) == 6

def test_list_with_four_elements():
    assert sum_squares([1, 2, 3, 4]) == 18

def test_list_with_five_elements():
    assert sum_squares([1, 2, 3, 4, 5]) == 33

def test_list_with_six_elements():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 54

def test_list_with_seven_elements():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7]) == 73

def test_list_with_eight_elements():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 98

def test_list_with_nine_elements():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 135

def test_list_with_ten_elements():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 170

def test_list_with_eleven_elements():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 209

def test_list_with_twelve_elements():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 265

def test_large_list():
    lst = list(range(1, 101))
    assert sum_squares(lst) == 348550