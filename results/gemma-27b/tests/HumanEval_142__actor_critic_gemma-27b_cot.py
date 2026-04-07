


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
    assert sum_squares([]) == 0

def test_list_with_one_element():
    assert sum_squares([5]) == 25

def test_list_with_multiple_elements():
    assert sum_squares([1, 2, 3]) == 14

def test_list_with_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == 56

def test_list_with_mixed_positive_and_negative():
    assert sum_squares([1, -2, 3, -4, 5, -6]) == 91

def test_list_with_large_numbers():
    assert sum_squares([100, 200, 300, 400]) == 3000000

def test_list_with_many_small_numbers():
    assert sum_squares([1] * 1000) == 1000000

def test_list_with_floats():
    with pytest.raises(TypeError):
        sum_squares([1.0, 2.0, 3.0])

def test_list_with_strings():
    with pytest.raises(TypeError):
        sum_squares([1, "2", 3])

def test_list_with_mixed_types():
    with pytest.raises(TypeError):
        sum_squares([1, 2.0, "3"])

def test_large_list():
    large_list = list(range(1, 1001))
    expected_sum = sum(x**2 for x in large_list)
    assert sum_squares(large_list) == expected_sum