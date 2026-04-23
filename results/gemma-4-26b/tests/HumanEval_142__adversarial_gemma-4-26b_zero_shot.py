


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

# The function is assumed to be in the same scope or imported
# from the module under test.
# from solution import sum_squares

def test_sum_squares_empty_list():
    """Tests that an empty list returns 0."""
    assert sum_squares([]) == 0

@pytest.mark.parametrize("input_list, expected_output", [
    ([1, 2, 3], 6),  # idx 0: 1^2=1; idx 1: 2; idx 2: 3. Sum: 6
    ([-1, -5, 2, -1, -5], -126),  # idx 0: (-1)^2=1; idx 1: -5; idx 2: 2; idx 3: (-1)^2=1; idx 4: (-5)^3=-125. Sum: -126
])
def test_sum_squares_provided_examples(input_list, expected_output):
    """Tests the specific examples provided in the docstring."""
    assert sum_squares(input_list) == expected_output

def test_sum_squares_index_zero_logic():
    """
    Tests index 0. 0 is a multiple of 3 (and 4). 
    According to rules: if multiple of 3 -> square. 
    If multiple of 4 and NOT 3 -> cube.
    Since 0 is a multiple of 3, it must be squared.
    """
    assert sum_squares([5]) == 25  # 5^2

def test_sum_squares_multiple_of_three():
    """Tests indices that are multiples of 3 but not 4 (e.g., index 3, 6, 9)."""
    # idx 0: 2^2=4; idx 1: 2; idx 2: 2; idx 3: 2^2=4. Sum: 4+2+2+4 = 12
    assert sum_squares([2, 2, 2, 2]) == 12
    # idx 0: 1^2=1; idx 1: 1; idx 2: 1; idx 3: 1^2=1; idx 4: 1; idx 5: 1; idx 6: 1^2=1. Sum: 7
    assert sum_squares([1, 1, 1, 1, 1, 1, 1]) == 7

def test_sum_squares_multiple_of_four_not_three():
    """Tests indices that are multiples of 4 but not 3 (e.g., index 4, 8, 16)."""
    # idx 0: 1^2=1; idx 1: 1; idx 2: 1; idx 3: 1^2=1; idx 4: 2^3=8. Sum: 1+1+1+1+8 = 12
    assert sum_squares([1, 1, 1, 1, 2]) == 12

def test_sum_squares_multiple_of_both_three_and_four():
    """
    Tests index 12 (multiple of both 3 and 4).
    Rule: square if multiple of 3.
    Rule: cube if multiple of 4 AND NOT 3.
    Therefore, index 12 should be squared.
    """
    # Create list of 13 elements (indices 0 to 12)
    # idx 0, 3, 6, 9, 12 (5 items) -> squared: 2^2 = 4. Total = 20
    # idx 4, 8 (2 items) -> cubed: 2^3 = 8. Total = 16
    # idx 1, 2, 5, 7, 10, 11 (6 items) -> unchanged: 2. Total = 12
    # Expected sum: 20 + 16 + 12 = 48
    lst = [2] * 13
    assert sum_squares(lst) == 48

def test_sum_squares_negative_numbers():
    """Tests that squaring negative numbers results in positive and cubing preserves sign."""
    # idx 0: (-2)^2 = 4
    # idx 1: -2
    # idx 2: -2
    # idx 3: (-2)^2 = 4
    # idx 4: (-2)^3 = -8
    # Sum: 4 - 2 - 2 + 4 - 8 = -4
    assert sum_squares([-2, -2, -2, -2, -2]) == -4

def test_sum_squares_zeros():
    """Tests that the function handles zeros correctly."""
    assert sum_squares([0, 0, 0, 0, 0]) == 0

def test_sum_squares_large_integers():
    """Tests the function with larger integer values."""
    large_val = 10**5
    # idx 0: (10^5)^2 = 10^10
    # idx 1: 10^5
    # Sum: 10,000,100,000
    assert sum_squares([large_val, large_val]) == 10000100000

def test_sum_squares_type_error():
    """Tests that the function raises TypeError if input is not a list (Robustness check)."""
    with pytest.raises(TypeError):
        sum_squares(None)
    with pytest.raises(TypeError):
        sum_squares(123)