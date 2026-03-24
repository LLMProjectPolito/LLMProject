


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

def test_example_1():
    assert sum_squares([1, 2, 3]) == 6

def test_example_2():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_list_with_only_multiples_of_3():
    assert sum_squares([3, 6, 9]) == 126

def test_list_with_only_multiples_of_4():
    assert sum_squares([4, 8, 12]) == 748

def test_list_with_mixed_multiples():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 708

def test_list_with_negative_numbers():
    assert sum_squares([-1, -2, -3, -4, -5, -6]) == -146

def test_list_with_zeroes():
    assert sum_squares([0, 0, 0, 0]) == 0

def test_large_numbers():
    assert sum_squares([100, 200, 300, 400]) == 1000000

def test_single_element_list():
    assert sum_squares([5]) == 25

def test_list_with_decimal_numbers():
    with pytest.raises(TypeError):
        sum_squares([1.5, 2.5, 3.5])

def test_list_with_string_numbers():
    with pytest.raises(TypeError):
        sum_squares(['1', '2', '3'])