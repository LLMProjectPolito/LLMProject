


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
from your_module import sum_squares  # Replace your_module

def test_empty_list():
    assert sum_squares([]) == 0

def test_basic_list():
    assert sum_squares([1, 2, 3]) == 14

def test_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_mixed_numbers():
    assert sum_squares([1, -2, 3, -4, 5, -6]) == -11

def test_multiples_of_3():
    assert sum_squares([3, 6, 9, 1, 2, 4]) == 102

def test_multiples_of_4():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 131

def test_multiples_of_both():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 278

def test_large_numbers():
    assert sum_squares([10, 20, 30, 40]) == 100 + 8000 + 900 + 64000

def test_zeroes():
    assert sum_squares([0, 0, 0, 0, 0]) == 0

def test_single_element():
    assert sum_squares([5]) == 5

def test_single_element_multiple_of_3():
    assert sum_squares([3]) == 9

def test_single_element_multiple_of_4():
    assert sum_squares([4]) == 64

def test_list_with_zeros_and_negatives():
    assert sum_squares([0, -1, 2, -3, 4]) == -28

def test_list_with_large_negative_numbers():
    assert sum_squares([-10, -20, -30, -40]) == -100 + -8000 + -2700 + -64000

def test_list_with_floats_converted_to_int():
    assert sum_squares([1.0, 2.0, 3.0, 4.0]) == 14

def test_list_with_mixed_positive_and_negative_multiples():
    assert sum_squares([-3, 4, -6, 8, -9, 10]) == -27 + 64 + -216 + 512 + -729 + 100