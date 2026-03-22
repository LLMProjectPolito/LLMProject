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
    for i in range(len(lst)):
        if i % 3 == 0 and i % 4 != 0:
            total += lst[i] ** 2
        elif i % 4 == 0 and i % 3 != 0:
            total += lst[i] ** 3
        else:
            total += lst[i]
    return total

def test_empty_list():
    assert sum_squares([]) == 0

def test_positive_numbers():
    assert sum_squares([1, 2, 3]) == 6

def test_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_mixed_numbers():
    assert sum_squares([-1, 2, -3, 4, -5]) == -12

def test_single_element():
    assert sum_squares([5]) == 25

def test_multiple_elements():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 56
    
def test_large_numbers():
    assert sum_squares([100, 200, 300]) == 900
    
def test_zero_values():
    assert sum_squares([0, 0, 0]) == 0