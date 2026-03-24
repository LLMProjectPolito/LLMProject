


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

def test_empty_list():
    assert sum_squares([]) == 0

def test_list_with_one_element():
    assert sum_squares([5]) == 5

def test_negative_numbers():
    assert sum_squares([-1, -2, -3, -4, -5]) == -1 + -2 + 9 + -64 + -5

def test_mixed_positive_and_negative():
    assert sum_squares([1, -2, 3, -4, 5, -6]) == 1 + -2 + 9 + -64 + 5 + -216

def test_list_with_zeros():
    assert sum_squares([0, 0, 0, 0, 0]) == 0

def test_list_with_floats_converted_to_int():
    assert sum_squares([1.0, 2.0, 3.0, 4.0, 5.0]) == 1 + 2 + 9 + 64 + 5

def test_list_with_mixed_types_converted_to_int():
    assert sum_squares([1, 2.5, "3", 4, 5]) == 1 + 2 + 9 + 64 + 5

def test_multiples_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 9 + 16 + 5 + 36 + 7 + 64 + 81 + 10 + 11 + 144

def test_edge_case_multiple_of_12():
    assert sum_squares([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 2 + 9 + 16 + 5 + 36 + 7 + 64 + 81 + 10 + 11 + 144

def test_large_numbers():
    assert sum_squares([100, 200, 300, 400, 500]) == 100 + 40000 + 90000 + 160000 + 250000