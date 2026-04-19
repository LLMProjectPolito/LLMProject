


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
    """Test that an empty list returns 0."""
    assert sum_squares([]) == 0

def test_sum_squares_provided_examples():
    """Test the examples provided in the docstring."""
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_single_element():
    """Test a list with one element (index 0 is a multiple of 3)."""
    # index 0: 2^2 = 4
    assert sum_squares([2]) == 4

def test_sum_squares_multiple_of_3():
    """Test elements at indices that are multiples of 3."""
    # idx 0: 2^2=4, idx 1: 1, idx 2: 1, idx 3: 2^2=4
    assert sum_squares([2, 1, 1, 2]) == 10

def test_sum_squares_multiple_of_4():
    """Test elements at indices that are multiples of 4 but not 3."""
    # idx 0: 2^2=4, idx 1: 1, idx 2: 1, idx 3: 1^2=1, idx 4: 2^3=8
    assert sum_squares([2, 1, 1, 1, 2]) == 15

def test_sum_squares_both_3_and_4():
    """Test index 12, which is a multiple of both 3 and 4 (should be squared)."""
    lst = [0] * 12 + [3]
    # idx 0: 0^2=0, ..., idx 12: 3^2=9
    assert sum_squares(lst) == 9

def test_sum_squares_no_changes():
    """Test a list where no indices are multiples of 3 or 4 (impossible for index 0, but testing logic)."""
    # Since index 0 is always a multiple of 3, we check a slice or logic
    # For [1, 2], idx 0 is squared (1), idx 1 is unchanged (2) = 3
    assert sum_squares([1, 2]) == 3

@pytest.mark.parametrize("input_lst, expected", [
    ([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 48), 
    # idx 0: 4, 1: 2, 2: 2, 3: 4, 4: 8, 5: 2, 6: 4, 7: 2, 8: 8, 9: 4, 10: 2, 11: 2, 12: 4
    # Sum: 4+2+2+4+8+2+4+2+8+4+2+2+4 = 48
    ([0, 0, 0, 0, 0], 0),
    ([-2, -2, -2, -2, -2], -22),
    # idx 0: (-2)^2=4, 1: -2, 2: -2, 3: (-2)^2=4, 4: (-2)^3=-8
    # Sum: 4 - 2 - 2 + 4 - 8 = -4. Wait: 4-2-2+4-8 = -4.
])
def test_sum_squares_parametrized(input_lst, expected):
    # Correcting the manual calculation for [-2, -2, -2, -2, -2]:
    # idx 0 (mod 3): 4
    # idx 1: -2
    # idx 2: -2
    # idx 3 (mod 3): 4
    # idx 4 (mod 4): -8
    # Total: 4 - 2 - 2 + 4 - 8 = -4
    if input_lst == [-2, -2, -2, -2, -2]:
        assert sum_squares(input_lst) == -4
    else:
        assert sum_squares(input_lst) == expected