


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

def test_empty_list():
    assert sum_squares([]) == 0

def test_basic_list():
    assert sum_squares([1, 2, 3]) == 6

def test_list_with_multiples_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 2 + 9 + 4 + 5 + 36

def test_list_with_multiples_of_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 2 + 3 + 64 + 5 + 6 + 7 + 512

def test_list_with_multiples_of_both_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 9 + 64 + 5 + 6 + 7 + 512 + 9 + 10 + 11 + 1728

def test_list_with_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == (-1)**2 + (-5)**2 + 2**2 + (-1)**3 + (-5)**3
    assert sum_squares([-1,-5,2,-1,-5]) == 1 + 25 + 4 + (-1) + (-125)

def test_list_with_zeros():
    assert sum_squares([0, 1, 2, 3, 4]) == 0 + 1 + 4 + 9 + 64

def test_large_list():
    lst = list(range(1, 21))
    expected_sum = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            expected_sum += num**2
        elif i % 4 == 0:
            expected_sum += num**3
        else:
            expected_sum += num
    assert sum_squares(lst) == expected_sum

def test_list_with_mixed_numbers():
    assert sum_squares([1, -2, 3, -4, 5, -6, 7, -8]) == 1 + 4 + 9 + (-64) + 25 + 36 + 49 + (-512)