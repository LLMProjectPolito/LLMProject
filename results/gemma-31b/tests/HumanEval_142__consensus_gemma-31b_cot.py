


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
    """Test that an empty list returns 0."""
    assert sum_squares([]) == 0

def test_sum_squares_examples():
    """Test the examples provided in the docstring."""
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_single_element():
    """Test a list with one element (index 0 is a multiple of 3)."""
    assert sum_squares([2]) == 4
    assert sum_squares([-3]) == 9
    assert sum_squares([0]) == 0

def test_sum_squares_no_transformation():
    """Test indices that are neither multiples of 3 nor 4 (indices 1 and 2)."""
    # idx 0: 0^2 = 0, idx 1: 5, idx 2: 10
    assert sum_squares([0, 5, 10]) == 15

def test_sum_squares_multiple_of_4_not_3():
    """Test indices that are multiples of 4 but not 3."""
    # idx 0: 2^2 = 4
    # idx 1: 1
    # idx 2: 1
    # idx 3: 1^2 = 1
    # idx 4: 2^3 = 8
    # Sum: 4 + 1 + 1 + 1 + 8 = 15
    assert sum_squares([2, 1, 1, 1, 2]) == 15

def test_sum_squares_multiple_of_both():
    """Test indices that are multiples of both 3 and 4 (e.g., index 12 should be squared)."""
    # Create a list of 13 ones.
    # Multiples of 3: 0, 3, 6, 9, 12 (5 elements) -> 1^2 = 1
    # Multiples of 4 (not 3): 4, 8 (2 elements) -> 1^3 = 1
    # Others: 1, 2, 5, 7, 10, 11 (6 elements) -> 1
    # Total sum: 5 + 2 + 6 = 13
    assert sum_squares([1] * 13) == 13

def test_sum_squares_complex_case():
    """Test a longer list with various integers to ensure logic robustness."""
    # Indices for [2] * 13:
    # 0, 3, 6, 9, 12 (sq): 5 * 4 = 20
    # 4, 8 (cb): 2 * 8 = 16
    # 1, 2, 5, 7, 10, 11 (id): 6 * 2 = 12
    # Sum: 20 + 16 + 12 = 48
    assert sum_squares([2] * 13) == 48

def test_sum_squares_all_zeros():
    """Test that a list of zeros always returns 0."""
    assert sum_squares([0, 0, 0, 0, 0]) == 0

@pytest.mark.parametrize("lst, expected", [
    ([1, 1, 1], 3),                                # 1^2 + 1 + 1 = 3
    ([1, 1, 1, 1], 4),                             # 1^2 + 1 + 1 + 1^2 = 4
    ([1, 1, 1, 1, 1], 5),                          # 1^2 + 1 + 1 + 1^2 + 1^3 = 5
    ([2, 2, 2, 2, 2], 20),                         # 4 + 2 + 2 + 4 + 8 = 20
    ([-2, -2, -2, -2, -2], -4),                    # 4 - 2 - 2 + 4 - 8 = -4
    ([2, 2, 2, 2, 2, 2, 2], 26),                   # 4 + 2 + 2 + 4 + 8 + 2 + 4 = 26
])
def test_sum_squares_parametrized(lst, expected):
    assert sum_squares(lst) == expected