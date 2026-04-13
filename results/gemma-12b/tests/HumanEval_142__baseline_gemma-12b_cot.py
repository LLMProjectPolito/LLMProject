


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

def test_empty_list():
    """Test case for an empty list."""
    lst = []
    expected = 0
    assert sum_squares(lst) == expected

def test_list_with_only_multiples_of_3():
    """Test case for a list where only elements at multiples of 3 are modified."""
    lst = [1, 2, 3, 4, 5, 6]
    expected = 1 + 2 + 27 + 4 + 5 + 36
    assert sum_squares(lst) == expected

def test_list_with_only_multiples_of_4():
    """Test case for a list where only elements at multiples of 4 are modified."""
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    expected = 1 + 2 + 3 + 64 + 5 + 6 + 7 + 512
    assert sum_squares(lst) == expected

def test_list_with_multiples_of_both_3_and_4():
    """Test case for a list where elements at multiples of both 3 and 4 are modified."""
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    expected = 1 + 2 + 27 + 64 + 5 + 36 + 7 + 512 + 9 + 10 + 11 + 1728
    assert sum_squares(lst) == expected

def test_list_with_negative_numbers():
    """Test case for a list with negative numbers."""
    lst = [-1, -2, -3, -4, -5, -6]
    expected = 1 + 4 + 27 + 64 + 125 + 216
    assert sum_squares(lst) == expected

def test_list_with_mixed_positive_and_negative_numbers():
    """Test case for a list with mixed positive and negative numbers."""
    lst = [-1, -5, 2, -1, -5]
    expected = 1 + (-125) + 4 + 1 + (-125)
    assert sum_squares(lst) == -244

def test_list_with_zeros():
    """Test case for a list with zeros."""
    lst = [0, 1, 2, 3, 4, 5]
    expected = 0 + 1 + 4 + 27 + 64 + 25
    assert sum_squares(lst) == 121

def test_list_with_large_numbers():
    """Test case for a list with large numbers."""
    lst = [100, 200, 300, 400]
    expected = 10000 + 20000 + 90000 + 640000
    assert sum_squares(lst) == 760000

def test_list_with_duplicate_numbers():
    """Test case for a list with duplicate numbers."""
    lst = [1, 1, 1, 1, 1]
    expected = 1 + 1 + 1 + 1 + 1
    assert sum_squares(lst) == 5