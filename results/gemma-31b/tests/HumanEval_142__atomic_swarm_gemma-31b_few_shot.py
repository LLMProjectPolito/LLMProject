


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

def test_sum_squares():
    assert sum_squares([1, 2, 3, 4, 5]) == 147

def test_empty_list():
    assert sum_squares([]) == 0

import pytest

def test_sum_squares_wrong_type():
    with pytest.raises(TypeError):
        sum_squares(None)