


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

def sum_squares(lst):
    """
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    """
    # Implementation is assumed to be provided; this suite tests the logic described.
    # To make the tests runnable, we include a reference implementation based on the prompt.
    res = []
    for i in range(len(lst)):
        if i % 3 == 0:
            res.append(lst[i]**2)
        elif i % 4 == 0:
            res.append(lst[i]**3)
        else:
            res.append(lst[i])
    return sum(res)

@pytest.mark.parametrize("lst, expected", [
    ([], 0),                                      # Empty list
    ([1, 2, 3], 6),                               # Example 1: idx 0 squared (1^2 + 2 + 3)
    ([-1, -5, 2, -1, -5], -126),                  # Example 3: idx 0 sq, idx 3 sq, idx 4 cube
    ([2], 4),                                     # Single element: idx 0 is multiple of 3
    ([0, 0, 0, 0, 0], 0),                         # All zeros
    ([1, 1, 1, 1, 1], 1 + 1 + 1 + 1 + 1),         # All ones (idx 0: 1^2, idx 3: 1^2, idx 4: 1^3) -> 5
    ([2, 2, 2, 2, 2], 4 + 2 + 2 + 4 + 8),         # idx 0: 2^2, idx 3: 2^2, idx 4: 2^3 -> 20
])
def test_sum_squares_basic(lst, expected):
    assert sum_squares(lst) == expected

def test_index_overlap_12():
    """
    Index 12 is a multiple of both 3 and 4. 
    The rule states: square if multiple of 3, cube if multiple of 4 AND NOT multiple of 3.
    Therefore, index 12 must be squared.
    """
    # Create a list of 13 zeros, with a 2 at index 12
    lst = [0] * 12 + [2]
    # idx 0: 0^2, idx 3: 0^2, idx 4: 0^3, idx 6: 0^2, idx 8: 0^3, idx 9: 0^2, idx 12: 2^2
    assert sum_squares(lst) == 4

def test_negative_cubing():
    """
    Test that negative numbers are cubed correctly (preserving sign) at index 4.
    """
    # idx 0: (-2)^2 = 4
    # idx 1: 0
    # idx 2: 0
    # idx 3: 0^2 = 0
    # idx 4: (-2)^3 = -8
    lst = [-2, 0, 0, 0, -2]
    assert sum_squares(lst) == -4

def test_large_integers():
    """
    Test with larger integers to ensure no overflow/precision issues.
    """
    lst = [100, 0, 0, 100, 100] 
    # idx 0: 100^2 = 10,000
    # idx 3: 100^2 = 10,000
    # idx 4: 100^3 = 1,000,000
    assert sum_squares(lst) == 1020000

def test_non_modified_indices():
    """
    Ensure indices 1, 2, 5, 7, 10, 11 are not modified.
    """
    # Indices: 0(sq), 1(no), 2(no), 3(sq), 4(cu), 5(no), 6(sq), 7(no)
    lst = [1, 10, 20, 1, 1, 30, 1, 40]
    # 1^2 + 10 + 20 + 1^2 + 1^3 + 30 + 1^2 + 40
    # 1 + 10 + 20 + 1 + 1 + 30 + 1 + 40 = 104
    assert sum_squares(lst) == 104