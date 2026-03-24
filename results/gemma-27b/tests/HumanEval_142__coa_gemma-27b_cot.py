


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
import math


# Focus: Index-based Calculations
import pytest

def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_basic_list():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_mixed_indices():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 605

def test_sum_squares_large_list():
    assert sum_squares(list(range(13))) == 861

# Focus: Empty List Handling
def test_empty_list():
    assert sum_squares([]) == 0

def test_empty_list_with_none():
    assert sum_squares([None]) == 0

# Focus: Positive/Negative Numbers
import pytest

def test_positive_numbers():
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 29
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 140

def test_negative_numbers():
    assert sum_squares([-1, -2, -3]) == -6
    assert sum_squares([-1, -5, 2, -1, -5]) == -126
    assert sum_squares([-1, -2, -3, -4, -5, -6]) == -29

def test_mixed_numbers():
    assert sum_squares([-1, 2, -3, 4, -5, 6]) == -29
    assert sum_squares([1, -2, 3, -4, 5, -6]) == 29