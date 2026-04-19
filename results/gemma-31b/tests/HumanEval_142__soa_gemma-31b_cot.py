


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
    """Test with an empty list."""
    assert sum_squares([]) == 0

def test_sum_squares_provided_examples():
    """Test the examples provided in the docstring."""
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_single_element():
    """Test with a single element (index 0 is a multiple of 3)."""
    # Index 0: 2^2 = 4
    assert sum_squares([2]) == 4
    # Index 0: (-3)^2 = 9
    assert sum_squares([-3]) == 9

def test_sum_squares_index_logic():
    """
    Test specific index rules:
    Index 0: multiple of 3 -> square
    Index 1: neither -> keep
    Index 2: neither -> keep
    Index 3: multiple of 3 -> square
    Index 4: multiple of 4 (not 3) -> cube
    Index 5: neither -> keep
    Index 6: multiple of 3 -> square
    Index 7: neither -> keep
    Index 8: multiple of 4 (not 3) -> cube
    """
    # lst = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    # Idx 0: 1^2 = 1
    # Idx 1: 1
    # Idx 2: 1
    # Idx 3: 1^2 = 1
    # Idx 4: 1^3 = 1
    # Idx 5: 1
    # Idx 6: 1^2 = 1
    # Idx 7: 1
    # Idx 8: 1^3 = 1
    # Sum = 9
    assert sum_squares([1] * 9) == 9

    # lst = [2, 2, 2, 2, 2, 2, 2, 2, 2]
    # Idx 0: 2^2 = 4
    # Idx 1: 2
    # Idx 2: 2
    # Idx 3: 2^2 = 4
    # Idx 4: 2^3 = 8
    # Idx 5: 2
    # Idx 6: 2^2 = 4
    # Idx 7: 2
    # Idx 8: 2^3 = 8
    # Sum = 4+2+2+4+8+2+4+2+8 = 36
    assert sum_squares([2] * 9) == 36

def test_sum_squares_multiple_of_both():
    """Test index 12, which is a multiple of both 3 and 4 (should be squared)."""
    # Create list of 13 zeros, last element is 2
    lst = [0] * 12 + [2]
    # Index 12 is multiple of 3 -> 2^2 = 4
    # All other indices are 0
    assert sum_squares(lst) == 4

def test_sum_squares_negatives():
    """Test with negative numbers to ensure squaring and cubing behave correctly."""
    # Idx 0: (-2)^2 = 4
    # Idx 1: -2
    # Idx 2: -2
    # Idx 3: (-2)^2 = 4
    # Idx 4: (-2)^3 = -8
    # Sum: 4 - 2 - 2 + 4 - 8 = -4
    assert sum_squares([-2, -2, -2, -2, -2]) == -4

def test_sum_squares_zeros():
    """Test with a list of zeros."""
    assert sum_squares([0, 0, 0, 0, 0]) == 0

@pytest.mark.parametrize("lst, expected", [
    ([1, 2, 3], 6),
    ([], 0),
    ([-1, -5, 2, -1, -5], -126),
    ([10], 100),
    ([0, 0, 0, 0, 2], 8), # Idx 0:0, 1:0, 2:0, 3:0, 4:2^3=8
])
def test_sum_squares_parametrized(lst, expected):
    assert sum_squares(lst) == expected