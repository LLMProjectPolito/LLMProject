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

def test_basic_list():
    assert sum_squares([1, 2, 3]) == 6

def test_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_mixed_numbers():
    assert sum_squares([1, -2, 3, -4, 5, -6]) == -13

def test_multiples_of_3():
    assert sum_squares([3, 6, 9, 1, 2, 4]) == 126

def test_multiples_of_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 136

def test_multiples_of_both():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 12]) == 216

def test_large_numbers():
    assert sum_squares([10, 20, 30, 40]) == 3000

def test_zeroes():
    assert sum_squares([0, 0, 0, 0, 0]) == 0

def test_single_element():
    assert sum_squares([5]) == 5

def test_single_element_multiple_of_3():
    assert sum_squares([3]) == 9

def test_single_element_multiple_of_4():
    assert sum_squares([4]) == 64