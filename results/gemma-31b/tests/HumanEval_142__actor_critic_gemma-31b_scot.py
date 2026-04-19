


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

# The function sum_squares is assumed to be imported from the solution module.
# from solution import sum_squares 

@pytest.mark.parametrize("lst, expected", [
    # Provided examples
    ([1, 2, 3], 6),               # idx 0: 1^2=1; idx 1: 2; idx 2: 3 -> 1+2+3 = 6
    ([], 0),                      # Empty list -> 0
    ([-1, -5, 2, -1, -5], -126),  # idx 0: (-1)^2=1; idx 1: -5; idx 2: 2; idx 3: (-1)^2=1; idx 4: (-5)^3=-125 -> 1-5+2+1-125 = -126
])
def test_provided_examples(lst, expected):
    """Test the examples provided in the function docstring."""
    assert sum_squares(lst) == expected

def test_single_element():
    """Test a list with one element (index 0 is always a multiple of 3)."""
    # 5^2 = 25
    assert sum_squares([5]) == 25
    # (-3)^2 = 9
    assert sum_squares([-3]) == 9

def test_index_logic_priority():
    """
    Test the priority of rules.
    Index 0: Multiple of 3 and 4 -> Square
    Index 3: Multiple of 3 -> Square
    Index 4: Multiple of 4 (not 3) -> Cube
    Index 12: Multiple of 3 and 4 -> Square
    """
    # Indices: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    # Values:  2, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 2
    # Ops:     S, N, N, S, C, N, S, N, C, S, N, N, S
    # Result:  4, 1, 1, 4, 8, 1, 4, 1, 8, 4, 1, 1, 4
    # Sum: 4+1+1+4+8+1+4+1+8+4+1+1+4 = 42
    lst = [2, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 2]
    assert sum_squares(lst) == 42

def test_negative_numbers():
    """Test negative numbers to ensure squaring and cubing behave correctly."""
    # idx 0: (-2)^2 = 4
    # idx 1: -1
    # idx 2: -1
    # idx 3: (-2)^2 = 4
    # idx 4: (-2)^3 = -8
    # Sum: 4 - 1 - 1 + 4 - 8 = -2
    assert sum_squares([-2, -1, -1, -2, -2]) == -2

def test_zeros():
    """Test that zeros remain zero regardless of the operation."""
    assert sum_squares([0, 0, 0, 0, 0]) == 0

def test_non_transforming_indices():
    """
    Verify that indices that are not multiples of 3 or 4 remain unchanged.
    Index 0 is always squared, but indices 1 and 2 should be untouched.
    """
    # [10, 5, 5] -> 10^2 + 5 + 5 = 110
    assert sum_squares([10, 5, 5]) == 110

def test_floating_point_numbers():
    """Test that the function handles floating-point numbers correctly."""
    # idx 0: 1.5^2 = 2.25
    # idx 1: 2.0
    # idx 2: 3.0
    # Sum: 2.25 + 2.0 + 3.0 = 7.25
    assert sum_squares([1.5, 2.0, 3.0]) == pytest.approx(7.25)
    
    # idx 0: 2.0^2 = 4.0
    # idx 1: 1.0
    # idx 2: 1.0
    # idx 3: 2.0^2 = 4.0
    # idx 4: 2.0^3 = 8.0
    # Sum: 4 + 1 + 1 + 4 + 8 = 18.0
    assert sum_squares([2.0, 1.0, 1.0, 2.0, 2.0]) == pytest.approx(18.0)