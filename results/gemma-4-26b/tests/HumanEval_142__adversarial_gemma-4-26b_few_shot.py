


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

# The function is assumed to be imported from the source module
# from solution import sum_squares

def test_docstring_examples():
    """Verify that the function satisfies the exact examples provided in the docstring."""
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([]) == 0
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_empty_list():
    """Ensure an empty list returns 0."""
    assert sum_squares([]) == 0

def test_single_element():
    """
    Index 0 is a multiple of 3 (0 % 3 == 0).
    The element should be squared.
    """
    assert sum_squares([5]) == 25
    assert sum_squares([0]) == 0
    assert sum_squares([-3]) == 9

def test_index_logic_boundaries():
    """
    Detailed check of the index rules:
    - Index 0: Multiple of 3 -> Square
    - Index 1: Neither -> Keep
    - Index 2: Neither -> Keep
    - Index 3: Multiple of 3 -> Square
    - Index 4: Multiple of 4 and NOT 3 -> Cube
    - Index 8: Multiple of 4 and NOT 3 -> Cube
    - Index 12: Multiple of 3 AND 4 -> Square (Rule 1 takes precedence)
    """
    # We use a list where every value is 2 to make math easy to track
    # Indices: 0(sq), 1(id), 2(id), 3(sq), 4(cu), 5(id), 6(sq), 7(id), 8(cu), 9(sq), 10(id), 11(id), 12(sq)
    # Values:  4,    2,    2,    4,    8,    2,    4,    2,    8,    4,     2,     2,     4
    test_list = [2] * 13
    expected_sum = (4 + 2 + 2 + 4 + 8 + 2 + 4 + 2 + 8 + 4 + 2 + 2 + 4)
    assert sum_squares(test_list) == expected_sum

@pytest.mark.parametrize("input_list, expected_output", [
    ([10, 10, 10, 10], 100 + 10 + 10 + 100), # Indices 0 and 3 are squared
    ([1, 1, 1, 1, 1], 1 + 1 + 1 + 1 + 1),    # No index is multiple of 3 or 4 (except 0 and 3)
    # Wait, let's re-verify: 
    # idx 0: sq (1), idx 1: id (1), idx 2: id (1), idx 3: sq (1), idx 4: cu (1)
    # Sum: 1+1+1+1+1 = 5
])
def test_small_lists_parametrized(input_list, expected_output):
    """Parametrized test for quick logic verification."""
    assert sum_squares(input_list) == expected_output

def test_negative_numbers():
    """
    Ensure squaring handles negatives (becomes positive) 
    and cubing handles negatives (stays negative).
    """
    # idx 0: (-2)^2 = 4
    # idx 1: -2
    # idx 2: -2
    # idx 3: (-2)^2 = 4
    # idx 4: (-2)^3 = -8
    # Sum: 4 - 2 - 2 + 4 - 8 = -4
    assert sum_squares([-2, -2, -2, -2, -2]) == -4

def test_large_integers():
    """Ensure the function handles large integers correctly (Python handles arbitrary precision)."""
    large_val = 10**6
    # idx 0: (10^6)^2 = 10^12
    # idx 1: 10^6
    # idx 2: 10^6
    # idx 3: (10^6)^2 = 10^12
    # Sum: 2*10^12 + 2*10^6
    assert sum_squares([large_val, large_val, large_val, large_val]) == (2 * 10**12 + 2 * 10**6)

def test_all_zeros():
    """Edge case: list of zeros."""
    assert sum_squares([0, 0, 0, 0, 0]) == 0