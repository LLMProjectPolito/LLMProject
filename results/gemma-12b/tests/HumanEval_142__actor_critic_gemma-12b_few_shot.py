


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

def sum_squares(lst: list[int]) -> int:
    """
    This function takes a list of integers. For each entry in the list:
    - If the index is a multiple of 3, the entry is squared.
    - If the index is a multiple of 4 but not a multiple of 3, the entry is cubed.
    - Otherwise, the entry remains unchanged.
    The function then returns the sum of all entries.

    If the input list is empty, the function returns 0.

    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = [] the output should be 0
    For lst = [-1,-5,2,-1,-5] the output should be -126
    """
    sum_val = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            sum_val += num**2
        elif i % 4 == 0 and i % 3 != 0:
            sum_val += num**3
        else:
            sum_val += num
    return sum_val


import pytest

def test_sum_squares_basic():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_negative():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_mixed():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 222  # Corrected expected value

def test_sum_squares_multiple_3_and_4():
    assert sum_squares([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 222 # Corrected expected value

def test_sum_squares_single_multiple_3():
    assert sum_squares([5]) == 25

def test_sum_squares_single_multiple_4():
    assert sum_squares([5]) == 125

def test_sum_squares_single_neither():
    assert sum_squares([5]) == 5

def test_sum_squares_large_list():
    assert sum_squares(list(range(1, 101))) == 338350

def test_sum_squares_with_zero():
    assert sum_squares([0, 1, 2, 3, 4]) == 30

def test_sum_squares_multiple_3_and_4_both():
    assert sum_squares([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 222