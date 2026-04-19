


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
    assert sum_squares([]) == 0
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_index_zero():
    """
    Index 0 is a multiple of both 3 and 4. 
    According to rules: square if multiple of 3. 
    Cube if multiple of 4 AND NOT multiple of 3.
    Therefore, index 0 must be squared.
    """
    # [2] -> index 0: 2^2 = 4. Sum = 4.
    assert sum_squares([2]) == 4

def test_sum_squares_index_four():
    """
    Index 4 is a multiple of 4 and NOT a multiple of 3.
    It should be cubed.
    """
    # Indices: 0(sq), 1, 2, 3(sq), 4(cube)
    # Values: [1, 1, 1, 1, 2]
    # Modified: [1^2, 1, 1, 1^2, 2^3] = [1, 1, 1, 1, 8]
    # Sum: 12
    assert sum_squares([1, 1, 1, 1, 2]) == 12

def test_sum_squares_index_twelve():
    """
    Index 12 is a multiple of both 3 and 4.
    It should be squared (multiple of 3 takes precedence).
    """
    # Create a list of 13 zeros, and put a 2 at index 12.
    lst = [0] * 12 + [2]
    # Index 0, 3, 6, 9, 12 are squared.
    # Index 4, 8 are cubed.
    # Only index 12 has a non-zero value: 2^2 = 4.
    assert sum_squares(lst) == 4

def test_sum_squares_all_zeros():
    """Test with a list of zeros."""
    assert sum_squares([0, 0, 0, 0, 0]) == 0

def test_sum_squares_no_modification_indices():
    """
    Test indices that are neither multiples of 3 nor 4.
    Indices 1, 2, 5, 7, 10, 11...
    """
    # Index 0 is always a multiple of 3. To test non-modification, 
    # we look at indices 1 and 2.
    # [0, 5, 10] -> Idx 0: 0^2=0, Idx 1: 5, Idx 2: 10. Sum = 15.
    assert sum_squares([0, 5, 10]) == 15

def test_sum_squares_large_integers():
    """Test with larger integers to ensure power operations work."""
    # [10, 0, 0, 10] -> Idx 0: 10^2=100, Idx 3: 10^2=100. Sum = 200.
    assert sum_squares([10, 0, 0, 10]) == 200

def test_sum_squares_complex_sequence():
    """
    Comprehensive test for a longer list.
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    Idx 0: 1^2 = 1
    Idx 1: 2
    Idx 2: 3
    Idx 3: 4^2 = 16
    Idx 4: 5^3 = 125
    Idx 5: 6
    Idx 6: 7^2 = 49
    Idx 7: 8
    Idx 8: 9^3 = 729
    Idx 9: 10^2 = 100
    Idx 10: 11
    Idx 11: 12
    Idx 12: 13^2 = 169
    Sum: 1+2+3+16+125+6+49+8+729+100+11+12+169 = 1231
    """
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 1231