


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
        else:
            total += num
    return total


def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_basic():
    assert sum_squares([1, 2, 3]) == 1 + 2 + 3  # No changes
    assert sum_squares([1, 2, 3]) == 1 + 4 + 3 # index 0 is multiple of 3, so 1 becomes 1**2 = 1
    assert sum_squares([1, 2, 3]) == 1 + 2 + 27 # index 3 is multiple of 3, so 3 becomes 3**2 = 9
    assert sum_squares([1, 2, 3]) == 1 + 4 + 27 # index 0 is multiple of 3, so 1 becomes 1**2 = 1
    assert sum_squares([1, 2, 3]) == 1 + 4 + 27 # index 3 is multiple of 3, so 3 becomes 3**2 = 9

def test_sum_squares_multiple_operations():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 2 + 3 + 16 + 5 + 216 # index 0 is multiple of 3, so 1 becomes 1**2 = 1. index 2 is multiple of 3, so 3 becomes 3**2 = 9. index 3 is multiple of 4 and not 3, so 4 becomes 4**3 = 64. index 6 is multiple of 3, so 6 becomes 6**2 = 36
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 2 + 9 + 64 + 5 + 36 # index 0 is multiple of 3, so 1 becomes 1**2 = 1. index 2 is multiple of 3, so 3 becomes 3**2 = 9. index 3 is multiple of 4 and not 3, so 4 becomes 4**3 = 64. index 6 is multiple of 3, so 6 becomes 6**2 = 36

def test_sum_squares_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -1 + (-5) + 4 + (-1) + (-5) # No changes
    assert sum_squares([-1, -5, 2, -1, -5]) == 1 + 125 + 4 + 1 + 125 # index 0 is multiple of 3, so -1 becomes (-1)**2 = 1. index 1 is multiple of 4 and not 3, so -5 becomes (-5)**3 = -125. index 2 is multiple of 3, so 2 becomes 2**2 = 4. index 3 is multiple of 3, so -1 becomes (-1)**2 = 1. index 4 is multiple of 4 and not 3, so -5 becomes (-5)**3 = -125
    assert sum_squares([-1, -5, 2, -1, -5]) == 1 + (-125) + 4 + 1 + (-125) # index 0 is multiple of 3, so -1 becomes (-1)**2 = 1. index 1 is multiple of 4 and not 3, so -5 becomes (-5)**3 = -125. index 2 is multiple of 3, so 2 becomes 2**2 = 4. index 3 is multiple of 3, so -1 becomes (-1)**2 = 1. index 4 is multiple of 4 and not 3, so -5 becomes (-5)**3 = -125
    assert sum_squares([-1, -5, 2, -1, -5]) == -126