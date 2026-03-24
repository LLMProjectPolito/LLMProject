


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

def test_sum_squares_basic():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_mixed_indices():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 605

# Focus: Empty List/Null Input
def test_empty_list():
    assert sum_squares([]) == 0

def test_null_input():
    assert sum_squares(None) == 0

# Focus: Positive, Negative, and Zero Values
import pytest

def test_sum_squares_positive_values():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 665
    assert sum_squares([1, 2, 3, 4]) == 30
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_negative_values():
    assert sum_squares([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12]) == -665
    assert sum_squares([-1, -2, -3, -4]) == -30
    assert sum_squares([-1, -2, -3]) == -6

def test_sum_squares_zero_values():
    assert sum_squares([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert sum_squares([0, 1, 0, 2, 0, 3]) == 14
    assert sum_squares([0, -1, 0, -2, 0, -3]) == -14