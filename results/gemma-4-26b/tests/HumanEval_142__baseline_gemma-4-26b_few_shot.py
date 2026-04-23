


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
    """Tests that an empty list returns 0."""
    assert sum_squares([]) == 0

def test_sum_squares_provided_examples():
    """Tests the specific examples provided in the docstring."""
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_single_element():
    """Tests a single element at index 0 (multiple of 3)."""
    assert sum_squares([5]) == 25  # 5^2

def test_sum_squares_index_logic():
    """
    Tests specific indices to ensure the math logic is applied correctly:
    Index 0: Multiple of 3 -> Square
    Index 1: Neither -> No change
    Index 2: Neither -> No change
    Index 3: Multiple of 3 -> Square
    Index 4: Multiple of 4 (not 3) -> Cube
    Index 5: Neither -> No change
    Index 6: Multiple of 3 -> Square
    """
    # [2, 2, 2, 2, 2, 2, 2]
    # idx 0: 2^2 = 4
    # idx 1: 2
    # idx 2: 2
    # idx 3: 2^2 = 4
    # idx 4: 2^3 = 8
    # idx 5: 2
    # idx 6: 2^2 = 4
    # Sum: 4 + 2 + 2 + 4 + 8 + 2 + 4 = 26
    assert sum_squares([2, 2, 2, 2, 2, 2, 2]) == 26

def test_sum_squares_precedence_rule():
    """
    Tests the rule that multiples of 3 take precedence over multiples of 4.
    Index 12 is a multiple of both 3 and 4. It should be squared, not cubed.
    """
    # Create a list of 13 elements (indices 0 to 12) all being 2
    lst = [2] * 13
    # idx 0: 4 (sq)
    # idx 1: 2
    # idx 2: 2
    # idx 3: 4 (sq)
    # idx 4: 8 (cube)
    # idx 5: 2
    # idx 6: 4 (sq)
    # idx 7: 2
    # idx 8: 8 (cube)
    # idx 9: 4 (sq)
    # idx 10: 2
    # idx 11: 2
    # idx 12: 4 (sq) - Precedence check: 12 is multiple of 3
    # Sum: 4+2+2+4+8+2+4+2+8+4+2+2+4 = 48
    assert sum_squares(lst) == 48

def test_sum_squares_with_zeros():
    """Tests that zeros are handled correctly (0^2 and 0^3 are 0)."""
    assert sum_squares([0, 0, 0, 0]) == 0

def test_sum_squares_negative_numbers():
    """Tests behavior with negative numbers to ensure squaring/cubing is correct."""
    # [ -2, -2, -2, -2, -2 ]
    # idx 0: (-2)^2 = 4
    # idx 1: -2
    # idx 2: -2
    # idx 3: (-2)^2 = 4
    # idx 4: (-2)^3 = -8
    # Sum: 4 - 2 - 2 + 4 - 8 = -4
    assert sum_squares([-2, -2, -2, -2, -2]) == -4