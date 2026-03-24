


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

def sum_squares(lst):
    """
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    For lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] the output should be 190
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    for element in lst:
        if not isinstance(element, int):
            raise TypeError("List elements must be integers.")

    total_sum = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            total_sum += lst[i]**2
        elif i % 4 == 0 and i % 3 != 0:
            total_sum += lst[i]**3
        else:
            total_sum += lst[i]
    return total_sum

import pytest

def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_basic():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_negative():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_multiple_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 190

def test_sum_squares_zero():
    assert sum_squares([0, 1, 2, 3]) == 14

def test_sum_squares_long():
    assert sum_squares(list(range(20))) == 2485

def test_sum_squares_invalid_input_string():
    with pytest.raises(TypeError):
        sum_squares("not a list")

def test_sum_squares_invalid_input_float():
    with pytest.raises(TypeError):
        sum_squares([1, 2, 3.0])

def test_sum_squares_invalid_input_tuple():
    with pytest.raises(TypeError):
        sum_squares((1, 2, 3))

def test_sum_squares_large_mixed():
    assert sum_squares([-1, 2, -3, 4, 5, -6, 7, -8, 9, 0, -10, 11, 12, -13, 14, -15]) == 110

def test_sum_squares_index_multiple_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 190