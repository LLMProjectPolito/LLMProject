


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
    """Test the examples provided in the docstring to ensure basic requirements are met."""
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([]) == 0
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_empty_and_single():
    """Test edge cases regarding list length."""
    # Empty list
    assert sum_squares([]) == 0
    # Single element: Index 0 is a multiple of 3, so it should be squared
    assert sum_squares([2]) == 4  # 2^2
    assert sum_squares([-3]) == 9 # (-3)^2

def test_sum_squares_index_logic():
    """
    Test specific indices to ensure the priority of rules:
    Index 0: Multiple of 3 (and 4) -> Square
    Index 3: Multiple of 3 -> Square
    Index 4: Multiple of 4, not 3 -> Cube
    Index 12: Multiple of 3 and 4 -> Square (Rule 1 takes precedence)
    """
    # Index 0: 2^2 = 4
    # Index 1: 1 (no change)
    # Index 2: 1 (no change)
    # Index 3: 2^2 = 4
    # Index 4: 2^3 = 8
    # Total: 4 + 1 + 1 + 4 + 8 = 18
    assert sum_squares([2, 1, 1, 2, 2]) == 18

def test_sum_squares_precedence_rule():
    """
    Verify that if an index is a multiple of both 3 and 4 (e.g., index 12), 
    it is squared, NOT cubed.
    """
    # Create a list of 13 zeros, and put a 2 at index 12
    lst = [0] * 12 + [2]
    # Index 12 is multiple of 3 -> 2^2 = 4
    # If it were cubed (multiple of 4), it would be 8.
    assert sum_squares(lst) == 4

def test_sum_squares_negative_numbers():
    """Test how the function handles negative numbers with squaring and cubing."""
    # Index 0: (-2)^2 = 4
    # Index 1: -1 (no change)
    # Index 2: -1 (no change)
    # Index 3: (-2)^2 = 4
    # Index 4: (-2)^3 = -8
    # Total: 4 - 1 - 1 + 4 - 8 = -2
    assert sum_squares([-2, -1, -1, -2, -2]) == -2

def test_sum_squares_large_list():
    """Test a longer list to ensure the pattern holds over multiple cycles."""
    # Indices: 0(S), 1, 2, 3(S), 4(C), 5, 6(S), 7, 8(C), 9(S), 10, 11, 12(S)
    # Values: all 1s
    # Squares: 1^2 = 1
    # Cubes: 1^3 = 1
    # No change: 1
    # Since 1^2 and 1^3 are both 1, the sum should simply be the length of the list.
    assert sum_squares([1] * 13) == 13

def test_sum_squares_zeros():
    """Test that zeros are handled correctly."""
    assert sum_squares([0, 0, 0, 0, 0]) == 0