


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

def test_sum_squares_multiple_of_3_branch():
    # Index 0 and 3 are multiples of 3 (squared)
    assert sum_squares([2, 0, 0, 2]) == 8 
    # Index 12 is multiple of both 3 and 4; logic specifies multiple of 3 takes precedence (squared)
    assert sum_squares([0] * 12 + [3]) == 9

def test_sum_squares_multiple_of_4_not_3_branch():
    # Index 4 and 8 are multiples of 4 and not 3 (cubed)
    # Index 0 is mult 3 (0^2), Index 3 is mult 3 (0^2)
    assert sum_squares([0, 0, 0, 0, 2, 0, 0, 0, 2]) == 16 # 2^3 + 2^3

def test_sum_squares_neither_branch():
    # Index 1, 2, 5 are neither multiples of 3 nor 4 (unchanged)
    # Index 0 (0^2), Index 3 (0^2), Index 4 (0^3)
    assert sum_squares([0, 5, 5, 0, 0, 5]) == 15

# Focus: Boundary Values
import pytest

def test_sum_squares_empty():
    """Boundary value: Empty list."""
    assert sum_squares([]) == 0

def test_sum_squares_single_element():
    """Boundary value: Single element (index 0 is a multiple of 3)."""
    assert sum_squares([2]) == 4

def test_sum_squares_index_boundaries():
    """Boundary value: List length covering the first transition points (indices 3 and 4)."""
    # Index 0: 2^2=4, Index 1: 1, Index 2: 1, Index 3: 2^2=4, Index 4: 2^3=8
    assert sum_squares([2, 1, 1, 2, 2]) == 18

# Focus: Input Value Scenarios
def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_negative_values():
    # idx 0: (-1)^2=1, idx 1: -5, idx 2: 2, idx 3: (-1)^2=1, idx 4: (-5)^3=-125
    # Sum: 1 - 5 + 2 + 1 - 125 = -126
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_zeros():
    assert sum_squares([0, 0, 0, 0, 0]) == 0