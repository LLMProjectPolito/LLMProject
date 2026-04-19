


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

def test_sum_squares_provided_examples():
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([]) == 0
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_single_element():
    # Index 0 is a multiple of 3 -> squared
    assert sum_squares([2]) == 4
    assert sum_squares([-3]) == 9
    assert sum_squares([0]) == 0

def test_sum_squares_index_3_logic():
    # Indices: 0(sq), 1, 2, 3(sq)
    # Values:  2, 2, 2, 2
    # Result:  4 + 2 + 2 + 4 = 12
    assert sum_squares([2, 2, 2, 2]) == 12

def test_sum_squares_index_4_logic():
    # Indices: 0(sq), 1, 2, 3(sq), 4(cu)
    # Values:  2, 2, 2, 2, 2
    # Result:  4 + 2 + 2 + 4 + 8 = 20
    assert sum_squares([2, 2, 2, 2, 2]) == 20

def test_sum_squares_index_12_overlap():
    # Index 12 is multiple of 3 and 4. 
    # Rule: square if multiple of 3. Cube if multiple of 4 AND NOT multiple of 3.
    # Therefore, index 12 must be squared.
    # List of 13 zeros except index 12 is 2.
    lst = [0] * 13
    lst[12] = 2
    # Index 0 is 0^2=0. Index 12 is 2^2=4.
    assert sum_squares(lst) == 4

def test_sum_squares_mixed_negatives():
    # Indices: 0(sq), 1, 2, 3(sq), 4(cu), 5, 6(sq)
    # Values:  -2, 3, -4, -5, -6, 7, -8
    # Calc:    (-2)^2 + 3 + (-4) + (-5)^2 + (-6)^3 + 7 + (-8)^2
    # Calc:    4 + 3 - 4 + 25 - 216 + 7 + 64 = -117
    assert sum_squares([-2, 3, -4, -5, -6, 7, -8]) == -117

@pytest.mark.parametrize("lst, expected", [
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 13), # All 1s, sum is just length
    ([0, 0, 0, 0, 0], 0),                          # All 0s
    ([10], 100),                                   # Index 0 squared
    ([0, 0, 0, 10], 100),                          # Index 3 squared
    ([0, 0, 0, 0, 10], 1000),                      # Index 4 cubed
])
def test_sum_squares_parametrized(lst, expected):
    assert sum_squares(lst) == expected