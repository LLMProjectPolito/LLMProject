


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
    ([1, 1, 1, 1, 1, 1, 1, 1, 1], 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1), # Wait, let's calculate carefully
    # Idx 0: 1^2=1, Idx 1: 1, Idx 2: 1, Idx 3: 1^2=1, Idx 4: 1^3=1, Idx 5: 1, Idx 6: 1^2=1, Idx 7: 1, Idx 8: 1^3=1
    # Sum: 1+1+1+1+1+1+1+1+1 = 9
    ([1, 1, 1, 1, 1, 1, 1, 1, 1], 9),
    ([2, 2, 2, 2, 2, 2, 2, 2, 2], 4 + 2 + 2 + 4 + 8 + 2 + 4 + 2 + 8), # 4+2+2+4+8+2+4+2+8 = 36
    ([2, 2, 2, 2, 2, 2, 2, 2, 2], 36),
])
def test_sum_squares_parametrized(lst, expected):
    assert sum_squares(lst) == expected

def test_sum_squares_index_12():
    """
    Index 12 is a multiple of both 3 and 4.
    According to rules: square if multiple of 3. 
    Cube if multiple of 4 AND NOT multiple of 3.
    Therefore, index 12 should be squared.
    """
    # List of 13 zeros, last element is 3. Index 12 is 3.
    lst = [0] * 12 + [3]
    # Index 0: 0^2, Index 3: 0^2, Index 6: 0^2, Index 9: 0^2, Index 12: 3^2 = 9
    # Index 4: 0^3, Index 8: 0^3
    assert sum_squares(lst) == 9

def test_sum_squares_negative_numbers():
    # Idx 0: (-2)^2 = 4
    # Idx 1: -1
    # Idx 2: -1
    # Idx 3: (-2)^2 = 4
    # Idx 4: (-2)^3 = -8
    lst = [-2, -1, -1, -2, -2]
    # 4 - 1 - 1 + 4 - 8 = -2
    assert sum_squares(lst) == -2

def test_sum_squares_large_values():
    # Idx 0: 10^2 = 100
    # Idx 4: 10^3 = 1000
    lst = [10, 0, 0, 0, 10]
    assert sum_squares(lst) == 1100