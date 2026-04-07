


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

def test_example_1():
    assert sum_squares([1, 2, 3]) == 6

def test_example_2():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_list_with_only_multiples_of_3():
    assert sum_squares([3, 6, 9]) == 3**2 + 6**2 + 9**2

def test_list_with_only_multiples_of_4():
    assert sum_squares([4, 8, 12]) == 4**3 + 8**3 + 12**3

def test_list_with_multiples_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 3**2 + 4**3 + 5 + 6**2 + 7 + 8**3 + 9**2 + 10 + 11 + 12**3

def test_list_with_negative_numbers():
    assert sum_squares([-1, -2, -3, -4]) == -1 + -2 + (-3)**2 + (-4)**3

def test_list_with_zeroes():
    assert sum_squares([0, 0, 0, 0]) == 0 + 0 + 0**2 + 0**3

def test_list_with_mixed_positive_and_negative():
    assert sum_squares([1, -2, 3, -4, 5, -6]) == 1 + (-2) + 3**2 + (-4)**3 + 5 + (-6)**2

def test_large_numbers():
    assert sum_squares([100, 200, 300, 400]) == 100 + 200 + 300**2 + 400**3

def test_single_element_list():
    assert sum_squares([5]) == 5

def test_single_element_multiple_of_3():
    assert sum_squares([3]) == 3**2

def test_single_element_multiple_of_4():
    assert sum_squares([4]) == 4**3

def test_list_with_floats_converted_to_int():
    assert sum_squares([1.0, 2.0, 3.0]) == 6

def test_list_with_strings_raises_typeerror():
    with pytest.raises(TypeError):
        sum_squares([1, "a", 3])