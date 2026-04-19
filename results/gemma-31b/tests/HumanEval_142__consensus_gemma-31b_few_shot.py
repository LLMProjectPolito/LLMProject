


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
    """Test with a single element (index 0 is a multiple of 3)."""
    assert sum_squares([2]) == 4
    assert sum_squares([-3]) == 9
    assert sum_squares([5]) == 25

def test_sum_squares_small_lists():
    """Test lists with lengths that don't reach the first multiple of 4."""
    # index 0: 2^2 = 4; index 1: 3; index 2: 4. Sum = 11
    assert sum_squares([2, 3, 4]) == 11
    # index 0: 5^2 = 25; index 1: 6. Sum = 31
    assert sum_squares([5, 6]) == 31
    # index 0: 4^2 = 16; index 1: 1; index 2: 1. Sum = 18
    assert sum_squares([4, 1, 1]) == 18

def test_sum_squares_logic_boundaries():
    """
    Verify the specific index rules:
    - index 0: multiple of 3 (square)
    - index 3: multiple of 3 (square)
    - index 4: multiple of 4, not 3 (cube)
    - index 12: multiple of 3 AND 4 (square)
    """
    # Indices: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    # Values:  2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,  2,  2
    # Mod:     S, N, N, S, C, N, S, N, C, S, N,  N,  S
    # Result:  4, 2, 2, 4, 8, 2, 4, 2, 8, 4, 2,  2,  4
    # Sum: 4+2+2+4+8+2+4+2+8+4+2+2+4 = 48
    lst = [2] * 13
    assert sum_squares(lst) == 48

def test_sum_squares_overlap_index_12():
    """Test index 12 which is a multiple of both 3 and 4 (multiple of 3 takes precedence)."""
    lst = [0] * 13
    lst[12] = 3
    # index 12: 3^2 = 9
    assert sum_squares(lst) == 9

def test_sum_squares_zeros():
    """Test with a list of zeros."""
    assert sum_squares([0, 0, 0, 0, 0]) == 0

def test_sum_squares_negatives():
    """Test with negative numbers to verify squaring and cubing behavior."""
    # idx 0: (-2)^2 = 4; idx 1: -2; idx 2: -2; idx 3: (-2)^2 = 4; idx 4: (-2)^3 = -8
    # Sum: 4 - 2 - 2 + 4 - 8 = -4
    assert sum_squares([-2, -2, -2, -2, -2]) == -4
    # idx 0: (-2)^2 = 4; idx 1: -1; idx 2: -1; idx 3: (-2)^2 = 4; idx 4: (-2)^3 = -8
    # Sum: 4 - 1 - 1 + 4 - 8 = -2
    assert sum_squares([-2, -1, -1, -2, -2]) == -2
    # idx 0: 1^2 = 1; idx 1: 0; idx 2: 0; idx 3: 0^2 = 0; idx 4: (-2)^3 = -8
    # Sum: 1 + 0 + 0 + 0 - 8 = -7
    assert sum_squares([1, 0, 0, 0, -2]) == -7

@pytest.mark.parametrize("lst, expected", [
    ([1, 1, 1, 1, 1], 5),     # idx 0: 1^2, idx 3: 1^2, idx 4: 1^3 -> 1+1+1+1+1 = 5
    ([2, 1, 1, 2, 1], 11),    # idx 0: 2^2, idx 3: 2^2, idx 4: 1^3 -> 4+1+1+4+1 = 11
    ([0, 1, 2, 0, 3], 30),    # idx 0: 0^2, idx 3: 0^2, idx 4: 3^3 -> 0+1+2+0+27 = 30
    ([1, 2, 1, 1, 2], 13),    # idx 0: 1^2, idx 3: 1^2, idx 4: 2^3 -> 1+2+1+1+8 = 13
    ([2, 1, 1, 2, 2], 18),    # idx 0: 2^2, idx 3: 2^2, idx 4: 2^3 -> 4+1+1+4+8 = 18
])
def test_sum_squares_parametrized(lst, expected):
    assert sum_squares(lst) == expected