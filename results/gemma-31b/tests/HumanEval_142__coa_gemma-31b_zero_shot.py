


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

def test_sum_squares_mixed_branches():
    # Index 0: mult 3 (1^2=1), Index 1: neither (2), Index 2: neither (3), 
    # Index 3: mult 3 (4^2=16), Index 4: mult 4 not 3 (5^3=125)
    # Sum: 1 + 2 + 3 + 16 + 125 = 147
    assert sum_squares([1, 2, 3, 4, 5]) == 147

def test_sum_squares_priority_branch():
    # Index 12 is a multiple of both 3 and 4.
    # Logic specifies: square if multiple of 3; cube if multiple of 4 AND NOT multiple of 3.
    # Therefore, index 12 must be squared: 2^2 = 4.
    assert sum_squares([0] * 12 + [2]) == 4

def test_sum_squares_no_change_branch():
    # Indices 1, 2, 5, 7 are neither multiples of 3 nor 4.
    # Indices 0, 3, 4, 6 are multiples of 3 or 4 but contain 0.
    # Sum: 0 + 1 + 2 + 0 + 0 + 3 + 0 + 4 = 10
    assert sum_squares([0, 1, 2, 0, 0, 3, 0, 4]) == 10

# Focus: Boundary Values
import pytest

def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_single_element():
    # Index 0 is a multiple of 3, so 2^2 = 4
    assert sum_squares([2]) == 4

def test_sum_squares_boundary_index_4():
    # Index 0: 0^2=0, Index 1: 0, Index 2: 0, Index 3: 0^2=0, Index 4: 2^3=8
    assert sum_squares([0, 0, 0, 0, 2]) == 8

# Focus: Value Scenarios
def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_zeros():
    assert sum_squares([0, 0, 0, 0, 0]) == 0

def test_sum_squares_negatives():
    # idx 0: (-2)^2=4, idx 1: -2, idx 2: -2, idx 3: (-2)^2=4, idx 4: (-2)^3=-8
    # Sum: 4 - 2 - 2 + 4 - 8 = -4
    assert sum_squares([-2, -2, -2, -2, -2]) == -4