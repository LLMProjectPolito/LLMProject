


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

def test_sum_squares_example_1():
    """Test with the first provided example: [1, 2, 3]."""
    # i=0: 1^2=1; i=1: 2; i=2: 3. Sum = 6
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_example_3():
    """Test with the third provided example: [-1, -5, 2, -1, -5]."""
    # i=0: (-1)^2=1; i=1: -5; i=2: 2; i=3: (-1)^2=1; i=4: (-5)^3=-125. Sum = -126
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_single_element():
    """Test with a single element (index 0 is a multiple of 3)."""
    assert sum_squares([2]) == 4
    assert sum_squares([-3]) == 9
    assert sum_squares([0]) == 0

def test_sum_squares_index_logic():
    """
    Test a list long enough to trigger multiple rules.
    Indices:
    0: mult 3 -> square
    1: none   -> identity
    2: none   -> identity
    3: mult 3 -> square
    4: mult 4 (not 3) -> cube
    5: none   -> identity
    6: mult 3 -> square
    7: none   -> identity
    8: mult 4 (not 3) -> cube
    9: mult 3 -> square
    10: none  -> identity
    11: none  -> identity
    12: mult 3 -> square (even though it is also mult 4)
    """
    lst = [2] * 13
    # Calculation:
    # i=0: 2^2 = 4
    # i=1: 2
    # i=2: 2
    # i=3: 2^2 = 4
    # i=4: 2^3 = 8
    # i=5: 2
    # i=6: 2^2 = 4
    # i=7: 2
    # i=8: 2^3 = 8
    # i=9: 2^2 = 4
    # i=10: 2
    # i=11: 2
    # i=12: 2^2 = 4
    # Sum: 4+2+2+4+8+2+4+2+8+4+2+2+4 = 48
    assert sum_squares(lst) == 48

def test_sum_squares_zeros():
    """Test with a list of zeros."""
    assert sum_squares([0, 0, 0, 0, 0]) == 0

def test_sum_squares_all_ones():
    """Test with a list of ones (powers of 1 are always 1)."""
    assert sum_squares([1, 1, 1, 1, 1]) == 5

def test_sum_squares_negative_cubes():
    """Test that cubing negative numbers preserves the sign."""
    # i=0: (-2)^2 = 4
    # i=1: -2
    # i=2: -2
    # i=3: (-2)^2 = 4
    # i=4: (-2)^3 = -8
    # Sum: 4 - 2 - 2 + 4 - 8 = -4
    assert sum_squares([-2, -2, -2, -2, -2]) == -4