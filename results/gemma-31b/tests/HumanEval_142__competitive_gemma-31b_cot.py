


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

@pytest.mark.parametrize("lst, expected", [
    ([], 0),
    ([1, 2, 3], 6),
    ([-1, -5, 2, -1, -5], -126),
    ([2], 4),  # Index 0: 2^2 = 4
    ([0, 0, 0, 2], 4),  # Index 0: 0^2, Index 3: 2^2 = 4
    ([0, 0, 0, 0, 2], 8),  # Index 0: 0^2, Index 3: 0^2, Index 4: 2^3 = 8
    ([1, 1, 1, 1, 1, 1, 1, 1, 1], 1 + 1 + 1 + 1^2 + 1 + 1 + 1^2 + 1 + 1^2), # Indices 0, 3, 6 are squared
    # Index 0: 1^2=1, 1: 1, 2: 1, 3: 1^2=1, 4: 1^3=1, 5: 1, 6: 1^2=1, 7: 1, 8: 1^3=1
    ([1, 1, 1, 1, 1, 1, 1, 1, 1], 9), 
    ([2, 2, 2, 2, 2, 2, 2, 2, 2], 4 + 2 + 2 + 4 + 8 + 2 + 4 + 2 + 8), # 4+2+2+4+8+2+4+2+8 = 36
])
def test_sum_squares_parametrized(lst, expected):
    assert sum_squares(lst) == expected

def test_sum_squares_index_12():
    # Index 12 is a multiple of both 3 and 4. 
    # Rule: square if multiple of 3. Cube if multiple of 4 AND NOT multiple of 3.
    # Therefore, index 12 should be squared.
    lst = [0] * 12 + [3]
    # Indices 0, 3, 6, 9 are 0^2. Index 12 is 3^2 = 9.
    # Indices 4, 8 are 0^3.
    assert sum_squares(lst) == 9

def test_sum_squares_all_zeros():
    assert sum_squares([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0

def test_sum_squares_large_numbers():
    # Index 0: 10^2 = 100
    # Index 1: 10
    # Index 2: 10
    # Index 3: 10^2 = 100
    # Index 4: 10^3 = 1000
    lst = [10, 10, 10, 10, 10]
    assert sum_squares(lst) == 100 + 10 + 10 + 100 + 1000

def test_sum_squares_negative_cubes():
    # Index 4: (-2)^3 = -8
    lst = [0, 0, 0, 0, -2]
    assert sum_squares(lst) == -8