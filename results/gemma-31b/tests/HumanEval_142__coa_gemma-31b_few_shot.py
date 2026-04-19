


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
    # Index 0: mult 3 (sq), Index 1: neither, Index 2: neither, Index 3: mult 3 (sq), Index 4: mult 4 not 3 (cube)
    # [2, 2, 2, 2, 2] -> 2^2 + 2 + 2 + 2^2 + 2^3 = 4 + 2 + 2 + 4 + 8 = 20
    assert sum_squares([2, 2, 2, 2, 2]) == 20

def test_sum_squares_overlap_branch():
    # Index 12 is a multiple of both 3 and 4. 
    # According to logic: "square if index is multiple of 3" takes precedence.
    # Create list where only index 12 is non-zero.
    lst = [0] * 12 + [3]
    # Index 12: 3^2 = 9
    assert sum_squares(lst) == 9

def test_sum_squares_no_modification_branch():
    # Test indices that are neither multiples of 3 nor 4 (e.g., 1, 2, 5, 7)
    # Index 0: 1^2=1, Index 1: 2, Index 2: 3, Index 3: 4^2=16, Index 4: 5^3=125, Index 5: 6
    # Sum: 1 + 2 + 3 + 16 + 125 + 6 = 153
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 153

# Focus: Boundary Values
def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_single_element():
    # Index 0 is a multiple of 3, so it should be squared
    assert sum_squares([3]) == 9

def test_sum_squares_boundary_indices():
    # Index 0: multiple of 3 (sq) -> 2^2 = 4
    # Index 1: neither -> 2
    # Index 2: neither -> 2
    # Index 3: multiple of 3 (sq) -> 2^2 = 4
    # Index 4: multiple of 4 and not 3 (cube) -> 2^3 = 8
    # Total: 4 + 2 + 2 + 4 + 8 = 20
    assert sum_squares([2, 2, 2, 2, 2]) == 20

# Focus: Value Scenarios
import pytest

def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_negatives():
    # Idx 0: (-1)^2=1, Idx 1: -2, Idx 2: -3, Idx 3: (-4)^2=16, Idx 4: (-5)^3=-125
    # Sum: 1 - 2 - 3 + 16 - 125 = -113
    assert sum_squares([-1, -2, -3, -4, -5]) == -113

def test_sum_squares_zeros_and_ones():
    # Idx 0: 0^2=0, Idx 1: 1, Idx 2: 0, Idx 3: 1^2=1, Idx 4: 0^3=0
    # Sum: 0 + 1 + 0 + 1 + 0 = 2
    assert sum_squares([0, 1, 0, 1, 0]) == 2