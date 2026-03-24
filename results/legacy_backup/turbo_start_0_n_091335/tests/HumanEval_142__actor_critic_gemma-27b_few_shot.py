def sum_squares(lst):
    """
    This function takes a list of integers and calculates a sum based on the index of each element.
    For elements at indices that are multiples of 3, the element is squared.
    For elements at indices that are multiples of 4 but not multiples of 3, the element is cubed.
    Elements at other indices are included in the sum unchanged.

    Examples:
    For lst = [1, 2, 3] the output should be 1**2 + 2 + 3**2 = 1 + 2 + 9 = 12
    For lst = [] the output should be 0
    For lst = [-1, -5, 2, -1, -5] the output should be (-1)**2 + -5 + 2**2 + (-1)**3 + (-5) = 1 - 5 + 4 - 1 - 5 = -6
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    for element in lst:
        if not isinstance(element, int):
            raise TypeError("List elements must be integers.")

    return sum(x**2 if i % 3 == 0 else x**3 if i % 4 == 0 and i % 3 != 0 else x for i, x in enumerate(lst))


import pytest

def test_sum_squares_basic():
    assert sum_squares([1, 2, 3]) == 12
    assert sum_squares([]) == 0
    assert sum_squares([-1, -5, 2, -1, -5]) == -6

def test_sum_squares_longer_list():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    expected = 1**2 + 2 + 3**2 + 4**3 + 5 + 6**2 + 7 + 8**3 + 9**2 + 10 + 11 + 12**2
    assert sum_squares(lst) == expected

def test_sum_squares_with_zero():
    expected = 0**2 + 1 + 2 + 3**2
    assert sum_squares([0, 1, 2, 3]) == expected

def test_sum_squares_negative_and_zero():
    expected = (-1)**2 + 0 + 1 + (-2)**3 + 2
    assert sum_squares([-1, 0, 1, -2, 2]) == expected

def test_sum_squares_mixed_positive_negative():
    expected = 1**2 + (-2) + 3**2 + (-4)**3 + 5
    assert sum_squares([1, -2, 3, -4, 5]) == expected

def test_sum_squares_type_error_not_list():
    with pytest.raises(TypeError):
        sum_squares("not a list")

def test_sum_squares_type_error_non_integer():
    with pytest.raises(TypeError):
        sum_squares([1, 2, "a"])

def test_sum_squares_large_numbers():
    lst = [1000, 2000, 3000]
    expected = 1000**2 + 2000 + 3000**2
    assert sum_squares(lst) == expected

def test_sum_squares_multiples_of_3_only():
    lst = [1, 2, 3, 4, 5, 6]
    expected = 1 + 2 + 3**2 + 4 + 5 + 6**2
    assert sum_squares(lst) == expected

def test_sum_squares_multiples_of_4_not_3():
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    expected = 1 + 2 + 3**2 + 4**3 + 5 + 6**2 + 7 + 8**3
    assert sum_squares(lst) == expected

def test_sum_squares_neither_multiple_of_3_nor_4():
    lst = [1, 2, 5, 7, 10, 11]
    expected = 1 + 2 + 5 + 7 + 10 + 11
    assert sum_squares(lst) == expected