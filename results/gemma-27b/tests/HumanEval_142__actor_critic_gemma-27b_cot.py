


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
    assert sum_squares([5]) == 5

def test_list_with_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == 56

def test_list_with_zeros():
    assert sum_squares([0, 0, 0, 0]) == 0

def test_list_with_mixed_positive_and_negative():
    assert sum_squares([1, -2, 3, -4, 5, -6]) == 41

def test_list_with_large_numbers():
    assert sum_squares([100, 200, 300, 400]) == 3000000

@pytest.mark.parametrize("lst, expected", [
    ([1, 2, 9], 1 + 4 + 81),
    ([1, 2, 3, 8], 1 + 4 + 9 + 64),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100 + 121 + 144),
])
def test_sum_of_squares_of_indices(lst, expected):
    assert sum_squares(lst) == expected

def test_large_list():
    large_list = list(range(1000))
    expected_sum = sum(i**2 for i in range(1000))
    assert sum_squares(large_list) == expected_sum

def test_list_with_very_large_numbers():
    assert sum_squares([10**9, 2*10**9]) == 5 * 10**18

def test_list_with_large_positive_and_negative():
    assert sum_squares([10**9, -2*10**9]) == 5 * 10**18

def test_list_with_floats():
    with pytest.raises(TypeError):
        sum_squares([1.0, 2.0, 3.0])

def test_list_with_strings():
    with pytest.raises(TypeError):
        sum_squares([1, "2", 3])

def test_list_with_mixed_types():
    with pytest.raises(TypeError):
        sum_squares([1, 2.0, "3"])