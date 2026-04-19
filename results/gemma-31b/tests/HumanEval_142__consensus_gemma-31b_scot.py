


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

def test_sum_squares_empty():
    """Test with an empty list."""
    assert sum_squares([]) == 0

def test_sum_squares_provided_examples():
    """Test the examples provided in the docstring."""
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_single_element():
    """Test a list with one element (index 0 is a multiple of 3)."""
    assert sum_squares([2]) == 4
    assert sum_squares([-3]) == 9

def test_sum_squares_both_3_and_4():
    """Test that index 12 (multiple of both 3 and 4) is squared (priority to 3)."""
    lst = [0] * 13
    lst[12] = 3
    # index 0: 0^2 = 0, index 12: 3^2 = 9
    assert sum_squares(lst) == 9

def test_sum_squares_mixed_long():
    """Test a longer list with mixed indices to verify all rules."""
    # Indices: 0(sq), 1, 2, 3(sq), 4(cb), 5, 6(sq), 7, 8(cb), 9(sq), 10, 11, 12(sq)
    # Values:  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
    # Calc:    1^2 + 2 + 3 + 4^2 + 5^3 + 6 + 7^2 + 8 + 9^3 + 10^2 + 11 + 12 + 13^2
    # Sum:     1 + 2 + 3 + 16 + 125 + 6 + 49 + 8 + 729 + 100 + 11 + 12 + 169 = 1231
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 1231

def test_sum_squares_negative_integers():
    """Test handling of negative integers for squaring and cubing."""
    # index 0: (-2)^2 = 4
    # index 1: -1
    # index 2: -1
    # index 3: (-2)^2 = 4
    # index 4: (-2)^3 = -8
    # Sum: 4 - 1 - 1 + 4 - 8 = -2
    assert sum_squares([-2, -1, -1, -2, -2]) == -2

def test_sum_squares_zeros():
    """Test with a list of zeros."""
    assert sum_squares([0, 0, 0, 0, 0]) == 0

def test_sum_squares_large_numbers():
    """Test with larger integers to ensure logic holds."""
    # Index 0: 100^2 = 10000
    # Index 1: 100
    # Index 2: 100
    # Index 3: 100^2 = 10000
    # Index 4: 100^3 = 1000000
    # Sum: 10000 + 100 + 100 + 10000 + 1000000 = 1020200
    lst = [100] * 5
    assert sum_squares(lst) == 1020200

@pytest.mark.parametrize("lst, expected", [
    ([1, 1, 1, 1, 1], 5), # 0:1^2, 1:1, 2:1, 3:1^2, 4:1^3 -> 5
    ([10, 10, 10, 10], 220), # 0:100, 1:10, 2:10, 3:100 -> 220
    ([10, 10, 10, 10, 10], 1220), # 0:100, 1:10, 2:10, 3:100, 4:1000 -> 1220
])
def test_sum_squares_parametrized(lst, expected):
    assert sum_squares(lst) == expected