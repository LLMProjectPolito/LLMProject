def sum_squares(lst: list[int]) -> int:
    """
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 

    Examples:
    >>> sum_squares([1,2,3])
    6
    >>> sum_squares([])
    0
    >>> sum_squares([-1,-5,2,-1,-5])
    -126
    >>> sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    300
    >>> sum_squares([0, 0, 0, 0])
    0
    >>> sum_squares([-2, -4, -6, -8])
    -200
    >>> sum_squares([1, 2, 3, 4, 5, 6, 7, 8])
    160
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
        elif i % 4 == 0:
            total_sum += lst[i]**3
        else:
            total_sum += lst[i]
    return total_sum

import pytest

def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_positive():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_negative():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_mixed():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 300

def test_sum_squares_zeros():
    assert sum_squares([0, 0, 0, 0]) == 0

def test_sum_squares_negative_only():
    assert sum_squares([-2, -4, -6, -8]) == -200

def test_sum_squares_long_list():
    assert sum_squares(list(range(20))) == 2870

def test_sum_squares_mixed_cubing_squaring():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 160

def test_sum_squares_type_error_list():
    with pytest.raises(TypeError):
        sum_squares("not a list")

def test_sum_squares_type_error_element():
    with pytest.raises(TypeError):
        sum_squares([1, 2, "a"])