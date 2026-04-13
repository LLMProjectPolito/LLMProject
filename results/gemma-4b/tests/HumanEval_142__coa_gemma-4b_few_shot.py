


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


# Focus: Boundary Values
import pytest

def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_multiple_of_3():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_multiple_of_4_not_3():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 225

# Focus: Type Scenarios
import pytest

def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_no_multiples_of_3_or_4():
    assert sum_squares([1, 2, 3, 4, 5]) == 15

def test_sum_squares_multiple_of_3():
    assert sum_squares([1, 2, 3, 4, 5]) == 15

# Focus: Logic Branches
import pytest

def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_multiple_of_3():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_multiple_of_4_not_3():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 225