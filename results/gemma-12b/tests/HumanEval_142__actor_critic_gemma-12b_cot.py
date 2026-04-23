


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
    total = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            total += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            total += num ** 3
        else:
            total += num
    return total

def test_empty_list():
    assert sum_squares([]) == 0

def test_element_at_index_0():
    assert sum_squares([5, 1, 2, 3, 4]) == 16

def test_element_at_index_1():
    assert sum_squares([1, 5, 2, 3, 4]) == 15

def test_element_at_index_2():
    assert sum_squares([1, 2, 5, 3, 4]) == 16

def test_basic_list():
    assert sum_squares([1, 2, 3]) == 6

def test_list_with_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_list_with_zeros():
    assert sum_squares([0, 1, 2, 3, 4]) == 10

def test_list_with_mixed_numbers():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 140

def test_list_with_only_multiples_of_3():
    assert sum_squares([3, 6, 9, 12]) == 210

def test_list_with_only_multiples_of_4():
    assert sum_squares([4, 8, 12, 16]) == 208

def test_list_with_multiples_of_both_3_and_4():
    assert sum_squares([3, 4, 6, 8, 9, 12]) == 156

def test_list_with_large_numbers():
    large_sum = 100**2 + 200**3 + 300
    assert sum_squares([100, 200, 300]) == large_sum

def test_large_numbers_overflow():
    assert sum_squares([1000, 2000, 3000]) == 1000000 + 8000000000 + 9000000000

def test_list_with_floats():
    with pytest.raises(TypeError):
        sum_squares([1.0, 2.0, 3.0])

def test_single_element_multiple_of_3():
    assert sum_squares([3]) == 9

def test_single_element_multiple_of_4():
    assert sum_squares([4]) == 64

def test_single_element_neither_multiple():
    assert sum_squares([5]) == 5

def test_negative_index():
    assert sum_squares([-1, -2, -3, -4]) == -126