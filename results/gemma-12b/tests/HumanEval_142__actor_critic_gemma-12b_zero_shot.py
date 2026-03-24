


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
    assert sum_squares([1, 2, 3]) == 6

def test_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_mixed_numbers():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 225

def test_multiples_of_3():
    assert sum_squares([3, 6, 9, 12]) == 210

def test_multiples_of_4():
    assert sum_squares([4, 8, 12, 16]) == 208

def test_multiples_of_3_and_4():
    assert sum_squares([3, 4, 6, 8, 9, 12, 15, 16]) == 258

def test_large_numbers():
    assert sum_squares([100, 200, 300, 400]) == 300000

def test_duplicate_numbers():
    assert sum_squares([1, 1, 1, 1, 1]) == 5

def test_single_element():
    assert sum_squares([5]) == 5

def test_negative_and_positive():
    assert sum_squares([-2, 3, -4, 5, -6]) == -125

def test_list_with_floats():
    assert sum_squares([1.5, 2.5, 3.5]) == pytest.approx(20.75)

def test_list_with_zeros():
    assert sum_squares([0, 0, 0]) == 0

def test_single_negative_number():
    assert sum_squares([-5]) == -5

def test_numbers_close_to_max_int():
    assert sum_squares([2**31 - 1, -(2**31 - 1), 2**31 - 2, -(2**31 - 2)]) == 0

def test_list_with_none():
    with pytest.raises(TypeError):
        sum_squares([1, 2, None, 4])

def test_invalid_input_type():
    with pytest.raises(TypeError):
        sum_squares("not a list")

def test_list_with_non_numeric_values():
    with pytest.raises(TypeError):
        sum_squares([1, 2, "a", 4])

def test_very_large_numbers():
    """Checks for potential overflow with very large numbers."""
    assert sum_squares([10**9, -10**9, 2 * 10**9, -2 * 10**9]) == 0