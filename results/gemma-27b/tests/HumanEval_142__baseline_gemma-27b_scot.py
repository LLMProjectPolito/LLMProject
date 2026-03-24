


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
    new_lst = []
    for i, num in enumerate(lst):
        if i % 3 == 0:
            new_lst.append(num**2)
        elif i % 4 == 0:
            new_lst.append(num**3)
        else:
            new_lst.append(num)
    return sum(new_lst)

def test_empty_list():
    assert sum_squares([]) == 0

def test_example_1():
    assert sum_squares([1, 2, 3]) == 6

def test_example_2():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_multiples_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 2 + 9 + 4 + 5 + 36

def test_multiples_of_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 2 + 3 + 64 + 5 + 6 + 7 + 512

def test_multiples_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 9 + 64 + 5 + 6 + 7 + 512 + 81 + 10 + 11 + 144

def test_negative_numbers():
    assert sum_squares([-1, -2, -3, -4]) == 1 + -2 + 9 + -64

def test_large_list():
    lst = list(range(20))
    expected_sum = 0
    for i in range(20):
        if i % 3 == 0:
            expected_sum += i**2
        elif i % 4 == 0:
            expected_sum += i**3
        else:
            expected_sum += i
    assert sum_squares(lst) == expected_sum

def test_mixed_numbers():
    assert sum_squares([-1, 2, -3, 4, -5, 6]) == 1 + 2 + 9 + 64 + -5 + 36