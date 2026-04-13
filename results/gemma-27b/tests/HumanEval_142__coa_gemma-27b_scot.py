


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
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 440

def test_sum_squares_only_multiples_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 14 + 36

def test_sum_squares_only_multiples_of_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 2 + 3 + 64 + 5 + 6 + 7 + 512

# Focus: Empty List/Null Input
def test_empty_list():
    assert sum_squares([]) == 0

def test_null_input():
    assert sum_squares(None) == 0

# Focus: Positive/Negative/Zero Integers
import pytest

def test_sum_squares_positive_integers():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 2 + 9 + 64 + 5 + 36
    assert sum_squares([3, 6, 9]) == 9 + 36 + 81
    assert sum_squares([4, 8, 12]) == 4 + 64 + 12

def test_sum_squares_negative_integers():
    assert sum_squares([-1, -2, -3, -4, -5, -6]) == -1 + -2 + 9 + -64 + -5 + 36
    assert sum_squares([-3, -6, -9]) == 9 + 36 + 81
    assert sum_squares([-4, -8, -12]) == -4 + 64 + -12

def test_sum_squares_zero_integers():
    assert sum_squares([0, 0, 0, 0, 0, 0]) == 0
    assert sum_squares([0, 3, 0, 4, 0, 6]) == 0 + 9 + 0 + 64 + 0 + 36