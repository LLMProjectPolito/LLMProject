


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
    This function takes a list of integers. For all entries in the list, the function squares the integer entry if its index is a 
    multiple of 3 and cubes the integer entry if its index is a multiple of 4 and not a multiple of 3. 
    The function does not change the entries in the list whose indexes are not a multiple of 3 or 4, and these entries are excluded from the sum.
    The function then returns the sum of all modified entries.

    Examples:
    For lst = [1,2,3] the output should be 6 (1**2 + 2 + 3**2 = 1 + 2 + 9 = 12)
    For lst = [] the output should be 0
    For lst = [-1,-5,2,-1,-5] the output should be -4 ((-1)**2 + -5 + 2**2 + (-1)**2 + -5 = 1 - 5 + 4 + 1 - 5 = -4)
    For lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] the output should be 272
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    for element in lst:
        if not isinstance(element, int):
            raise TypeError("List elements must be integers.")

    return sum(x**2 for i, x in enumerate(lst) if i % 3 == 0) + sum(x**3 for i, x in enumerate(lst) if i % 4 == 0 and i % 3 != 0)

import pytest

def test_sum_squares_basic1():
    assert sum_squares([1, 2, 3]) == 12

def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_basic2():
    assert sum_squares([-1, -5, 2, -1, -5]) == -4

def test_sum_squares_length_12():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 272

def test_sum_squares_with_zero():
    assert sum_squares([0, 1, 2, 3, 4]) == 10

def test_sum_squares_negative_and_zero():
    assert sum_squares([-1, 0, 1, -2, 2]) == 2

def test_sum_squares_type_error_not_list():
    with pytest.raises(TypeError):
        sum_squares("not a list")

def test_sum_squares_type_error_non_integer():
    with pytest.raises(TypeError):
        sum_squares([1, 2, "a"])

def test_sum_squares_large_list():
    large_list = list(range(100))
    # Calculate expected value manually to avoid potential overflow issues
    expected_sum = sum(x**2 for i, x in enumerate(large_list) if i % 3 == 0) + sum(x**3 for i, x in enumerate(large_list) if i % 4 == 0 and i % 3 != 0)
    assert sum_squares(large_list) == expected_sum