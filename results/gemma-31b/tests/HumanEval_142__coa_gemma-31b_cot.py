


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
import math


# Focus: Logic Branches
import pytest

def test_sum_squares_logic_branches():
    # Index 0: mult of 3 (2^2=4)
    # Index 1: neither (2)
    # Index 2: neither (2)
    # Index 3: mult of 3 (2^2=4)
    # Index 4: mult of 4, not 3 (2^3=8)
    # Sum: 4 + 2 + 2 + 4 + 8 = 20
    assert sum_squares([2, 2, 2, 2, 2]) == 20

def test_sum_squares_overlap_branch():
    # Index 12 is a multiple of both 3 and 4.
    # It should hit the 'multiple of 3' branch (square) and NOT the 'multiple of 4' branch (cube).
    # lst = [2] * 13
    # Indices 0, 3, 6, 9, 12 -> 2^2 = 4 (5 entries)
    # Indices 4, 8 -> 2^3 = 8 (2 entries)
    # Indices 1, 2, 5, 7, 10, 11 -> 2 (6 entries)
    # Sum: (5 * 4) + (2 * 8) + (6 * 2) = 20 + 16 + 12 = 48
    assert sum_squares([2] * 13) == 48

def test_sum_squares_empty_branch():
    # Tests the empty list case
    assert sum_squares([]) == 0

# Focus: Boundary Values
import pytest

def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_single_element():
    # Index 0 is a multiple of 3, so it should be squared
    assert sum_squares([3]) == 9

def test_sum_squares_boundary_index_4():
    # Index 0: sq, 1: same, 2: same, 3: sq, 4: cube
    # [2, 2, 2, 2, 2] -> 2^2 + 2 + 2 + 2^2 + 2^3 = 4 + 2 + 2 + 4 + 8 = 20
    assert sum_squares([2, 2, 2, 2, 2]) == 20

# Focus: Value Scenarios
def test_sum_squares_mixed_values():
    # Index 0: 0^2=0, Index 1: -2, Index 2: 3, Index 3: (-1)^2=1, Index 4: 2^3=8, Index 5: 0
    # Sum: 0 - 2 + 3 + 1 + 8 + 0 = 10
    assert sum_squares([0, -2, 3, -1, 2, 0]) == 10

def test_sum_squares_large_values():
    # Index 0: 10^2=100, Index 1: 1, Index 2: 1, Index 3: 10^2=100, Index 4: 10^3=1000
    # Sum: 100 + 1 + 1 + 100 + 1000 = 1202
    assert sum_squares([10, 1, 1, 10, 10]) == 1202

def test_sum_squares_all_negative():
    # Index 0: (-2)^2=4, Index 1: -2, Index 2: -2, Index 3: (-2)^2=4, Index 4: (-2)^3=-8
    # Sum: 4 - 2 - 2 + 4 - 8 = -4
    assert sum_squares([-2, -2, -2, -2, -2]) == -4